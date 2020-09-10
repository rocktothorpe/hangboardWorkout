import os, sys, time
import gtts
from playsound import playsound


def say(text):
    # read exercises aloud using google text-to-speech lol
    mp3 = "tts.mp3"
    print(text)
    tts = gtts.gTTS(text)
    tts.save(mp3)
    playsound(mp3)
    os.remove(mp3)


text = ["15 second hang, 3 pull ups on jugs.",
        "20 second hang on crimp. Two pull ups on large edge.",
        "20 second hang on large edge. 20 second bent arm hang on pocket.",
        "30 second hang, 2 pull ups on jugs.",
        "20 second hang, large edge, 4 pull ups large edge.",
        "3 offset pull ups on jug and crimp.",
        "15 knee raises on sloper, 10 second hang on large edge.",
        "20 second hang, large edge.",
        "15 second hang on pocket, 3 pull ups on jug.",
        "Hang as long as possible, large edge."
        ]

for min in range(10):
    say(text[min])

    # countdown timer
    i = 60
    while i > 0:
        start = time.time()
        sys.stdout.write('\r' + str(i))
        if i % 10 == 0:  # beep every 10 sec (used mp3s so it works cross-platform :P)
            start = time.time()
            playsound("beep.mp3")
            time.sleep(1 - (time.time() - start))
        else:
            time.sleep(1)
        i -= 1
    sys.stdout.write('\r')  # remove last value from stdout
    playsound("longbeep.mp3")
