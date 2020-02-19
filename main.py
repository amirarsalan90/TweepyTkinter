import tkinter as tk
from tkinter import font
import tweepy

def print_tweet(stuff):
    return 'User: %s \n%s' %(stuff[0].author.screen_name, stuff[0].text)


def get_tweet(user):
    auth = tweepy.OAuthHandler("Q4XzAOy6MsUblE5GbVgvcYPmD", "Lhm3Epvi6bJZuGZgbnGtH2fmQhDoFVfCehuh4T4HXsKlQwmI3D")
    auth.set_access_token("1152350802880684033-w3NpbaVq39EyMMU4gKknvJUX8EyP8k",
                          "QrzLllhCkVAQ0D8nBTOXD9BzYQUls5TDcKgsJ3pgEcezv")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    stuff = api.user_timeline(screen_name=user, count=10)
    label['text']=print_tweet(stuff)

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

left_frame = tk.Frame(root, bg= "#99ccff")
left_frame.place(relx=0.25, rely=0.1, relwidth=0.4, relheight=0.1, anchor="n")

entry = tk.Entry(left_frame, font=40)
entry.place(rely=0, relx=0.35, relwidth=0.7, relheight=1, anchor="n")

button = tk.Button(left_frame, text="get tweet", font=('Times', 10), command= lambda: get_tweet(entry.get()))
button.place(relx=0.85, rely=0, relheight=1, relwidth=0.3, anchor="n")

right_frame = tk.Frame(root, bg= "#99ccff")
right_frame.place(relx=0.75, rely=0, relwidth=0.5, relheight=1, anchor="n")

label = tk.Label(right_frame, font=('Times', 13))
label.place(relx=0.5, rely=0, relheight=1, relwidth=1, anchor="n")
# button = tk.Button(frame, text="weather", font=('times', 20), command= lambda: get_weather(entry.get()))
# button.place(relx=0.7, rely=0.5, relheight=0.8, relwidth=0.3, anchor="w")
#
#
# lower_frame = tk.Frame(root, bg="#99ccff")
# lower_frame.place(relx= 0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
#
# label = tk.Label(lower_frame, font=('times', 20))
# label.place(relx=0.5, rely=0.5, relheight=0.95, relwidth=0.95, anchor="c")
#
# print(tk.font.families())

root.mainloop()
