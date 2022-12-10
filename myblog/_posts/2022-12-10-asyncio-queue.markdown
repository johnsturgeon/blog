---
layout: single
title:  "FastAPI: Writing a FIFO queue with asyncio.Queue"
date:   2022-12-10 08:31:32 -0800
categories: python asyncio fastapi
toc: true
---
### Summary
In this quick post I'm going to describe how to use [asyncio.Queue](https://docs.python.org/3/library/asyncio-queue.html)
in a FastAPI server for processing incoming requests in the background, and in the order that they
were received.

### Background

I am in the process of writing a [plugin for BakkesMod](https://github.com/johnsturgeon/stat-scraper) 
(Rocket League) to collect game stats.

It pushes game data rapidly to a FastAPI web server.  The problem was that some tasks were being 
processed out of order by workers depending on how long they were taking to run.  This was causing
issues with old data sometimes overwriting newer data.

### Things I tried

I tried using [FastAPI's BackgroundTasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) but I quickly 
discovered that those just throw the task into the background and run it immediately, and if a second
request came in, it would immediately start that background task even if the first one wasn't complete.

I thought of writing my own queue manager so I could just run the tasks one at a time, but surely that had
to already exist!

### Enter `asyncio.Queue`

It turned out to be incredibly simple to create a FIFO queue using `asyncio.Queue` in FastAPI, I'll walk you through it now.

#### Set up your FastAPI server and import `asyncio`

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app)
```

#### Create your fifo queue and attach it to your server

```python
app = FastAPI()

app.fifo_queue = asyncio.Queue()

```

#### Write a worker method

A worker method is a long-running method that you will start when your FastAPI server starts (more on that below).  
It is what manages the queue

```python
app.fifo_queue = asyncio.Queue()

async def fifo_worker():
    print("Starting DB Worker")
    while True:
        job = await app.fifo_queue.get()
        print(f"Got a job: (size of remaining queue: {app.fifo_queue.qsize()}")
        await job()
```

#### Start the worker on server start

```python
@app.on_event("startup")
async def start_db():
    asyncio.create_task(fifo_worker())

```

#### Write your long running background task
In this example, we're just sleeping, but your task is your task.

```python
async def do_a_slow_thing():
    print("in a slow task")
    await asyncio.sleep(5)
    print("done with slow thing")
```

#### Example route that needs to queue
This is an example of a route that needs to return to the caller immediately, and queue the work.
When you `put` a task on the queue, the worker will immediately `get` the task.

```python
@app.get("/queue")
async def queue():
    print("Queueing a job")
    await app.fifo_queue.put(do_a_slow_thing)
    return {"result": "success"}

```

### Putting it all together
The entire script:

```python
import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

app.fifo_queue = asyncio.Queue()


async def fifo_worker():
    print("Starting DB Worker")
    while True:
        job = await app.fifo_queue.get()
        print(f"Got a job: (size of remaining queue: {app.fifo_queue.qsize()}")
        await job()


async def do_a_slow_thing():
    print("in a slow task")
    await asyncio.sleep(5)
    print("done with slow thing")


@app.on_event("startup")
async def start_db():
    asyncio.create_task(fifo_worker())


@app.get("/queue")
async def queue():
    print("Queueing a job")
    await app.fifo_queue.put(do_a_slow_thing)
    return {"result": "success"}


if __name__ == "__main__":
    uvicorn.run(app)

```

Run your server, and hit the url: [http://localhost:8823/queue](http://localhost:8823/queue) three quick times:

output:

```console
Starting DB Worker
Queueing a job
Got a job: (size of remaining queue: 0
in a slow task
Queueing a job
Queueing a job
done with slow thing
Got a job: (size of remaining queue: 1
in a slow task
done with slow thing
Got a job: (size of remaining queue: 0
in a slow task
done with slow thing
```