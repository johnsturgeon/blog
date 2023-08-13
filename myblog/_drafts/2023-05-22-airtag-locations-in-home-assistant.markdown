---
title:  "AirTag support in Home Assistant"
date:   2023-05-22 8:07:00 -0800
categories: howto, homeassistant
tags: findmy mac airtag 
description: How to send FindMy data (including airtags, and devices) fleto Home Assistant for 
tracking
toc: true
---
### Summary
I ran across [this question posted](https://www.reddit.
com/r/thingsapp/comments/11gbrhb/i_cant_believe_this_app_doesnt_handle_timezones/)
in the [r/thingsapp](https://www.reddit.com/r/thingsapp/) subreddit.  The crux of the question 
was how to handle the case where you set your reminder for a task in Things 3 in one timezone, 
but need it to be TZ aware in your new Timezone.

### Solution

I've created a shortcut that you can use that will make your reminders TZ aware.

[https://www.icloud.com/shortcuts/ec2fbfaee0ef4d36a604521c3256c412](https://www.icloud.com/shortcuts/ec2fbfaee0ef4d36a604521c3256c412)

Instructions: Run the shortcut whenever you add a reminder to a task (or simply schedule it to run every <n> minutes / hours).  That's it!

What the shortcut does (you don't need to know this):

1. It will find all todos that have 'reminders'
2. For each todo it will:
   1. if it has a checklist item starting with `TZ:` it will grab that value and set the reminder based on the time/timezone in the checklist
   2. if no checklist item exists, it will create one for the next run.


Voila!

How you can test it out -- Let's say you're in the PST timezone:

1. create a todo and add a reminder for.. say.. 6pm
2. Run the shortcut
3. Notice that there is now a 'checklist' item that says: `TZ: 6:00:00 pm PST`
4. Edit the checklist item to say `TZ: 6:00:00 pm EST`
5. Re-Run the shortcut

Notice that now your reminder time changed to Today: 3pm!