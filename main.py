import tkinter as tk
from tkinter import font
import tweepy

def print_tweet(stuff):
    return 'User: %s \n%s\n\n' %(stuff.author.screen_name, stuff.text)


def get_tweet(user):
    text.delete('1.0', tk.END)
    COUNT=10
    auth = tweepy.OAuthHandler("Q4XzAOy6MsUblE5GbVgvcYPmD", "Lhm3Epvi6bJZuGZgbnGtH2fmQhDoFVfCehuh4T4HXsKlQwmI3D")
    auth.set_access_token("1152350802880684033-w3NpbaVq39EyMMU4gKknvJUX8EyP8k",
                          "QrzLllhCkVAQ0D8nBTOXD9BzYQUls5TDcKgsJ3pgEcezv")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    stuff = api.user_timeline(screen_name=user, count=COUNT)
    for i in range(COUNT):
        text.insert(tk.END, print_tweet(stuff[i]))

HEIGHT = 600
WIDTH = 600

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

left_frame = tk.Frame(root, bg= "#99ccff")
left_frame.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2, anchor="n")

entry = tk.Entry(left_frame, font=('Times', 13))
entry.place(relx=0.5, rely=0, relwidth=1, relheight=0.5, anchor="n")
# #
button = tk.Button(left_frame, text="get tweet", font=('Times', 13), command= lambda: get_tweet(entry.get()))
button.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.5,anchor="n")
# button.pack()

upper_right_frame = tk.Frame(root, bg='#ff8080')
upper_right_frame.place(relx=0.6, rely=0, relwidth=0.8, relheight=0.2, anchor="n")

lower_right_frame = tk.Frame(root, bg= "#99ccff")
lower_right_frame.place(relx=0.6, rely=0.2, relwidth=0.8, relheight=0.8, anchor="n")

text = tk.Text(lower_right_frame, font=('Helvetica', 13), wrap="word")

text.place(relx = 0.5, rely=0, relheight=1, relwidth=1, anchor="n")


root.mainloop()
