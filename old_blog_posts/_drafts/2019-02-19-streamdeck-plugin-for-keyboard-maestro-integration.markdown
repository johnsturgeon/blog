---
title: "StreamDeck Plugin for Keyboard Maestro integration"
date: "2019-02-19"
categories: 
  - "automation"
tags: 
  - "automation"
  - "keyboard-maestro"
  - "streamdeck"
---

I'm a huge [Keyboard Maestro](https://www.keyboardmaestro.com/main/) fan, and I have been wanting to use the [StreamDeck](https://www.elgato.com/en/gaming/stream-deck) for integration with Keyboard Maestro. Elgato recently released their SDK for StreamDeck which makes this kind of integration possible. I know I can just use 'buttons' straight in KM, but a plugin will provide so much more flexibility.

![](images/streamdeck-300x215.jpg)

StreamDeck from Elgato

I have created a Python plugin that allows you to specify a Keyboard Maestro Macro UUID in the properties inspector, and pressing the button will run the macro.

[https://github.com/johnofcamas/streamdeck\_keyboard\_maestro](https://github.com/johnofcamas/streamdeck_keyboard_maestro)

I have a lot of things on my todo list for this plugin, primarily to allow two-way communication with KM for status, icon updates, etc...

But for now, this is a good starting point.

NOTE: This is NOT a redistributable plugin as it requires a Python installation with specific packages, or a virtual environment. But it's a great start for tinkerers.
