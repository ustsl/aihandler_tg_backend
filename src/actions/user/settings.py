from src.api.requests import put_request
from src.settings import API_DOMAIN, API_MAIN_TOKEN


async def update_language(user: str, lang: str) -> bool:
    url = f"{API_DOMAIN}v1/users/{str(user)}/settings"
    lang = str(lang).lower()
    await put_request(
        url=url,
        headers={"Authorization": API_MAIN_TOKEN},
        data={"language": lang},
    )
    return True
