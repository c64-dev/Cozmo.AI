<div align="middle"><img src="https://preview.redd.it/vkrxx5pzg8541.jpg?width=608&format=pjpg&auto=webp&s=352a35c3c4faab0c6978f4c2a0dd6738a62cbca7"></div>
<br />

This project aims to extend Cozmo's abilities with voice recognition, interactive chatting sessions (served by online AI chatbots) special user commands, pulling useful information from the internet, etc.

 
## Requirements

1. If not already installed, download and install the following:
- <a href="https://www.python.org/downloads/">Python 3.x</a>
- <a href="https://git-scm.com/downloads">Git</a>
- <a href="https://www.mozilla.org/en-US/firefox/new/">Firefox</a>

2. Download <a href="https://github.com/mozilla/geckodriver/releases/latest">geckodriver</a> and install according to your OS.
- On Windows, copy the .exe to a folder (eg C:\bin\gecko) and open a command prompt to declare it in your PATH:<br />
```
$ set PATH=%PATH%;C:\bin\gecko
```

- On Linux and MacOS extract the file to your home folder, open a Terminal prompt and run:
```
mkdir ~/.local/bin
cp ~/geckodriver ~/.local/bin/
export PATH=$PATH:~/.local/bin/
```

3. Install all the necessary Python libraries. 
- On <b>Windows</b> start a command prompt, go to Python's pip.exe location (eg C:\Python35\Scripts\) and run:
```
pip.exe install -U selenium pillow termcolor cozmo requests SpeechRecognition selenium feedparser beautifulsoup4 unidecode
```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
pip3 install selenium pillow termcolor cozmo requests SpeechRecognition selenium feedparser beautifulsoup4 unidecode
```


## Installation 

After all the requirements are met you can install Cozmo.AI as follows:<br />
- On <b>Windows</b> start a command prompt using the "cmd.exe" program and type:
```
set PATH=%PATH%;C:\Program Files\Git\cmd
cd %HOME%
git.exe clone https://github.com/c64-dev/Cozmo.AI.git
```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
cd ~/
git clone https://github.com/c64-dev/Cozmo.AI.git
```


## Usage 

1. For the very first time only, you will need to enable the connection between your phone and your PC.
There are various guides on the internet depending on your computer OS and phone type (Android/iPhone) but generally the typical process for an Android phone is this:
- Enable USB debugging on your phone (https://gadgetsright.com/enable-usb-debugging-connect-android/)
- Connect your phone to your computer using a USB cable. 
- Tap the USB option from the Notification Panel on your phone and then select MTP mode and let the computer finish installing the various necessary drivers.

2. With your phone connected via USB to your computer, connect your Cozmo robot to your smartphone/tablet via wifi and run Cozmo's app. 

3. After Cozmo wakes up go to the app's settings and enable SDK mode. Now the phone should display a black text screen and Cozmo should stop moving around. The robot is now ready to execute our Python program.

4. Run the CozmoAI program as follows:<br />
- On <b>Windows</b> start a command prompt, go to Python's python.exe location (eg C:\Python35\) and run:
```
python.exe %HOME%\Cozmo.AI\main.py
```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
python3 ~/Cozmo.AI/main.py
```

## Updating 

To update to the latest version of CozmoAI simply run the following commands:
- On <b>Windows</b> start a command prompt and type:
```
cd %HOME%\Cozmo.AI
git.exe pull https://github.com/c64-dev/Cozmo.AI.git
```

- On <b>MacOS</b> and <b>Linux</b> start a Terminal and run:
```
cd ~/Cozmo.AI/
git pull https://github.com/c64-dev/Cozmo.AI.git
```
