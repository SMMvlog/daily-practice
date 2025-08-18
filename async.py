import asyncio

async def task1():
    print("Task 1")
    await asyncio.sleep(3)
    print("task 1 end")
    return "taskkkkk1"

async def task2():
    print("task 2")
    await asyncio.sleep(5)
    print("end 2")
    return "taskkk2"

# task1()
# task2()

async def main():
    result = await asyncio.gather(task1(),task2())
    # result = await task2()
    print("result---",result)
asyncio.run(main())
# import time
# def task1():
#     print("Task 1")
#     time.sleep(3)
#     print("task 1 end")

# def task2():
#     print("task 2")
#     time.sleep(1)
#     print("end 2")

# task1()
# task2()


import asyncio

async def my_coroutine():
    print("Start")
    await asyncio.sleep(2)  # यहां pause होगा
    print("End")

asyncio.run(my_coroutine())
