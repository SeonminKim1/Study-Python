import asyncio
import time

# await asyncio.sleep(1)  # await : 기다리게 하기.
async def say_after(delay):
    await asyncio.sleep(delay)

# 1. create_task 사용 없이 실행 - 순차 실행 : 3초 소요
async def main1():
    print(f"1. started at {time.strftime('%X')}")
    await say_after(1)
    await say_after(2)
    print(f"1. finished at {time.strftime('%X')}")

# 2. create_task로 만들고 동시에 실행 - 동시 실행 : 2초 소요
async def main2():
    task1 = asyncio.create_task(
        say_after(1))

    task2 = asyncio.create_task(
        say_after(2))

    print(f"2. started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"2. finished at {time.strftime('%X')}")

asyncio.run(main1())
asyncio.run(main2())
