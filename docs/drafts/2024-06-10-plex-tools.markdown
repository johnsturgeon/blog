---
authors:
  - johnsturgeon
categories:
  - Plex
  - Tools
date:
  created: 2024-06-10
description: Introduction Plex Song De-Dupe tool
draft: true
tags:
  - plex
  - plexamp
  - python
---

# Plex Tools (python plex api)

I've been migrating my Plex server to a new server and have found a ton of problems with my Plex Music Library, so I thought I'd write some tools to help me clean it up.

# Introducing GoshDarned Plex Tools

<img width="300" src="https://github.com/johnsturgeon/plex-tools/assets/9746310/0c42ce63-983b-43a6-8f2e-77338e204cba">

## Tool 1: Song De-Dupe tool

The first problem I had was a ton of songs that for one reason or another I had *exact* duplicate copies of in my library, so I wrote a tool to 'de-duplicate' the songs.

[Read about it on GitHub here](https://github.com/johnsturgeon/plex-tools){:target="_blank"}

## What's next?

### Song Metadata Mismatch fixer

I also notice that sometimes the song that's played is NOT the same as the one Plex matched it to.

My next project will be a *'song metadata mismatch finder'* (name pending... lol)  I'm going to use the Shazam API to find a match for my songs, then compare the metadata to what is in plex.  I'm sure I'll find quite a few mis-matches.

> **_NOTE:_** Please let me know if you have any issues, or what you might want to see for tools next by filing a GitHub Issue.