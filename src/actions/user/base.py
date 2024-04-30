from src.api.requests import post_request, get_request
from src.settings import API_DOMAIN, HEADERS


async def get_or_create_user(telegram_id: str | int) -> dict:
    url = f"{API_DOMAIN}v1/users/"
    data = {"telegram_id": str(telegram_id)}
    result = await post_request(url=url, data=data, headers=HEADERS)
    return result


async def get_user(telegram_id: str | int) -> dict:
    url = f"{API_DOMAIN}v1/users/{str(telegram_id)}"
    result = await get_request(url=url, headers=HEADERS)
    return result
