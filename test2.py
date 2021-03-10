import speech_recognition as sr
import time
import datetime
import sys
import os
import config

from requests import get
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import cprint

name = ["Cozmo", "Cosmo", "cosmo", "cozmo", "osmo", "Kuzma", "kuzma", "Prisma", "Goodwill", "Robert", "robot",
        "Christmas", "customer", "cuz my", "cuz", "Kosmos", "kiasma", "Kismet", "Kokomo"]
cmd_freeplay = ["freeplay", "free play", "FreePlay"]  # OK

def initCozmo():
    
    _ = os.system('cls' if os.name == 'nt' else 'clear')
    cprint("Initializing system...", "yellow")
    wake_up()
    freeplay()
    mainLoop()
    

# Main Program Loop
def mainLoop():
    global humanString, cozmoString

    # Set variables and connect to AI bot
    humanString = None
    cozmoString = None
    pb = AIBot()

    try:
        # Connect to Chatbot
        pb.browser.get(pb.url)
        print("Cozmo says: Yes user?")
    except:
        pb.browser.close()
        # TODO: Have a more elegant exit to the program.
        sys.exit(0)

    while True:
        # In a loop, listen to user
        try:
            pb.get_form()
        except:
            sys.exit(0)

        listen_robot()
        humanString = listen_robot.parsedText


        # Here we look for our special commands (quit, time, weather, movements etc).
        # If none are found we move forward with the chatbot and listen again in a loop.
        check_freeplay()

        # Else, we log what the human said (optional).
        # addEntry(log, "Human says: " + humanString)
        print("Human says: " + humanString)

        # Send user query
        pb.send_input(humanString)

        # Get bot's response
        cozmoString = pb.get_response()
        print("Cozmo says: " + cozmoString)
        

def check_freeplay():
    global humanString
    activate = set(name).intersection(humanString.split())
    command = set(cmd_freeplay).intersection(humanString.split())
    if activate and command:
        print("Human says: " + humanString)
        # addEntry(log, "Human says: " + humanString)
        freeplay()
        listen_robot()
        humanString = listen_robot.parsedText
    else:
        return



def wake_up():
    global user_name
    t = (datetime.datetime.now().strftime("%H"))

    if t >= "20":
        greet = "Good evening "
    elif t >= "16":
        greet = "Good afternoon "
    elif t >= "12":
        greet = "Good day "
    else:
        greet = "Good morning "
        
    ask_name()
    user_name = ask_name.parsedText
    print("Cozmo says: " + greet + user_name + ". Entering FreePlay mode.")
        

def ask_name():
    rec = sr.Recognizer()
    microphone = sr.Microphone()
    cprint("\nWhat's your name please?", "white", attrs=['bold'])

    with microphone as source:
        rec.pause_threshold = 0.6
        rec.energy_threshold = 4000
        rec.dynamic_energy_threshold = True  # was True
        rec.adjust_for_ambient_noise(source, duration=1)

        try:
            cprint("Listening...", "white", attrs=['bold'])
            voice = rec.listen(source, timeout=5)  # Recording audio
            cprint("Recognized.", "green")
            ask_name.parsedText = rec.recognize_google(voice)  # Recognizing audio
        except sr.WaitTimeoutError:
            cprint("Retrying...", "yellow")
            ask_name()
        except sr.UnknownValueError:
            cprint("Retrying...", "yellow")
            ask_name()
        except sr.RequestError as e:
            cprint("Could not request results from Speech Recognition service; {0}".format(e), "red")
            sys.exit(0)



def listen_robot():
    rec = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        rec.pause_threshold = 0.6
        rec.energy_threshold = 4000
        rec.dynamic_energy_threshold = True  # was True
        rec.adjust_for_ambient_noise(source, duration=1)

        try:
            cprint("Listening...", "white", attrs=['bold'])
            voice = rec.listen(source, timeout=10)  # Recording audio
            cprint("Done Listening: recognizing...", "green")
            listen_robot.parsedText = rec.recognize_google(voice)  # Recognizing audio
        except sr.WaitTimeoutError:
            cprint("Timeout...", "red")
            listen_robot.parsedText = " "
        except sr.UnknownValueError:
            cprint("Could not understand audio. Retrying...", "yellow")
            listen_robot()
        except sr.RequestError as e:
            cprint("Could not request results from Speech Recognition service; {0}".format(e), "red")
            sys.exit(0)



