import aiohttp


async def get_request(url, headers=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()


async def post_request(url, data=None, headers=None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            return await response.json()


async def put_request(url, data=None, headers=None):
    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=data, headers=headers) as response:
            return await response.json()
