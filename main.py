import tkinter as tk
from tkinter import font
import sqlite3
import webbrowser



def callback(url):
   webbrowser.open_new_tab(url)

def NextUser():
   try:
      global user_number
      user_number += 1
      conn = sqlite3.connect("users.db")
      c = conn.cursor()
      username = c.execute("select User from users where rowid = ?",[user_number])
      result = username.fetchall()
      conn.close()
      label1.config(text="user number %d:\n %s" % (user_number, result[0][0]))
      label2.config(text="twitter.com/%s"%result[0][0])
      label2.bind("<Button-1>", lambda e: callback("http://www.twitter.com/%s"%result[0][0]))

   except:
      label3.configure(text="This is the last user! press previous!")


def PreviousUser():
   try:
      global user_number
      user_number -= 1
      conn = sqlite3.connect("users.db")
      c = conn.cursor()
      username = c.execute("select User from users where rowid = ?",[user_number])
      result = username.fetchall()
      conn.close()
      label1.config(text="user number %d:\n %s" % (user_number, result[0][0]))
      label2.config(text="twitter.com/%s" % result[0][0])
      label2.bind("<Button-1>", lambda e: callback("http://www.twitter.com/%s" % result[0][0]))

   except:
      label3.configure(text="This is the first user! press next!")



def set_stance(value):

   global user_number

   if value == "Anti":
      conn = sqlite3.connect("users.db")
      c = conn.cursor()
      c.execute("update users set AntiOrPro=? where rowid = ?",[value, user_number])
      conn.commit()
      c.close()
   elif value == "Pro":
      conn = sqlite3.connect("users.db")
      c = conn.cursor()
      c.execute("update users set AntiOrPro=? where rowid = ?", [value, user_number])
      conn.commit()
      c.close()

def button_zero():
   global user_number
   user_number = int(entry1.get())
   try:
      conn = sqlite3.connect("users.db")
      c = conn.cursor()
      username = c.execute("select User from users where rowid = ?", [user_number])
      result = username.fetchall()
      conn.close()
      label1.config(text="user number %d:\n %s" % (user_number, result[0][0]))
      label2.config(text="twitter.com/%s" % result[0][0])
      label2.bind("<Button-1>", lambda e: callback("http://www.twitter.com/%s" % result[0][0]))
   except:
      label3.configure(text="User number out of range!")

conn = sqlite3.connect("users.db")
c = conn.cursor()
user_number = 1
first_user = c.execute("select User from users where rowid = ?",[user_number])
result = first_user.fetchall()
conn.close()
initial_text = result[0][0]

HEIGHT = 400
WIDTH = 800


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx = 0.5, rely = 0, relwidth=1, relheight=1, anchor="n")

label0 = tk.Label(frame, font=('Helvetica', 12), bg="#BDDCED", text="insert user number: ")
label0.place(relx = 0.37, rely = 0.06, relwidth = 0.2, relheight = 0.1, anchor = "n")

entry1 = tk.Entry(frame)
entry1.place(relx = 0.52, rely = 0.06, relwidth = 0.08, relheight = 0.1, anchor = "n")
entry1.insert(0, "1")

button0 = tk.Button(frame, text="go!", font=('Times', 12), command = lambda: button_zero())
button0.place(relx = 0.6, rely = 0.06, relwidth = 0.06, relheight = 0.1, anchor = "n")

label1 = tk.Label(frame, font=('Helvetica', 15), bg="#99ccff", text="user number 1:\n %s" % initial_text)
label1.place(relx = 0.5, rely = 0.2, relwidth = 0.4, relheight = 0.3, anchor ="n")


button1 = tk.Button(frame, text="next", font=('Times', 15), command= lambda: NextUser())
button1.place(relx=0.8, rely=0.2, relwidth=0.12, relheight=0.1,anchor="n")

button2 = tk.Button(frame, text="previous", font=('Times', 15), command= lambda: PreviousUser())
button2.place(relx=0.2, rely=0.2, relwidth=0.12, relheight=0.1,anchor="n")


var = tk.StringVar()

label2 = tk.Label(frame, fg="blue", cursor="hand2")
label2.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.09, anchor="n")

R1 = tk.Radiobutton(root, text="Anti-Brexit", font=('Times', 12), variable=var, value="Anti")
R1.place(relx=0.5, rely=0.7, relwidth=0.15, relheight=0.09, anchor="n")


R2 = tk.Radiobutton(root, text="Pro-Brexit", font=('Times', 12), variable=var, value="Pro")
R2.place(relx=0.5, rely=0.8, relwidth=0.15, relheight=0.09, anchor="n")

button3 = tk.Button(frame, text="Apply", font=('Times', 13), command=lambda: set_stance(var.get()))
button3.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.1, anchor="n")

label3 = tk.Label()
label3.pack(side="bottom")
root.mainloop()


# def print_tweet(stuff):
#     return 'User: %s \n%s\n\n' %(stuff.author.screen_name, stuff.text)
#
#
# def get_tweet(user):
#     text.delete('1.0', tk.END)
#     COUNT=10
#     auth = tweepy.OAuthHandler("Q4XzAOy6MsUblE5GbVgvcYPmD", "Lhm3Epvi6bJZuGZgbnGtH2fmQhDoFVfCehuh4T4HXsKlQwmI3D")
#     auth.set_access_token("1152350802880684033-w3NpbaVq39EyMMU4gKknvJUX8EyP8k",
#                           "QrzLllhCkVAQ0D8nBTOXD9BzYQUls5TDcKgsJ3pgEcezv")
#     api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#     stuff = api.user_timeline(screen_name=user, count=COUNT)
#     for i in range(COUNT):
#         text.insert(tk.END, print_tweet(stuff[i]))