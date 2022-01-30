"""My task for become Python Developer Senior(Trainee)."""
import asyncio
import hashlib

from randomless import Random

tasks = []
end_time = 5000


async def printing(text):
    """Print something async."""
    randomm = Random()
    seconds = randomm.randint(0, end_time) / 1000
    await asyncio.sleep(seconds)
    print(text)



    

async def main():
    """Run program."""
    tasks.append(asyncio.create_task(printing('danya')))
    tasks.append(asyncio.create_task(printing('Python Developer Trainee')))
    tasks.append(asyncio.create_task(printing('70000')))

    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

some_text = input()
print(hashlib.sha256(some_text.encode('utf-8')).hexdigest())
