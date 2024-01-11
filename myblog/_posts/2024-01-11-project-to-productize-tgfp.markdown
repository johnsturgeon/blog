---
title:  "Making The Great Football Pool a turnkey product"
date:   2024-01-11 00:10:00 -0800
categories: python, homelab, football, nfl
tags: tgfp python
description: Documenting my journey to productize my long time personal project the TGFP
toc: true
---
## Summary
I have been running a simple online "Pick 'em" style football pool for decades -- since 1995 -- and
it's been a source of enjoyment for my friends and family every year.  I thought it would be fun to
make the project a 'white box' or 'turnkey' solution for other people who want to run their own
friends and family football pool.

## Quick technical overview

It started out as CGI scripts and html forms where the data was saved in csv flat files.  Over the
years, I've migrated the technology from CGI to PHP to Ruby on Rails and finally to Flask / MongoDB.

The scores / odds / etc.. are fed via an undocumented API from ESPN.

All my code is open-sourced and available on [GitHub](https://github.com/TheGreatFootballPool){:target="_blank"}

Authentication is done through [Discord oath2](https://discord.com/developers/docs/topics/oauth2){:target="_blank"}.

I use [Listmonk](https://listmonk.app/){:target="_blank"} for my email distribution list.

I use [Prefect](https://www.prefect.io/){:target="_blank"} to host my 'secrets' and automate the workers.

Everything is in Docker containers and hosted in my homelab

## The football pool itself

The concept of the pool is incredibly simple.  Each week I post the entire NFL schedule of games and
each player in the pool goes through and picks their 'winner'.  There are ways to get bonus points
for upsets and 'locks'.

Here are the rules: [https://tgfp.us/rules](https://tgfp.us/rules){:target="_blank"}

And yes, I know it's not a 'pool' :)

## Goals of this project

I have a couple goals.  First, I want to be able to allow anybody to host their own football
pool, and have it be as 'turnkey' as possible.  Secondly, I want to make it even simpler by
providing the hosting of the football pool.

## Challenges

The main challenges I see at this point to achieving my goals are:

1. Creating a front end for the administration of the pool.  Administration tasks include:
   1. User management
   2. Job monitoring / recovery
2. Automate some of the tasks that are currently manually done by ME :)
3. Scaling and Robustness of the final product

## Conclusion

Stay tuned for updates as I go through the process, and if you have any thoughts or questions feel
free to connect with me on mastodon [https://pdx.social/@johnsturgeon](https://pdx.social/@johnsturgeon){:target="_blank"}, or create issues on github! 



