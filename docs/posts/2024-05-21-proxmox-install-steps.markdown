---
authors:
  - johnsturgeon
categories:
  - Howto
  - Proxmox
date:
  created: 2024-05-21
description: How to install Proxmox VE on to a Dell R430 Poweredge
tags:
  - proxmox
  - homelab
  - linux
slug: proxmox-install-steps
comments: true
---

# Proxmox VE Install on Dell R430
I recently purchased a very used Dell R430 for use in my Homelab.  The idea is to migrate the apps that I have running on various bits of hardware all over the place to one large server.  It has 2x Xeon processors w/12 cores each and 128GB of RAM, so it should do nicely.  Below I'll document each step through the process, for myself, as well as for anybody else who might come along.  I'll do my best to keep it updated.

<!-- more -->

# Install Proxmox

Proxmox is an excellent hypervisor which will allow me to run any VM or LXC (Linux Container) that I need to.

* Download Proxmox VE ISO
* Burn ISO to thumb drive (I used Balena etcher)
* Plug USB into front panel Dell R430
* Start up
* F11 to select "One shot boot front USB"
* Install (I chose to format ext4, if you choose zfs that will affect your boot config later)

#  Clover Bootloader (for NVMe)

Somebody on the Proxmox Forum wrote an excellent overview of preparing the clover bootloader.[^1]

  * Follow those^^ instructions for creating and using your CLOVER boot USB.
  * Then come back here.. you can see my notes below as I followed the process

> NOTE: Here are my notes from following the steps.. and how I gathered the information for creating the config.plist file

```bash
# get your EFI dev file
$ fdisk -l | grep EFI
/dev/nvme0n1p2    2048    2099199    2097152    1G EFI System # This one!!!
/dev/sde1      40   409639   409600  200M EFI System

# get your PARTUUID
$ blkid | grep nvme0n1p2
/dev/nvme0n1p2: UUID="B41F-1C61" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="0d05f343-cc10-414b-ba80-7d8ce4904353"

# get your bootloader (mine is 'proxmox grub')
$ mkdir /drive
$ mount /dev/nvme0n1p2 /drive
$ find /drive -iname "*.efi"
/drive/EFI/proxmox/shimx64.efi
/drive/EFI/proxmox/grubx64.efi # This one for me
/drive/EFI/proxmox/mmx64.efi
/drive/EFI/proxmox/fbx64.efi
/drive/EFI/BOOT/fbx64.efi
/drive/EFI/BOOT/grubx64.efi
/drive/EFI/BOOT/mmx64.efi
/drive/EFI/BOOT/BOOTx64.efi
```

## Update the config.plist file
* Shut down your server
* Pull your Clover USB thumb drive
* Re-mount it on your Mac/PC and add the `config.plist` file to your USB EFI/CLOVER directory (below)


Use the PARTUUID and the EFI PATH to the bootloader and update the `config.plist` below with your values

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Boot</key>
  <dict>
    <key>Timeout</key>
    <integer>5</integer>
    <key>DefaultVolume</key>
    <string>LastBootedVolume</string>
  </dict>
  <key>GUI</key>
  <dict>
    <key>Custom</key>
    <dict>
      <key>Entries</key>
      <array>
        <dict>
          <key>Path</key>
          <string>\EFI\proxmox\grubx64.efi</string>
          <key>Title</key>
          <string>Arch Linux</string>
          <key>Type</key>
          <string>Linux</string>
          <key>Volume</key>
          <string>D124B653-7947-4049-A2D8-50875F58BEFE</string>
          <key>VolumeType</key>
          <string>Internal</string>
        </dict>
      </array>
    </dict>
  </dict>
</dict>
</plist>
```

* re-insert the USB drive and boot up the server 

!!! warning

    The first time you boot back up you will need to hit 'enter' on the clover boot screen so that it will remember to boot to that option the next time

If you want to confirm that your boot will be clean, go ahead and reboot now, and observe your restart process

!!! tip

    As a final 'cleanup' step prior to doing all of your Proxmox "First Time Install" things, I would recommend using the wonderful [proxmox VE Helper-Scripts - Scripts for Streamlining Your Homelab with Proxmox VE](https://helper-scripts.com/scripts?id=Proxmox+VE+Post+Install){:target="_blank"} script

    ```bash
    bash -c "$(wget -qLO - https://github.com/tteck/Proxmox/raw/main/misc/post-pve-install.sh)"
    ```

[^1]: [Tutorial- bootable NVME install on old hardware made easy with pcie adapter and clover - Proxmox Support Forum](https://forum.proxmox.com/threads/bootable-nvme-install-on-old-hardware-made-easy-with-pcie-adapter-and-clover.78120/){:target="_blank"}
