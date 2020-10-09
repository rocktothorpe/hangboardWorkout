import os, sys, time
import gtts
from playsound import playsound
import tkinter as tk
import threading


def say(text):
    # read exercises aloud using google text-to-speech lol
    mp3 = "tts.mp3"
    print(text)
    tts = gtts.gTTS(text)
    tts.save(mp3)
    playsound(mp3)
    os.remove(mp3)


class HangboardWorkout:
    def __init__(self, count_time=60):
        # hangboard workouts
        self.text = ["15 second hang, 3 pull ups on jugs.",
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
        # countdown time per workout
        self.count_time = count_time
        # current countdown time
        self.i = self.count_time

        self.current_workout = ''

        self.work_thread = threading.Thread(target=self.workout, args=())
        self.gui_thread = threading.Thread(target=self.run_gui, args=())

        song_time = time.time()
        # playsound("unforgiven_ii.mp3", False)  # play metallica in background lmao

    def workout(self):
        for workout in range(len(self.text)):
            self.i = self.count_time
            self.current_workout = self.text[workout] + '\n'
            say(self.current_workout)
            while self.i > 0:
                start = time.time()
                sys.stdout.write(f'\r{self.i:03}')  # carriage return and zero pad i to be two digits
                if self.i % 10 == 0:  # beep every 10 sec (used mp3s so it works cross-platform :P)
                    # if min == 5 and i == 10:
                        # playsound("unforgiven_ii.mp3", False)  # play metallica on repeat lmao
                    playsound("beep.mp3", False)
                time.sleep(1 - (time.time() - start))  # sleep for rest of second
                self.i -= 1
            sys.stdout.write('\r')  # remove last value from stdout
            playsound("longbeep.mp3")

    def run_gui(self):
        self.root = tk.Tk()
        self.root.geometry("1200x350")
        bg1 = 'grey94'
        bg2 = 'hot pink'
        self.root.configure(background=bg1)
        font = ('Helvetica', 30)
        self.l = tk.Label(self.root, text=self.current_workout, font=font, bg=bg1)
        self.l.pack()
        self.timer = tk.Label(self.root, text=str(self.i), font=font, bg=bg1)
        self.timer.pack()
        self.dummy = tk.Label(self.root, text='', font=font, bg=bg1).pack()
        self.b = tk.Button(self.root, text='+10 s', command=self.add_time, font=font, bg=bg2)
        self.b.pack()
        self.root.after(10, self.update_gui)
        self.root.mainloop()

    def update_gui(self):
        self.l['text'] = self.current_workout
        self.timer['text'] = str(self.i)
        self.root.after(10, self.update_gui)

    def add_time(self):
        self.i += 10


if __name__ == "__main__":
    hang = HangboardWorkout(count_time=120)
    hang.gui_thread.start()
    hang.work_thread.start()

