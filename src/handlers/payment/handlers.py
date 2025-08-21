from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    LabeledPrice,
    Message,
    PreCheckoutQuery,
)

from src.api.payment import put_user_subscribe
from src.keyboards.main_kb import MainCallback, payment_keyboard, reverse_kb as kb
from src.settings import STARS_PRICE, SUBSCRIPTION_PRICE

# при желании: из настроек
# from src.settings import TELEGRAM_PROVIDER_TOKEN as PROVIDER_TOKEN

router = Router()

# --- Константы инвойса ---
TITLE = "Пополнить баланс на 100 STARS"
DESCRIPTION = "Деньги будут добавлены к вашему текущему балансу"
CURRENCY = "XTR"
PAYLOAD = "channel_support"
PROVIDER_TOKEN = ""  # подставьте боевой токен провайдера в проде


# --- Вспомогательные функции ---
def _prices() -> list[LabeledPrice]:
    # В Stars amount должен быть целым числом (единицы валюты XTR).
    return [LabeledPrice(label="XTR", amount=SUBSCRIPTION_PRICE)]


async def _send_invoice(msg: Message) -> None:
    await msg.answer_invoice(
        title=TITLE,
        description=DESCRIPTION,
        prices=_prices(),
        provider_token=PROVIDER_TOKEN,
        payload=PAYLOAD,
        currency=CURRENCY,
        reply_markup=payment_keyboard(),
    )


def _format_stars(balance_raw: float | int) -> str:
    # Баланс хранится в "денежных" единицах; переводим в ⭐
    stars = float(balance_raw) / STARS_PRICE
    # Обычно удобно показывать 2 знака
    return f"{stars:.2f}"


# --- Хендлеры ---
@router.message(Command(commands=["payment"]))
async def payment_by_command(message: Message) -> None:
    """Отправка инвойса по команде /payment."""
    await _send_invoice(message)


@router.callback_query(MainCallback.filter(F.action == "payment"))
async def payment_by_callback(query: CallbackQuery) -> None:
    """Отправка инвойса по нажатию кнопки."""
    if query.message:  # safety-guard
        await _send_invoice(query.message)


@router.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery) -> None:
    """Обязательное подтверждение перед оплатой."""
    await pre_checkout_query.answer(ok=True)


@router.message(F.successful_payment)
async def success_payment_handler(message: Message) -> None:
    """
    Срабатывает, когда Telegram прислал message.successful_payment.
    Начисляем ⭐ и уведомляем пользователя.
    """
    # Начисляем эквивалент 100 ⭐ в вашей валюте
    result = await put_user_subscribe(message.from_user.id, 100 * STARS_PRICE)

    if isinstance(result, dict) and result.get("status"):
        balance = result.get("balance")
        stars_text = _format_stars(balance)
        msg = (
            "<b>Баланс успешно пополнен!</b> 🤗\n"
            f"Ваш текущий баланс: ⭐️ {stars_text}"
        )
        await message.answer(msg, reply_markup=kb)
