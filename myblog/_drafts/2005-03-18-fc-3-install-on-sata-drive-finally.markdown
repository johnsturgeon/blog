---
title: "FC 3 install on SATA drive - finally"
date: "2005-03-18"
---

I've finally gotten Fedora Core 3 installed on my SATA drive. You may remember that I had some problems getting Fedora Core 3 installers to see my sata drive (bug in sata\_nv). My solution was a bit complex, but it ultimately worked:  

  
2. dropped a small (40Gig) IDE drive in  
    
3. installed FC3 onto it  
    
4. updated (as per [Jarod's Guide](http://wilsonet.com/mythtv/fcmyth.php)) to 2.6.10 which can recognize sata drives  
    
5. partitioned my SATA drive to look like my IDE drive  
    
6. [copied entire drive contents from IDE -> SATA](http://www.storm.ca/~yan/Hard-Disk-Upgrade.html)  
    
7. edited fstab and grub  
    
8. rebooted  
    
9. reordered drives in bios (sata first now)  
    
10. fought my way through some filesystem integrity problems (not too bad..., just let fsck do it's thing)  
    
11. ... and that's it!