def freeplay():
    rec = sr.Recognizer()
    microphone = sr.Microphone()

    print()
    cprint("==========================", "green", attrs=['bold'])
    cprint("= Entering FreePlay Mode =", "green", attrs=['bold'])
    cprint("==========================", "green", attrs=['bold'])
    print()
    cprint("Cozmo is now in full autonomous mode. \n"
           "He will freely explore his environment until he hears the wakeup command ", "green", end=''), \
    cprint("'Cozmo listen'", "cyan", attrs=['bold'])

    while True:
        time.sleep(config.interval)

        with microphone as source:
            rec.pause_threshold = 0.6
            rec.energy_threshold = 4000
            rec.dynamic_energy_threshold = True  # was True
            rec.adjust_for_ambient_noise(source, duration=1)

            try:
                cprint("Listening for wakeup command now.", "cyan")
                voice = rec.listen(source, timeout=5)
                p = rec.recognize_google(voice)  # Recognizing audio

                if p == "Cosmo" or p == "hey Cosmo listen" or p == "Cosmo listen" or p == "cosmopolitan" \
                        or p == "hey cosmopolitan" or p == "hey Cosmo Nissan":
                    cprint("Found. Exiting FreePlay mode. Please wait...", "green")
                    return
                else:
                    continue

            except sr.WaitTimeoutError:
                cprint("Timeout. Checking again in ", "red", end=''), \
                cprint(str(config.interval), "red", attrs=['bold'], end=''), cprint(" seconds.", "red")
                continue
            except sr.UnknownValueError:
                cprint("Not found. Checking again in ", "yellow", end=''), \
                cprint(str(config.interval), "yellow", attrs=['bold'], end=''), cprint(" seconds.", "yellow")
                continue


class AIBot:

    def __init__(self):

        # Initialize selenium options 
        self.opts = Options()
        self.opts.add_argument("--headless")
        self.browser = webdriver.Firefox(options=self.opts)
        self.url = "http://demo.vhost.pandorabots.com/pandora/talk?botid=b0dafd24ee35a477"
        self.searchEngine = "https://start.duckduckgo.com"

    def get_form(self):

        # Find the form tag to enter your message
        self.browser.implicitly_wait(10.0)
        self.elem = self.browser.find_element_by_name('input')

    def send_input(self, userInput):

        # Submits your message
        fOne = '<\/?[a-z]+>|<DOCTYPE'
        fTwo = '/<[^>]+>/g'
        while True:
            try:
                self.elem.send_keys(userInput + Keys.RETURN)
            except BrokenPipeError:
                continue
            break

    def get_response(self):
        response = None
        try:
            WebDriverWait(self.browser, 30).until(readystate_complete)
        except WebDriverException:
            pass

        # Retrieves response message
        while True:
            try:
                jFetch = get("http://code.jquery.com/jquery-2.1.1.min.js").content.decode('utf8')
                self.browser.execute_script(jFetch)
                data = self.browser.execute_script("""
                  try {
                  main_str = $;
                  var main_str = $('font:has(b:contains("Chomsky:"))').contents().has( "br" ).last().text().trim();
                  main_str = main_str.replace(/Chomsky:/gi,'').replace(/Chomsky/gi,'Cozmo')
                  .replace(/Wikipedia is a great online encyclopedia./gi, 'Wikipedia is your friend. Use it.')
                  .replace(/click here./gi, 'use a computer browser.')
                  .replace(/^\\s*[\\r\\n]/gm, '');
                  return main_str;
                  }
                  catch(error) {
                  return main_str;
                  }
                """)
                response = (data[:254] + '') if len(data) > 254 else data
                self.browser.quit()
            except BrokenPipeError:
                AIBot().get_response()
                self.browser.quit()
            return response



# ENTRY POINT #
if __name__ == "__main__":
    initCozmo()
