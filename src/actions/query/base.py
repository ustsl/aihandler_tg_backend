from uuid import UUID

from src.api.requests import post_request
from src.settings import API_DOMAIN


async def post_query(
    telegram_id: str,
    query: str,
    prompt_id: UUID,
    token: UUID,
    story: list = [],
    vision: bool = True,
):
    if prompt_id:
        url = f"{API_DOMAIN}v1/queries/{str(telegram_id)}"
        data = {
            "prompt_id": str(prompt_id),
            "query": query,
            "story": story,
            "vision": vision,
        }
        result = await post_request(
            url=url, data=data, headers={"Authorization": token}
        )
        if result.get("result") and result.get("cost"):
            string = f'{result.get("result")}\n\nCost: ${result.get("cost")}'
            return {"result": string, "clean": result.get("result")}
        return result
    else:
        return {"result": "Prompt not selected. Please, use interface and set prompt"}
