#Intro To Raspberry Pi: DIY Home Security System
This repository demonstrates how to stream live video to Youtube from a Raspberry Pi. Slides used from the class are here:
https://docs.google.com/presentation/d/1jFV8XzrUoVljoIxuk7CGZpTRrUEx1HQH5a4gPmkIESA/pub?start=false&loop=false&delayms=3000

#Installation

**SSH Into Pi**
<pre>
ssh pi@192.168.1.yourIP
</pre>

**Enable Camera And Expand Filesystem**
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
git clone https://github.com/devonmurphy/PIHomeSecurity
cd PIHomeSecurity/
</pre>

**Add Your Gmail Username and Password To start-server.py**
<pre>
nano start-server.py
</pre>

**Install**
<pre>
./install
</pre>
