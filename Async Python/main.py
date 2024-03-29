# 导入异步库
import asyncio


# 定义一个异步函数
async def hello():
    print("Hello world!")
    # 异步调用 asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
