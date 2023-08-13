---
title:  "HDMI -> Channels DVR"
date:   2023-08-13 13:07:00 -0800
categories: howto, channels, hdtv
tags: channels dvr 
description: How to capture HDMI output of Andoid TV for use in Channels DVR
toc: true
---
## Summary

DVRs have been around for a long time, but unfortunately streaming services have locked us in to 
*their* cloud DVR solutions.  As a long time MythTV then [Channels DVR](https://getchannels.com) 
user I'm excited at the idea of being able to record content from various streaming services 
that I subscribe to.  Primarily YouTube TV. 

## Solution

Thanks to the good folks over in the Channels DVR Community Forum, the solution I'm exploring today
is using Android TV Streaming devices that output HDMI to 
HDMI Capture / Encoding devices that capture then stream them over the network, those 
streams can then be captured in Channels DVR as custom channels.

Thanks go to:
  * [bnhf](https://community.getchannels.com/u/bnhf) (Docker container author / tremendous help)
  * [KompilerDJ](https://community.getchannels.com/u/KompilerDJ) (Forked original solution, provider of many scripts / help)
  * [Aman](https://community.getchannels.com/u/tmm1) (Co-Founder of the Channels project and the one that started this thread)

## Help
* If you need some help, or have corrections / suggestions for the steps below, please contact me
    * [John Sturgeon](https://community.getchannels.com/u/johnofcamas) at Mastodon
* You can also:
    * Post a question in the [HDMI Channels Thread](https://community.getchannels.com/t/hdmi-for-channels/36302)
    * If the thread is closed, or you have a different question, a post to the general [Channels Community](https://community.getchannels.com/) will be answered

## Instructions
### Prerequisites

* [Channels DVR Server](https://getchannels.com)
* HDMI / HDCP capable Video encoder (you can go network, or PC capture)

  I went with this: 
  [URayCoder 4K 4 Channels HDMI IP Video Streaming Encoder](https://www.amazon.com/URayCoder-Cost-Effective-Streaming-Broadcast-Transmitter/dp/B07TKMPCZH)
* 1 or more Android based video streaming stick / puck.

  I went with this:
  [ONN Android TV 4K UHD Streaming Device](https://www.amazon.com/gp/product/B0B75QMC7X)
* Knowledge of Docker and Machine to host [bnhf/ah4c](https://hub.docker.com/r/bnhf/ah4c) docker 
  container
### Steps
The steps below are going to be for the Network encoder / ONN device that I purchased -- recording YouTube TV, you might have to 
tweak some of these things for your specific configuration.

1. Set up the URay Encoder
   * Plug in the Network Transcoder to Ethernet, and Power and get the IP
   * Ideally set it static in your router -- make a note of your IP
     * Follow the quickstart in the guide for your URayEncoder -- I set mine to use DHCP, then made 
       the IP static in my router
     
2. Set up the Android ONN Device
   * Plug in the ONN device's HDMI to input 1 of the encoder
   * Plug in the power
   * Use VLC to view the stream (instructions for this are in the URay Quick Start guide)
   * Follow the prompts to configure your device (you can go with Wi-Fi, or if you want, you can 
     purchase an Ethernet adapter for the device).
   * Download / install any updates that the device needs now
   * Find your device in your router, and give it a static IP.
   * Finish installing / logging in to any apps you're interested in recording, I'll focus on 
     Youtube TV here
   * [Enable Developer Mode](https://developer.android.com/training/tv/start/start#:~:text=On%20your%20TV%20device%2C%20navigate,Return%20to%20Settings.)
   * Under the (new) developer menu:
     * change all animation durations to 'zero'
     * Enable USB Debugging
     * Toggle 'Stay Awake' to on
   * Under Power and Energy set to **never** Automatically Turn Off

3. Install the docker container

   _I use [Portainer](https://portainer.io), but you can use any method that you're comfortable 
   with for deploying 
   docker stacks_
   * Here is the docker_compose yaml that I used (thanks bnhf):

    ```yaml
    version: '3.9'
    services:
      ah4c:
        image: bnhf/ah4c:latest
        container_name: ah4c
        hostname: ah4c
        dns_search: localdomain # Specify the name of your LAN's domain, usually local or localdomain
        ports:
          - "5037:5037" # Port used by adb-server
          - "7654:7654" # Port used by this ah4c proxy
        environment:
          - IPADDRESS=${IPADDRESS} # Hostname or IP address of this ah4c extension to be used in M3U file (also add port number if not in M3U)
          - NUMBER_TUNERS=${NUMBER_TUNERS} # Number of tuners you'd like defined 1, 2, 3 or 4 supported
          - TUNER1_IP=${TUNER1_IP} # Streaming device #1 with adb port in the form hostname:port or ip:port
          - TUNER2_IP=${TUNER2_IP} # Streaming device #2 with adb port in the form hostname:port or ip:port
          - TUNER3_IP=${TUNER3_IP} # Streaming device #3 with adb port in the form hostname:port or ip:port
          - TUNER4_IP=${TUNER4_IP} # Streaming device #4 with adb port in the form hostname:port or ip:port
          - ENCODER1_URL=${ENCODER1_URL} # Full URL for tuner #1 in the form http://hostname/stream or http://ip/stream
          - ENCODER2_URL=${ENCODER2_URL} # Full URL for tuner #2 in the form http://hostname/stream or http://ip/stream
          - ENCODER3_URL=${ENCODER3_URL} # Full URL for tuner #3 in the form http://hostname/stream or http://ip/stream
          - ENCODER4_URL=${ENCODER4_URL} # Full URL for tuner #4 in the form http://hostname/stream or http://ip/stream
          - STREAMER_APP=${STREAMER_APP} # Streaming device name and streaming app you're using in the form scripts/streamer/app (use lowercase with slashes between as shown)
          - CHANNELSIP=${CHANNELSIP} # Hostname or IP address of the Channels DVR server itself
          #- ALERT_SMTP_SERVER="smtp.gmail.com:587"
          #- ALERT_AUTH_SERVER="smtp.gmail.com"
          #- ALERT_EMAIL_FROM=""
          #- ALERT_EMAIL_PASS=""
          #- ALERT_EMAIL_TO=""
          #- ALERT_WEBHOOK_URL=""
          - TZ=${TZ} # Your local timezone in Linux "tz" format
        volumes:
          - /data/ah4c/scripts:/opt/scripts # pre/stop/bmitune.sh scripts will be stored in this bound host directory under streamer/app
          - /data/ah4c/m3u:/opt/m3u # m3u files will be stored here and hosted at http://<hostname or ip>:7654/m3u for use in Channels DVR - Custom Channels settings
          - /data/ah4c/adb:/root/.android # Persistent data directory for adb keys
        restart: unless-stopped
    ```
   * And for me here are the environment variables:
 
    ```.dotenv
    IPADDRESS=192.168.1.128:7654
    TUNER1_IP=192.168.1.177:5555
    ENCODER1_URL=http://192.168.1.129/0.ts
    CHANNELSIP=192.168.1.170
    TZ=US/Pacific
    NUMBER_TUNERS=1
    STREAMER_APP=scripts/onn/youtubetv
    ```
   * Run the docker container
   * Use VLC to connect to your device's stream, use your remote to accept any prompts on your device.  (mine asked if I wanted to allow USB Debugging Connection, I checked 'Always Allow')
   * Look for any other errors, if you experience any errors that you're not sure how to fix, please post a message in the 
[HDMI Channels](https://community.getchannels.com/t/hdmi-for-channels/36302) thread in the Channels Community.
   * Once you've run the container you can stop it, and edit the files in your /data/ah4c directory

4. Edit the scripts
   * Here are the scripts I had to edit for YouTube TV:
   
   * `./scripts/onn/youtubetv/prebmitune.sh`: 
   ```shell
   IPADD=$1
   IS_ASLEEP=`adb -s $IPADD shell dumpsys display | grep mScreenState=OFF`
   WAKE="input keyevent KEYCODE_WAKEUP"
   HOME="input keyevent KEYCODE_HOME"
   adb connect $IPADD
   
   # YouTube TV sometimes fails to load video if the app is already open when waking up from sleep.
   if [ $IS_ASLEEP ];
   then
   adb -s $IPADD shell $WAKE; sleep 2
   fi
   
   adb -s $IPADD shell $HOME; sleep 2    
   ```
   * `./scripts/onn/youtubetv/bmitune.sh`:
   ```shell
   adb -s $2 shell am start -a android.intent.action.VIEW -d https://tv.youtube.com/watch/$1 -n com.google.android.youtube.tvunplugged/com.google.android.apps.youtube.tvunplugged.activity.MainActivity```
   ```

   * `./scripts/onn/youtubetv/stopbmitune.sh` _No changes_.

5. Add a custom channel to Channels DVR
   * Go to your Channels DVR Settings
   * Add Source
   * Custom Channel
     * Nickname: `YouTube TV` (or whatever you want)
     * Stream Format: `MPEG-TS` (unless you changed it from the defaults with your encoder)
     * Source: `URL` | `http://<ipaddress>:7654/m3u/youtubetv.m3u`
   * Save
6. Go to your guide and check to see if any of the default channels worked.
7. Configuring your YouTube TV Channels!

This was actually the tricky part for me, ymmv

Next blog post will be on getting YouTube TV channel ID's for the m3u!