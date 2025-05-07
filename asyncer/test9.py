import time

import asyncio
from asyncer import asyncify


def do_sync_work(name: str):
    time.sleep(3)
    return f"Hello, {name}"


async def main():
    message_awaitable = asyncify(do_sync_work)(name="World")
    message_task = asyncio.create_task(message_awaitable)
    print(type(message_task))
    print("main before sleep")
    await asyncio.sleep(5)
    print("main after sleep")
    message = await message_task
    print(message)


asyncio.run(main())
