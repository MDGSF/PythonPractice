import time

import threading
import anyio
from asyncer import asyncify, syncify


# 这个异步函数会在主线程的 event_loop 中执行
async def do_async_work(name: str):
    thread_id = threading.current_thread().ident
    await anyio.sleep(1)
    return f"Hello, {name}, {thread_id}"


def do_sync_work(name: str):
    time.sleep(1)
    message = syncify(do_async_work)(name=name)
    return message


async def main():
    thread_id = threading.current_thread().ident
    print(f"main thread id: {thread_id}")
    message = await asyncify(do_sync_work)(name="World")
    print(message)


anyio.run(main)
