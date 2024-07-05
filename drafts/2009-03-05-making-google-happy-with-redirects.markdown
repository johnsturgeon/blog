---
title: "Making google happy with redirects"
date: "2009-03-05"
---

I've been moving my blogs around a bit the last couple days, and the thought occured to me that I have years of posts that are still generating pretty significant traffic to my blog. How can I update the 'old' urls so that they 1) redirect the person who runs across an old link and 2) tell google to update my link in their search results and keep my rank.  
  
Here you go:  
`  
<?php  
  
header("HTTP/1.1 301 Moved Permanently");  
header("Location: http://blog.myhdbox.com/newpage/newurl.htm");  
exit();  
  
?>  
`  
That little dandy replaces every page that I want re-directed. Now... wouldn't it be nice to write a little ruby script to go through my 100 posts and update each one!
