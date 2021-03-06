**Intro To Raspberry Pi: DIY Home Security System**

This repository demonstrates how to setup a live stream to a web interface from a Raspberry Pi. Slides used from the class are here:

[Class Slides](https://docs.google.com/presentation/d/1jFV8XzrUoVljoIxuk7CGZpTRrUEx1HQH5a4gPmkIESA/pub?start=false&loop=false&delayms=3000)

**Installation**
**Enable Camera and SSH**
<pre>
raspi-config
</pre>
**SSH Into Pi**
<pre>
ssh pi@192.168.1.yourIP
</pre>

**Enable Pi Camera**
<pre>
sudo raspi-config
</pre>

**Get git**
<pre>
sudo apt-get update
sudo apt-get install git
</pre>

**Clone git Repo**
<pre>
cd ~/
git clone https://github.com/devonmurphy/homesecurity
cd homesecurity/
</pre>

**Install**
<pre>
./install
</pre>

**Add Your Gmail Username and Password To configuration.ini**

If you want to receive an email of your PI's ngrok public url, add your gmail account info to this file.
<pre>
nano configuration.ini
</pre>

**Enable Less Secure Apps In Gmail**

In order for start-server.py to send you an email, you need to enable less secure apps in gmail. Go here:

[https://www.google.com/settings/security/lesssecureapps](https://www.google.com/settings/security/lesssecureapps)

