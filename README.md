<div align="middle">![](https://preview.redd.it/vkrxx5pzg8541.jpg?width=608&format=pjpg&auto=webp&s=352a35c3c4faab0c6978f4c2a0dd6738a62cbca7)</div>

This project aims to extend Cozmo's abilities with voice recognition, interactive chatting sessions (served by online AI chatbots) special user commands, pulling useful information from the internet, etc.

 
## Requirements

1. If not already installed, download and install the following:
- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)

2. Download [geckodriver](https://github.com/mozilla/geckodriver/releases/latest) and install according to your OS.
- On Windows, copy the .exe to a folder (eg C:\bin\gecko) and open a command prompt to declare it in your PATH:
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
- On **Windows** start a command prompt, go to Python's pip.exe location (eg C:\Python35\Scripts\) and run:
```
pip.exe install -U selenium pillow termcolor cozmo requests SpeechRecognition selenium feedparser beautifulsoup4 unidecode pyaudio
```

- On **MacOS/Linux** start a Terminal and run:
```
pip3 install selenium pillow termcolor cozmo requests SpeechRecognition selenium feedparser beautifulsoup4 unidecode pyaudio
```

**For Apple Mac users only:** If you encounter an error trying to install **pyaudio**, then please install 
[Homebrew](http://brew.sh/) and then run the following terminal commands:
```
brew install --build-from-source portaudio
pip3 install pyaudio
```

## Installation 

After all the requirements are met you can install Cozmo.AI as follows:<br />
- **Windows**:
```
set PATH=%PATH%;C:\Program Files\Git\cmd
cd %HOME%
git.exe clone https://github.com/c64-dev/Cozmo.AI.git
```

- **MacOS/Linux**:
```
cd ~/
git clone https://github.com/c64-dev/Cozmo.AI.git
```


## Usage 

1. For the very first time only, you will need to enable the connection between your phone and your PC.
There are various guides on the internet (like [this one](https://www.technorange.com/2015/12/how-to-connect-your-android-device-to-adb-usb-driver-intterface/) depending on your computer OS and phone type but generally the typical process for an Android phone is this:
- Enable [USB debugging](https://gadgetsright.com/enable-usb-debugging-connect-android/) on your phone.
- Get Android ADB & Fastboot drivers either for [Mac/Linux](https://izziswift.com/installing-adb-on-macos/) or [Windows](https://techapple.net/2015/12/easily-install-adb-fastboot-windows-compact-adb-installer/) and install them.
- Connect your phone to your computer using a USB cable. 
- Tap the USB option from the Notification Panel on your phone and make sure that MTP mode and USB Debugging are both enabled.
- In a Terminal/Command prompt run ```adb devices```. It should list your phone as ```unauthorised```.
- Run any push/pull adb command such as ```adb push abc abc``` to prompt your phone to authorize your computer.

2. With your phone connected via USB to your computer, connect your Cozmo robot to your smartphone/tablet via wifi and run Cozmo's app. 

3. After Cozmo wakes up go to the app's settings and enable SDK mode. Now the phone should display a black text screen and Cozmo should stop moving around. The robot is now ready to execute our Python program.

4. Run the CozmoAI program as follows:
- **Windows**:
```
python.exe %HOME%\Cozmo.AI\main.py
```

- **MacOS/Linux**:
```
python3 ~/Cozmo.AI/main.py
```

## Updating 

To update to the latest version of CozmoAI simply run the following commands:
- **Windows**:
```
cd %HOME%\Cozmo.AI
git.exe pull https://github.com/c64-dev/Cozmo.AI.git
```

- **MacOS/Linux**:
```
cd ~/Cozmo.AI/
git pull https://github.com/c64-dev/Cozmo.AI.git
```
