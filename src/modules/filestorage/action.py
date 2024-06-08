from src.settings import API_MAIN_TOKEN
import aiohttp
from typing import Dict, Optional


class FileStorageAction:
    def __init__(self):
        self.headers = {"Authorization": API_MAIN_TOKEN}

    async def download(self, url: str, file: bytes) -> Dict[str, Optional[bool]]:
        path = None
        is_downloaded = False

        try:
            async with aiohttp.ClientSession() as session:
                form_data = aiohttp.FormData()
                form_data.add_field(
                    "file", file, filename="image.jpg", content_type="image/jpeg"
                )

                async with session.post(
                    url, headers=self.headers, data=form_data
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        path = result.get("path")
                        is_downloaded = path is not None
        except aiohttp.ClientError as e:
            print(f"Network error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return {"path": path, "is_downloaded": is_downloaded}
