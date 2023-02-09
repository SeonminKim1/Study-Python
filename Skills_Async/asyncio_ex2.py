import asyncio
import time

# await asyncio.sleep(1)  # await : 기다리게 하기.
async def say_after(delay):
    await asyncio.sleep(delay)
    return 'OK'

# gather를 통해 한번에 실행하고 결과를 받음.
async def test():
    sec_list = [1, 2]
    tasks = [asyncio.create_task(say_after(sec)) for sec in sec_list]  # task list
    tasks_result = await asyncio.gather(*tasks) # task results list
    return tasks_result

if __name__ == "__main__":
    start = time.time()

    # loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(test())
    # loop.close()

    result = asyncio.run(test())

    end = time.time()

    print('result : {}'.format(result))
    print('total time : {0:.2f} sec'.format(end - start))