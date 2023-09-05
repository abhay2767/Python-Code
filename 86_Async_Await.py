import asyncio
import time
import requests

async def function1(): #Download file
    url = 'https://www.facebook.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('facebook.ico', 'wb').write(r.content)

    await asyncio.sleep(1)
    print("Function1")
    return "Abhay"

async def function2():
    await asyncio.sleep(1)
    print("Function2")

async def function3():
    await asyncio.sleep(4)
    print("Function3")

async def main():
    """ task = asyncio.create_task(function1())
    #await function1()
    await function2()
    await function3() """

    l = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(type(l),l)

asyncio.run(main())