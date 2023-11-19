import os
from tkinter import *
from tkinter import ttk
from download_module import download_video
import smtplib
from send_email import *
from email.message import EmailMessage
import ssl
from tkinter import simpledialog

def open_settings():
    global email_receiver, subject, body
    email_receiver = simpledialog.askstring("Settings", "Enter new email_receiver:", initialvalue=email_receiver)
    subject = simpledialog.askstring("Settings", "Enter new subject:", initialvalue=subject)
    body = simpledialog.askstring("Settings", "Enter new body:", initialvalue=body)
    edit_confirmation_label.config(text="Data edited successfully!")

root = Tk()

settings_button = Button(root, text="⚙", command=open_settings)
settings_button.pack(side=TOP,anchor=NE, padx=10, pady=10)

root.title("YouTube Video Downloader")

root.geometry("500x300")


title_label = Label(root, text="YouTube Video Downloader", font=("Arial", 16))
title_label.pack(pady=10)

url_label = Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = Entry(root, width=40)
url_entry.pack()



# Label to display edit confirmation
edit_confirmation_label = Label(root, text="", font=("Arial", 10))
edit_confirmation_label.pack()

download_location_label = Label(root, text="Enter download location:")
download_location_label.pack()

download_location_entry = Entry(root, width=40)
download_location_entry.pack()

resolution_label = Label(root, text="Choose Resolution:")
resolution_label.pack()

resolution = ttk.Combobox(root, values=["Video (MP4)", "Audio (MP3)"])
resolution.pack()

def on_enter(e):
    download_button['background'] = 'green'
def on_leave(e):
    download_button['background'] = 'gray'
def on_enter2(e):
    send_button['background'] = 'green'
def on_leave2(e):
    send_button['background'] = 'gray'



download_button = Button(root, text="Download", command=lambda: download_video(url_entry, download_location_entry, resolution, status_label), font=("Arial", 10), bg="gray", fg="white")
download_button.pack(pady=10)
download_button.bind("<Enter>", on_enter)
download_button.bind("<Leave>", on_leave)

def download_and_send():
    file_path = download_video(url_entry, download_location_entry, resolution, status_label)
    if file_path is not None:
        send_email(file_path)

send_button = Button(root, text="Download and send", command=lambda: download_and_send(), font=("Arial", 10), bg="gray", fg="white")
send_button.pack(pady=1)
send_button.bind("<Enter>", on_enter2)
send_button.bind("<Leave>", on_leave2)


status_label = Label(root, text="", font=("Arial", 12))
status_label.pack()

root.mainloop()
