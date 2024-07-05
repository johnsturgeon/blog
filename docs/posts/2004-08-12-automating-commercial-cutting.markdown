---
authors:
  - johnsturgeon
categories:
  - HDTV
date:
  created: 2004-08-12
description: DIY comskip :)
tags:
  - hdtv
  - mythtv
---

# Automating commercial cutting

One of the nice features of mythtv is that it can do commercial detection, and from that, build a _cutlist_. My biggest problem, and what kept me from using this feature was that I thought you had to use the user interface to do this. Alas, I have found that indeed there is a command line way to generate the cutlist. Using `mythcommflag -f <filename>` you can create the commercial flags, the coming back and using `mythcommflag --blanks -f` give me the cutlist.  
<!-- more -->


```
Breaks (computed using only blank frame detection)
  
 13090 : 4 (00:07:16.10) (436)
  
 18678 : 5 (00:10:22.18) (622)
  
 35104 : 4 (00:19:30.04) (1170)
  
 41431 : 5 (00:23:01.01) (1381)
  
 51877 : 4 (00:28:49.07) (1729)
  
 52374 : 5 (00:29:05.24) (1745)
  
 53651 : 4 (00:29:48.11) (1788)
  
 65357 : 5 (00:36:18.17) (2178)
  
 78320 : 4 (00:43:30.20) (2610)
  
 85881 : 5 (00:47:42.21) (2862)
  
100991 : 4 (00:56:06.11) (3366)
  
107762 : 5 (00:59:52.02) (3592)
```

  
The first column is the frame number (useful for [avidemux](https://avidemux.sourceforge.net){:target="_blank"}), the second column is the `4:cut out` `5:cut in` column, the third column is the timecode (useful for ProjectX) and the fourth column is seconds (useful for mplayer).  

  
Some simple perl scripting, and we have a cutlist that can be used for avidemux, or as an EDL (edit decision list) for [mplayer](https://mplayerhq.hu/design7/news.html){:target="_blank"}.
