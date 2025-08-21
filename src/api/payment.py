from src.api.requests import get_request, post_request, put_request
from src.settings import API_DOMAIN, HEADERS


async def put_user_subscribe(user, balance):
    url = f"{API_DOMAIN}v1/users/{user}/balance"
    data = {"balance": balance}
    result = await put_request(url=url, data=data, headers=HEADERS)
    return result
