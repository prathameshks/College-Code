import pyttsx3
import math

import wolframalpha
import wikipedia

sor, term = 0, None

main_fns = ["sorry", "end",'read']

def read():
    # speak("ok finding that on web")
    # data = search()
    speak(listenedw)

def speak(textmain):
    engine = pyttsx3.init()  # object creation
    engine.setProperty("rate", 150)  # setting up new voice rate
    engine.setProperty("volume", 3.0)  # setting up volume level  between 0 and 1
    voices = engine.getProperty("voices")
    engine.setProperty(
        "voice", voices[1].id
    )  # changing index, changes voices. o for male, 1 for female
    print(textmain)
    # updatetextcomp(str(textmain))
    try:
        engine.say(textmain)
        # engine.save_to_file('Hello World', 'test.mp3')
        engine.runAndWait()
        engine.stop()
        return True
    except:
        engine.say("Something went wrong.")
        engine.runAndWait()
        engine.stop()
        return False


def match(listened, mainfns=main_fns):
    global term
    global listenedw
    greets = [
        "greet",
        "hi",
        "good morning",
        "good night",
        "how are you",
        "i am fine",
        "whats up",
        "good day",
        "good evening",
    ]
    listenedw = listened.lower()
    words = listenedw.split(" ")
    if listenedw in ["close", "quit", "exit", "stop", "stop listening"]:
        return "end"
    elif listenedw in greets:
        # greet
        greetresp = [
            "Hello",
            "hi",
            "good morning,have a good day",
            "ok good night, sweet dreams",
            "I am fine, tell about you",
            "ok, what can i do for you?",
            "everything cool",
            "same to you",
            "good evening",
        ]
        global greeting
        greeting = greetresp[greets.index(listenedw)]
        return "greet"

    elif words[0].lower() in ["information", "search", "find"]:
        global wikidata
        wikidata = str(listenedw[int(len(words[0]) + 1) :])
        # wikidata=str(listenedw)
        return "searchwiki"

    elif words[0].lower() == 'read':
        listenedw.replace('read', '')
        return "read"

    else:
        bestfn = "False"
        for fn in mainfns:
            i = fn.lower()
            fnwords = i.split("_")
            matches = 0
            for j in words:
                if j in fnwords:
                    matches += 1
            if matches >= math.ceil(len(words)):
                bestfn = fn
        if bestfn == "False":
            return "tell"
        else:
            return bestfn


def end():
    speak("ok good bye")
    exit()


def greet():
    speak(greeting)


def searchwiki():
    speak("Searching Wikipedia...")
    results = wikipedia.summary(wikidata, sentences=2)
    speak("According to Wikipedia")
    speak(results)


def search(question):
    app_id = "6LJUGL-QGQXA75X53"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    # print(res)
    if res["@success"]:
        pod0 = res["pod"][0]["subpod"]["plaintext"]
        if (question.lower()).startswith("tell"):
            data = "ok\n"
        else:
            data = str(pod0 + "\n")
        pod1 = res["pod"][1]
        if (
            ("definition" in pod1["@title"].lower())
            or ("result" in pod1["@title"].lower())
            or (pod1.get("@primary", "false") == "true")
        ):
            result = pod1["subpod"]["plaintext"]
            data += str(result)
        return data
    else:
        data = str("can't get information.")
        # sorry()
        return data


def tell():
    speak("ok finding that on web")
    data = search(listenedw)
    speak(data)


def sorry():
    global sor
    sor += 1
    if sor > 3:
        exit()
    speak("Sorry i didn't get that.")


# last
def run(function):
    exec(str(function + "()"))


while True:
    input_text = input("Enter Message: ")
    fnte = match(input_text)
    run(fnte)
