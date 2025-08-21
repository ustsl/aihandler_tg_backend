from src.settings import STARS_PRICE


def start_message(user: str, balance: str, language: str):
    messages = {
        "en": f"""
    Hello {user}

<b>Welcome to IMVO AI</b> 

Create prompts and use them through a chatbot or via an API link. 
Earn money from your prompts or complete your own tasks. 

<b>How to get started</b> 

Use the Interface button in the menu to create your first prompt, or select someone else’s prompt from those available in the public domain. 

The chatbot works within the prompt you choose.  More information on the links in the menu.

<b>Your current balance is ${balance}</b>.
    """,
        "ru": f"""
    Привет {user}

<b>Добро пожаловать в IMVO AI</b> 

Создавайте промпты и используйте их через чат-бота или через API ссылку. 
Зарабатывайте деньги на своих промптах или выполняйте собственные задачи. 

<b>Как начать</b> 

Используйте кнопку "Интерфейс" в меню, чтобы создать свой первый промпт, или выберите чей-то промпт из доступных в публичном домене. 

Чат-бот работает в рамках выбранного вами промпта. Дополнительная информация по ссылкам в меню.

<b>Ваш текущий баланс: {round(float(balance) / STARS_PRICE, 2)} ⭐</b>
    """,
        "tr": f"""
    Merhaba {user}

<b>IMVO AI'ye hoş geldiniz</b> 

Promtlar oluşturun ve bunları bir chatbot veya API bağlantısı aracılığıyla kullanın. 
Promtlarınızdan para kazanın veya kendi görevlerinizi tamamlayın. 

<b>Nasıl başlanır</b> 

İlk promt'unuzu oluşturmak için menüdeki Arayüz düğmesini kullanın veya herkese açık alanda bulunan başka birinin promt'unu seçin. 

Chatbot, seçtiğiniz promt içinde çalışır. Menüdeki bağlantılarda daha fazla bilgi bulabilirsiniz.

<b>Mevcut bakiyeniz: {round(float(balance) / 0.013, 2)} ⭐</b>
    """,
    }

    return messages.get(language, messages["en"])


about_message = {
    "en": f"""
<b>IMVO.</b> AI provider in Telegram with flexible configuration options for prompts and payment in cryptocurrency for actual use.

<b>Create prompts</b> in a convenient interface, select appropriate models and the size of the memory window of past messages to fine-tune the bot.

<b>Use AI inside telegram.</b>

<b>Share the IDs</b> of your prompts and earn money from other people using them.

<b>Use cryptocurrency</b> to pay for the service. No restrictions.
    """,
    "ru": f"""
<b>IMVO.</b> Провайдер ИИ в Telegram с гибкими настройками для промптов и оплатой криптовалютой за фактическое использование.

<b>Создавайте промпты</b> в удобном интерфейсе, выбирайте подходящие модели и размер окна памяти для прошлых сообщений, чтобы точно настроить бота.

<b>Используйте ИИ внутри Telegram.</b>

<b>Делитесь ID</b> своих промптов и зарабатывайте деньги, когда другие люди их используют.

<b>Используйте криптовалюту</b> для оплаты услуг. Никаких ограничений.
    """,
    "tr": f"""
<b>IMVO.</b> Telegram'da esnek yapılandırma seçenekleri ve gerçek kullanım için kripto para birimi ile ödeme seçenekleri sunan bir AI sağlayıcısı.

<b>Promtlar oluşturun</b> kullanışlı bir arayüzde, uygun modelleri ve geçmiş mesajların hafıza penceresinin boyutunu seçerek botu ince ayar yapın.

<b>Telegram içinde AI kullanın.</b>

<b>Promtlarınızın ID'lerini paylaşın</b> ve başkalarının kullanmasından para kazanın.

<b>Kripto para birimi kullanın</b> hizmet için ödeme yapmak için. Hiçbir kısıtlama yok.
    """,
}
