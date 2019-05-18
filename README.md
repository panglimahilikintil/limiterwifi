# limiterwifi
limiterwifi untuk meremot sebuah wifi
<p align="center"><img src="https://i.imgur.com/CBGh0Yx.png" /></p>

[![License Badge](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Compatibility](https://img.shields.io/badge/python-3-brightgreen.svg)](PROJECT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![HitCount](http://hits.dwyl.io/bitbrute/evillimiter.svg)](http://hits.dwyl.io/bitbrute/evillimiter)
[![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

A tool to limit the bandwidth (upload/download) of devices connected to your network without physical or administrative access.<br>
```limiterwifi``` employs [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing) and [traffic shaping](https://en.wikipedia.org/wiki/Traffic_shaping) to throttle the bandwidth of hosts on the network. This is explained in detail below.

## Requirements
- Linux distribution
- Python 3 or greater

Possibly missing python packages will be installed during the installation process.

## Installation

```bash
git clone https://github.com/panglimahilikintil/limiterwifi.git
cd limiterwfi
sudo python3 setup.py install
```

Alternatively, you can download a desired version from the [Release page](https://github.com/panglimahilikintil/limiterwifi/releases).<br>

## Usage

Type ```limiterwifi``` or ```python3 bin/limiterwifi``` to run the tool.

```limiterwifi``` will try to resolve required information (network interface, netmask, gateway address, ...) on its own, automatically.

#### Command-Line Arguments

| Argument | Explanation |
| -------- | ----------- |
| ```-h``` | Displays help message listing all command-line arguments |
| ```-i [Interface Name]``` | Specifies network interface (resolved if not specified)|
| ```-g [Gateway Address]``` | Specifies gateway IP address (resolved if not specified)|
| ```-n [Netmask Address]``` | Specifies netmask (resolved if not specified)|
| ```-f``` | Flushes current iptables and tc configuration. Ensures that packets are dealt with correctly.|
| ```--colorless``` | Disables colored output |

#### ```limiterwifi``` Commands

| Command | Explanation |
| ------- | ----------- |
| ```scan``` | Scans your network for online hosts. One of the first things to do after start.
| ```hosts``` | Displays all the hosts/devices previously scanned and basic information. Shows ID for each host that is required for interaction.
| ```limit [ID1,ID2,...] [Rate]``` | Limits bandwidth of host(s) associated to specified ID. Rate determines the internet speed.<br>Valid rates: ```bit```, ```kbit```, ```mbit```, ```gbit```, ```tbit```<br>For example: ```limit 4,5,6 200kbit``` or ```limit all 1gbit```
| ```block [ID1,ID2,...]``` | Blocks internet connection of host(s) associated to specified ID.
| ```free [ID1,ID2,...]``` | Unlimits/Unblocks host(s) associated to specified ID. Removes all further restrictions.
| ```add [IP] (--mac [MAC])``` | Adds custom host to host list. MAC-Address will be resolved automatically or can be specified manually.<br>For example: ```add 192.168.178.24``` or ```add 192.168.1.50 --mac 1c:fc:bc:2d:a6:37```
| ```clear``` | Clears the terminal window.
| ```?```, ```help``` | Displays command information similar to this one.

## Restrictions

- **Limits IPv4 connctions only**, since [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing) requires the ARP packet that is only present  on IPv4 networks.

## Disclaimer
[Limiter Wifi](https://github.com/panglimahilikintil/limiterwifi) is provided by [panglimahilikintil](https://github.com/panglimahilikintil) "as is" and "with all faults". The provider makes no representations or warranties of any kind concerning the safety, suitability, lack of viruses, inaccuracies, typographical errors, or other harmful components of this software. There are inherent dangers in the use of any software, and you are solely responsible for determining whether Evil Limiter is compatible with your equipment and other software installed on your equipment. You are also solely responsible for the protection of your equipment and backup of your data, and the provider will not be liable for any damages you may suffer in connection with using, modifying, or distributing this software. 

## License

Copyright (c) 2019 by [panglimahilikintil](https://github.com/panglimahilikintil). Some rights reserved.<br>
[Limiter Wifi](https://github.com/panglimahilikintil/limiterwifi) is licensed under the MIT License as stated in the [LICENSE file](LICENSE).