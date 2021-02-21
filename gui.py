from tkinter import *

from tkinter import ttk
import tkinter as tk
import smtplib
#TODO
# 1. Make Window widget that will contain all elements we need.
# 2. Add  fields for sender adress, reciever adress, text.
# 3. Add buttons for sending and e-mail attachements
# 4. Consider using POP3 for recieving e-mail.
def send():
    # try:
    #     username = name_entry.get()
    #     to = to_entry.get()
    #     subject = subject_entry.get()
    #     body = text_field.get()
    #     if username ==""or to==""or body=="":
    #         print('All fields are required')
    #     else:
    #         final_message = 'Subject {}\n\n'.format(subject,body)
    #         server = smtplib.SMTP('smtp.gmail.com',507)
    #         server.starttls()
    #         server.login(username)
    #         server.sendmail(username,to,final_message)
    pass

window = tk.Tk()
window.title('E - mail sender')
window.geometry('650x500')
window.resizable(False,False)

#username
user_label = tk.Label(window,text = "Username")
user_label.grid(row=1,column=0,pady=2)
username = tk.Entry(window)
username.grid(row=1,column=1,pady=2)

#password
pass_label =tk.Label(window,text='Password')
pass_label.grid(row=2,column=0)
password =tk.Entry(window)
password.grid(row =2,column =1)

#to
to_label = tk.Label(window,text="To")
to_label.grid(row=3,column=0)
to_entry=tk.Entry(window)
to_entry.grid(row=3,column=1)

#subject
subject_label = tk.Label(window,text ="Subject")
subject_label.grid(row =4,column=0)
subject_entry =tk.Entry(window)
subject_entry.grid(row =4,column =1)

#Text Field
text_label = tk.Label(window,text ='Type here')
text_label.grid(row=5,column=0)
text_field = tk.Text(window,height=10)
text_field.grid(row = 7,column = 0,columnspan=5)

#Button
send = tk.Button(window,text ='Send')
send.grid(row = 10,column = 1,columnspan =3)
window.mainloop()