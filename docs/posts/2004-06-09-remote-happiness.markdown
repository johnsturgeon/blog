---
authors:
  - johnsturgeon
categories:
  - HDTV
date:
  created: 2004-06-09
description: Universal remote control of linux HTPC with lirc
tags:
  - hdtv
  - lirc
---

# Remote happiness

I have followed the advice of [Jared Wilson](http://wilsonet.com/mythtv){:target="_blank"} a few months ago and went to Radio Shack and picked up a remote. I got the 15-2117 (with the RF command center). I pretty much followed his directions for setting it up verbatim, but I have always had problems navigating. Sometimes I have to press a button on the remote several times in order to get it to move around the MythTV menus. The latest CVS release (for some reason) really exacerbated the problem. I actually had to revert to my wireless keyboard just to watch a movie.  
<!-- more -->
  
I was convinced that the problem was in my .lircrc file, so after digging a bit, I decided to try and fix it by removing the 'repeat = 4' from all of my entries, so that the default(repeat = 0) would be in effect. If you're interested in just what the 'repeat = n' option is and how it works, check out the [lirc documentation](http://www.lirc.org/html/configure.html#lircrc_format){:target="_blank"}.  

Sure enough, it solved my problem. I'm back to my remote, happy as a clam.
