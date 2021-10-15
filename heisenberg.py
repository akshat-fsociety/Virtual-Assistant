import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import jokes_feature  # file created by me not a module
import alarm_feature  # file created by me not a module
# import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello and Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Hello and Good Afternoon!")
    else:
        speak("Hello and Good Evening!")
    speak("My name is Heisenberg, I'm your virtual assistant please tell how may I help you?")


def getCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    # r.pyaudio_module = r.get_pyaudio()
    # audio = r.pyaudio_module.PyAudio()
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        speak(f"you said{query}")

    except Exception as e:
        # print(e)
        print("Say that again please, I'm not able to recognize...")
        speak("Say that again please, I'm not able to recognize")
        return "None"
    return query


def alarm_command():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening: ")
        audio = recogniser.listen(source)
        command = ""
        try:
            command = recogniser.recognize_google(audio)
            print(command)
        except Exception:
            print("Sorry didn't get that, could you please repeat?")

        return command


if __name__ == "__main__":
    greetMe()
    while True:
        query = getCommands().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wekipedia")
            print(results)
            speak(results)

        elif 'hello' in query:
            speak("Hello how may I help you")
        elif 'hi' in query:
            speak("Hi how may I help you")
        elif 'hey' in query:
            speak("Hey how may I help you")
        elif 'hey there' in query:
            speak("Hello how may I help you")
        elif 'whats up' in query:
            speak("Nothing much you tell?")
        elif 'bye' in query:
            speak("Good bye and thank you")
            break
        elif 'who created you' in query:
            speak("Akshat Srivastava created me")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open wikipedia' in query:
            speak("Opening Wikipedia")
            webbrowser.open("wikipedia.com")

        elif 'open linkedin' in query:
            speak("Opening LinkedIn")
            webbrowser.open(
                "https://www.linkedin.com/in/akshat-srivastava-4812271a9/")

        elif 'open github' in query:
            speak("Opening Github")
            webbrowser.open("https://github.com/akshat-fsociety")

        elif 'who are you' in query:
            speak(
                "My name is Heisenberg, I'm the virtual assistant of Akshat Srivastava who created me")

        elif 'what is your name' in query:
            speak(
                "My name is Heisenberg, I'm the virtual assistant of Akshat Srivastava who created me")

        elif 'why is your name heisenberg' in query:
            speak("First tell me what is your name only first name?")
            name = getCommands().lower()
            speak(f"why is your name{name}...")
            speak("Just kidding, If you want to know the reason for my name you have to ask Akshat Srivastava who created me hahahahah ")

        elif 'why heisenberg' in query:
            speak("First tell me what is your name only first name?")
            name = getCommands().lower()
            speak(f"why is your name{name}...")
            speak("Just kidding, If you want to know the reason for my name you have to ask Akshat Srivastava who created me hahahahah ")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime(
                "%H hours %M minutes and %S seconds")
            print(strTime)
            speak(f"Sir, The time is{strTime}")

        elif "what is the day" in query:
            day = datetime.datetime.now().strftime("%A")
            speak(f"The day today is {day} ")

        elif "what is the date" in query:
            date = datetime.datetime.now().strftime("%A,%d %B, %Y")
            speak("The date today is " + date)

        elif "joke" in query:
            joke = jokes_feature.joke_choice()
            speak(joke)

        elif "set alarm" or "set a alarm" or "set an alarm" in query:
            speak("What hour do you want the alarm to be at: ")
            alarm_hour = alarm_command()
            speak("What minute do you want the alarm to be: ")
            alarm_minute = alarm_command()
            speak("Am or Pm")
            am_pm = alarm_command()
            speak("What message do you want to recieve: ")
            message = alarm_command()
            try:
                alarm_feature.start_alarm(
                    alarm_hour, alarm_minute, am_pm, message, speak)
            except Exception as e:
                print(f"Error: {e}")

        elif "search map" in query:
            location = query.replace("search", "")
            location = query.replace("map", "")
            webbrowser.open_new(
                f"https://www.google.com/maps/place/{location}")
            speak(f"Here is what I found for {location} on Google Maps")
