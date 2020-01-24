<div align="middle"><img src="https://preview.redd.it/vkrxx5pzg8541.jpg?width=608&format=pjpg&auto=webp&s=352a35c3c4faab0c6978f4c2a0dd6738a62cbca7"></div>
<br />

This project aims to extend Cozmo's abilities with voice recognition, interactive chatting sessions (served by online AI chatbots) special user commands, pulling useful information from the internet, etc.


## Installation
<b>Requirements</b>

1. First of all you need to have Python 3.x and pip3 installed. Python comes already preinstalled in many Linux distributions but if you are on Windows or MacOS, click <a href="https://www.python.org/downloads/">here</a> to get and install the latest version from the official Python.org website.

2. Once Python is installed you need to install <b><a href="https://www.mozilla.org/en-US/firefox/new/">Firefox browser</a></b> and <b><a href="https://selenium-python.readthedocs.io/installation.html">Selenium webdriver</a></b>. 
You can find detailed installation notes on the links.

3. Now you can install Cozmo.AI by issuing a simple command prompt line.<br />
- On <b>Windows</b> start a command prompt using the "cmd.exe" program, go to Python's pip.exe location (eg C:\Python35\Scripts\) and run:
```
pip.exe install -U CozmoAI
```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
pip3 install CozmoAI
```

<b>Drivers</b>

Selenium also requires geckodriver to interface with the headless browser, which needs to be installed before using this module. <br />

Download the latest geckodriver at https://github.com/mozilla/geckodriver/releases and then install according to your OS.
- On Windows, copy the .exe to a folder (eg C:\bin\gecko) and open a command prompt to declare it in your PATH:<br />
```
$ set PATH=%PATH%;C:\bin\gecko
```
- On Linux and MacOS extract the file to your home folder, open a Terminal prompt and run:
```
sudo cp geckodriver /usr/bin
export PATH=$PATH:/usr/bin
```
