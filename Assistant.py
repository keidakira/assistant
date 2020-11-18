#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

city_codes = {
    'Hyderabad': 'HYD',
    'Washington': 'WAS',
    'Washington DC': 'WAS',
    'New York': 'NYC',
    'Chicago': 'ORD',
    'Orlando': 'ORL'
}

month_codes = {
    'Dec': "12",
    'December': "12",
    'November': "11",
    'Nov': "11"
}

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    initialText = "Hey boss! How can I help you?"
    print(initialText)
    engine.say(initialText)
    engine.runAndWait()
    engine.stop()
    audio = r.listen(source, print('Listening...'))

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    print(text)

    if "flight" in text:
        # from New York to Washington DC on 22nd December
        second_half = text.split("from ")[1]
        third_half = second_half.split(" to ")
        fourth_half = third_half[1].split(" on ")

        from_city = third_half[0]
        to_city = fourth_half[0]

        date_of_travel_half = fourth_half[1].split(" ")

        date_or_month = ""
        date = ""

        for i in date_of_travel_half[0]:
            if i.isdigit():
                date_or_month += i

        if len(date_or_month) == 0:
            # Month then date
            month = date_of_travel_half[0]
            for i in date_of_travel_half[1]:
                if i.isdigit():
                    date += i
        else:
            month = date_of_travel_half[1]
            for i in date_of_travel_half[0]:
                if i.isdigit():
                    date += i

        full_date = date+month_codes[month]+"2020"

        webbrowser.open(
            f"https://www.flipkart.com/travel/search/result/flight/{city_codes[from_city]}/{city_codes[to_city]}/{full_date}//1/0/0/e")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
