#Script for a classic beginner project: downloading videos from youtube

#Important modules
import pytube
from tkinter import *
from tkinter import messagebox

#Widget to enter the video url
root = Tk()
root.title("Enter URL")

#url = StringVar(root)

e = Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def downloadvideo(url):

	youtube = pytube.YouTube(url)

	video = youtube.streams.get_highest_resolution()

	#Download the video
	video.download()

	#Printing out the video info
	video_info = "Title: "+video.title
	messagebox.showinfo("Info",video_info)

#Button to execute the downloader
dbutton = Button(root,text="Download",command=lambda:downloadvideo(e.get())).grid(row=0,column=4)

#Main loop
root.mainloop()