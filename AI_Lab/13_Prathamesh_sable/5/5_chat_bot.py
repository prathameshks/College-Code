import math
import wolframalpha
import wikipedia

sor, term = 0, None

main_fns = ["sorry", "end",'read']

def read():
    data = search()
    print(listenedw)

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
    print("ok good bye")
    exit()


def greet():
    print(greeting)


def searchwiki():
    print("Searching Wikipedia...")
    results = wikipedia.summary(wikidata, sentences=2)
    print("According to Wikipedia")
    print(results)


def search(question):
    app_id = "6LJUGL-QGQXA75X53"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
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
        return data


def tell():
    print("ok finding that on web")
    data = search(listenedw)
    print(data)


def sorry():
    global sor
    sor += 1
    if sor > 3:
        exit()
    print("Sorry i didn't get that.")


def run(function):
    exec(str(function + "()"))


while True:
    input_text = input("Enter Message: ")
    fnte = match(input_text)
    run(fnte)
