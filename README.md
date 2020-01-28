<div align="middle"><img src="https://preview.redd.it/vkrxx5pzg8541.jpg?width=608&format=pjpg&auto=webp&s=352a35c3c4faab0c6978f4c2a0dd6738a62cbca7"></div>
<br />

This project aims to extend Cozmo's abilities with voice recognition, interactive chatting sessions (served by online AI chatbots) special user commands, pulling useful information from the internet, etc.


## Requirements

1. First of all you need to have Python 3.x and Git installed. Python comes already preinstalled in many Linux distributions but if you are on Windows or MacOS, click <a href="https://www.python.org/downloads/">here</a> to get and install the latest version from the official Python.org website.
To install Git go to the project's <a href="https://git-scm.com/downloads">download webpage</a> and get the latest version for your platform.  

2. Once Python and Git are installed you need to install <b><a href="https://www.mozilla.org/en-US/firefox/new/">Firefox browser</a></b> and <b><a href="https://selenium-python.readthedocs.io/installation.html">Selenium webdriver</a></b>. 
You can find detailed installation notes on the links.

3. Selenium also requires geckodriver to interface with the headless browser. 
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

4. Install all the necessary Python libraries.
- On <b>Windows</b> start a command prompt using the "cmd.exe" program, go to Python's pip.exe location (eg C:\Python35\Scripts\) and run:
```
pip.exe install -U selenium pillow termcolor cozmo requests SpeechRecognition PyAudio
```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
pip3 install selenium pillow termcolor cozmo requests SpeechRecognition PyAudio
```


## Installation 

After all the requirements are met you can install Cozmo.AI as follows:<br />
- On <b>Windows</b> start a command prompt using the "cmd.exe" program and type:
```
cd 
git.exe clone https://github.com/zayfod/pycozmo.git
```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
cd ~/
git clone https://github.com/zayfod/pycozmo.git
```


## Usage 

1. For the very first time only, you will need to enable the connection between your phone and your PC.
There are various guides on the internet depending on your computer OS and phone type (Android/iPhone) but generally the typical process for an Android phone is this:
- Enable USB debugging on your phone (https://gadgetsright.com/enable-usb-debugging-connect-android/)
- Connect your phone to your computer using a USB cable. 
- Tap the USB option from the Notification Panel on your phone and then select MTP mode and let the computer finish installing the various necessary drivers.

2. With your phone connected via USB to your computer, connect your Cozmo robot to your smartphone/tablet via wifi and run Cozmo's app. 

3. After Cozmo wakes up go to the app's settings and enable SDK mode. Now the phone whould display a black text screen and Cozmo should stop moving around. The robot is now ready to execute our Python program.

4. Run the CozmoAI program as follows:<br />
- On <b>Windows</b> start a command prompt using the "cmd.exe" program and type:
```

```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
cd ~/Cozmo.AI
python3 main.py
```

