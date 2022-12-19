---
title: "My Home Automation Setup"
date: "2019-03-19"
categories: 
  - "home-automation"
tags: 
  - "home-automation"
  - "siri"
---

I've been delaying writing anything about my current home automation setup because I'm never really completely satisfied with it. Well, that's been the case since I started to dabble almost two decades ago. With that out, I'll use this post to just give an overview, and possible dive deeper into individual components at another time.

![](images/Insteon-Logo-Blue-1024x107.png)

Starting with Insteon, most of my frequently used switches are Insteon. The reliability has been solid, and from what I've heard/read, smart switches are a mixed bag whichever technology you choose. The biggest complaint that I have is that they are quite large and really fill an electrical box, so installation/repair can be a pain. They integrate with openHAB through the [Insteon PLM](https://www.openhab.org/addons/bindings/insteonplm1/) (USB)

Other devices each have their own integrations with openHAB (Harmony, Tesla, MyQ Garage Doors, etc...) and all the bindings actually work quite well.

![](images/openhab-logo-square.png)

OpenHAB: This is the heart of the system. Open Source, and a multitude of well-maintained integrations are key. The idea of using a system like openHAB is that you end up with a single point of access for every possible "smart" thing you have, and might get in the future. There might be times where you get something that doesn't have an integration, but typically, writing your own, or using a shell script integration will do the trick. In that sense, it kind of 'future proofs' your home automation.

![](images/siri.png)

One note about HomeKit. I \*REALLY\* like being able to control my devices with Siri, so the HomeKit integration with openHAB is fantastic, but can be buggy at times. I think at some point there are just too many moving parts to get the whole thing working perfectly, but it does work most of the time, and when it does, it adds the finishing touch and makes all the technology behind it disappear.
