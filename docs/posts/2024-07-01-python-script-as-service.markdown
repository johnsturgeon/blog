---
authors:
  - johnsturgeon
categories:
  - Howto
date:
  created: 2024-07-01T07:00:00
description: Basic instructions for adding your python script to systemd for long
  running processes
tags:
  - python
  - linux
---

# Running a Python Script from systemd

If you have a long-running python script (for example a discord bot) that you want running continuously, this tutorial is for you.
I will show you how to create a long-running python script on any linux machine that supports systemd services.

<!-- more -->
If you don't know what systemd is, [this is a great overview](https://www.linux.com/training-tutorials/understanding-and-using-systemd/){:target="_blank"}

Below, I'll run through a very simple example of script that syncs two folders every 30 seconds

## Python script

Let's go ahead and set up a virtual environment to run our folder syncing script

### Virtual Env and library

Set up the virtual environment and install `dirsync`

```bash
python3 -m venv mcbackup
source mcbackup/bin/activate
cd mcbackup
pip install dirsync
```

### Long running python script

Now, let's write a simple long-running script for syncing our minecraft world for backup purposes

```bash
vi sync-minecraft.py
```

```python
from dirsync import sync
import time


def run():
    while True:
        # Sync our minecraft folder every 30 seconds
        sync('/opt/minecraft/server', '/opt/mccopy', 'sync')
        time.sleep(30)

if __name__ == '__main__':
    run()
```

## Systemd

### Create system service file
```bash
sudo vi /etc/systemd/system/mc-backup.service
```

```ini
[Unit]
Description=Sync Minecraft World
After=multi-user.target

[Service]
WorkingDirectory=/home/<username>/mcbackup
Type=simple
Restart=always
ExecStart=/home/<username>/mcbackup/bin/python /home/<username>/mcbackup/sync-minecraft.py

[Install]
WantedBy=multi-user.target
```

### Load the service

Reload systemd to read the new service file:

```bash
sudo systemctl daemon-reload
```

Enable your new service:

```bash
sudo systemctl enable mc-backup.service
```

Start your new service:

```bash
sudo systemctl start mc-backup.service
```

### Additional info

Now that you have the script running, you have several ways you can control the script using `systemd`

Check the status:

```bash
sudo systemctl status mc-backup.service
```

Stop the script:
```bash
sudo systemctl stop mc-backup.service
```

Reload the script:
```bash
sudo systemctl restart mc-backup.service
```

### Conclusion

There are some other things you'll probably want to do, such as log the output, maybe monitor the status of your script with healthchecks, etc...  I'll cover those in future tutorials.
