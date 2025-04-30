import time

import asyncio
from asyncer import asyncify


# 会放到单独的线程中去运行
def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def main():
    tasks = [asyncify(do_sync_work)(name="World") for _ in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
