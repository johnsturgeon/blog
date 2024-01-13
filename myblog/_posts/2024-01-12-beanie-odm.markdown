---
title:  "Using Beanie ODM"
date:   2024-01-12 2:15:00  -0800
categories: python, tgfp
tags: tgfp python mongodb
description: I'm going to use Beanie ODM instead of home-grown ODM for the new TGFP
toc: true
header:
  og_image: /assets/images/beanie_odm.png
---

# Summary

Update time!  I'm working on this tasks to get things started:

GitHub: [Migrate models from homegrown PyMongo to Beanie](https://github.com/TheGreatFootballPool/tgfp-lib/issues/26)


I want to move from Flask to [FastAPI](https://fastapi.tiangolo.com/){:target="_blank"},
and on a few past projects, I've enjoyed FastAPI's native
integration with Pydantic models.  Since I use MongoDB on the backend, I've also used 
[Beanie ODM](https://github.com/roman-right/beanie){:target="_blank"}
for persisting my models to my DB.

As I move forward with this project I definitely want to have Administrator CRUD capabilities for
user management.

As of now, I've rolled my own ODM and while that will work for what it has been used for, as I 
move to a more robust system, using something async like Beanie will definitely help.

## Captains Log
#### 2024-01-12
I needed to re-acquaint myself with Beanie ODM, so I spent the better part of the morning reading
through an old project of mine, and the Beanie Docs (to see if anything has changed).

**Problem 1**: It seems that I forgot how Beanie structures linked documents, and since my homegrown solution
won't map directly to the same document style, I am going to need to migrate my 'old' data.

This might end up taking a bit of time to figure out all the bits and pieces of my old DB Schema
that need to migrate and work through it.

OK, I'm done for the day -- tomorrow will be writing migration scripts and testing them out on 
my development db.

#### 2024-01-13

I have 6 models that need to be migrated, and today is the first day of the NFL Playoffs for the 2023 season
so... I'm not sure how much I'll get done.  I'll start with the 'TGFPPick' model.

Tomorrow's post will elaborate on what it takes to do a migration from a manual ODM to a proper
Beanie ODM (Pydantic) model.
