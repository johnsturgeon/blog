---
title:  "Discord.py bot Uptime with Healthcheck"
date:   2024-07-01 01:00:00 -0800
categories: python, howto
tags: python discord
description: Tutorial for discord.py bot uptime healthcheck using healthcheck.io
toc: true
header:
  og_image: /assets/images/healthchecks.png
---

Sometimes you are running a discord bot using `discord.py` (python library) and it goes offline.  Sure would be nice to know right?

Let's go through some easy steps for adding a background `@task` to your discord.py bot to ping [healthchecks.io](https://healthchecks.io/){:target="_blank"} on a regular interval.

## Prerequisites
* Discord bot created (using `discord.py` library)
* Python 3.10+ 
* virtual env with `requests` library 
* [Healthchecks.io](https://healthchecks.io){:target="_blank"} account


## Set up healthchecks

* Create an account on HealthChecks.io
* Click on 'New Project' (give it a name like "Discord Checks")
* Click 'Add Check'
  * Name: Bot Uptime
  * slug: (use suggested)
  * tags: (leave blank)
  * Schedule: Simple
  * Period: 30 Minutes
  * Grace: 10 Minutes
* Click 'Save'
* Copy the 'ping' url


> *NOTE:* Make sure to set up an 'alert' on Healthchecks.io like discord, or email!

    

## Simple discord bot

This tutorial assumes you know how to create a `discord.py` bot, so I'm not going to go through the steps necessary for creating your bot.  Let's just assume that you already have a bot and it's running.

If you don't know how to create a discord bot, check out the guide: [How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/){:target="_blank"} by RealPython

Below is an extremely simple discord bot (happens to be the example bot from discord.py docs):


```python
# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

BOT_TOKEN='MTI1NzQyNDkyNjY1MDkyOTI1Mg.GIObto.fn85xqqsB7gZdvLRfjmq5fElbuDFX78eJnIXw'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(BOT_TOKEN)

```

Now let's say we want to add a task to ping healthchecks.io every 30 minutes.

First thing we need to do is get the `requests` library

```bash
pip install requests
```

## Add a `@task`

Code below adds the task which pings healthchecks

```python
import discord
from discord.ext import tasks
import requests


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

HEALTHCHECK_URL="https://hc-ping.com/3f0f10e1-b622-40b7-b63d-f4bdbdd6399"
BOT_TOKEN='MTI1NzQyNDkyNjY1MDkyOTI1Mg.GIObto.fn85xqqsB7gZdvLRfjmq5fElbuDFX78eJnIXw'

@tasks.loop(minutes=30)
async def ping_healthchecks():
    try:
        requests.get(HEALTHCHECK_URL, timeout=10)
    except requests.RequestException as e:
        # Log ping failure here...
        print("Ping failed: %s" % e)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Ping once on startup
    await ping_healthchecks()
    ping_healthchecks.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(BOT_TOKEN)
```

That's it, fire up your bot and it should ping your healthcheck right away.

As usual, ping me on mastodon if you have any questions or thoughts.
