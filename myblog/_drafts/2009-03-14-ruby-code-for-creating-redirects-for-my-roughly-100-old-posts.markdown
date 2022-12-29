---
title: "Ruby code for creating redirects for my (roughly) 100 old posts"
date: "2009-03-14"
categories: 
  - "atom"
  - "rss"
  - "ruby"
---

As I mentioned in a [previous post](https://www.myhdbox.com/2009/03/05/making-google-happy-with-redirects/), I moved my blog from my own host, to Google's blogger. As a result, there are ~ 100 old blog posts that are linked to from all over the place and I'd like to have a graceful way to re-direct. The previous post mentioned updated the header with a 301 redirect. Going through so many old posts, and updating each one was nuts, so I wrote a small ruby script to handle the duties.  

  
#!/usr/bin/ruby  
\# update\_redirects.rb  
\# This script will traverse the directory given as the first argument  
\# and replace the contents of all files with the 'redirect\_text'  
#  
\# some special conditions: it assumes that they are php redirects, but you   
\# can use <meta> redirect tags as well for plain HTML  
#  
#  
  
require 'find'  
  
dir = ARGV\[0\]  
redirect\_text ='<?php  
header("HTTP/1.1 301 Moved Permanently");  
header("Location: http://blog.myhdbox.com/%%PATH%%");  
exit();  
?> '  
  
\# find all the files that were published by blogger (they are all in their  
\# respective year directories)  
#  
Find.find(dir) do |path|  
    if path=~/^./200.\*.php$/  
        f=File.open(path,'w') # open 'w' truncates the file  
        new\_text= redirect\_text.gsub("%%PATH%%",path.gsub("./",""))  
        f.write(new\_text)  
        f.close()  
    end  
end
