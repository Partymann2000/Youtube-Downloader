# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
 
 
# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
 
    head_label = Label(root, text="YouTube Video Downloader",
                       padx=15,
                       pady=15,
                       font="Helvetica 18 bold",
                       bg="Black",
                       fg="White")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)
 
    link_label = Label(root,
                       text="YouTube link :",
                       bg="Green",
                       pady=5,
                       padx=5,
                       font="Arial 10 bold")
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)
 
    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)
 
 
    destination_label = Label(root,
                              text="Destination :",
                              bg="Green",
                              pady=5,
                              padx=9,
                              font="Arial 10 bold")
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)
 
 
    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)
 
 
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="Green",
                      relief=GROOVE,
                      font="Arial 10 bold")
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)
 
    Download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        bg="green",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 13 bold")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)
 
 
# Defining Browse() to select a
# destination folder to save the video
 
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")
 
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)
 
# Defining Download() to download the video
 
 
def Download():
 
    # getting user-input Youtube Link
    Youtube_link = video_Link.get()
 
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    print(Youtube_link)
    if Youtube_link == "":
        messagebox.showinfo("ERROR", "Please put a link in the 'YouTube Link' Field")
    else:
        # Creating object of YouTube()
        getVideo = YouTube(Youtube_link)
     
        # Getting all the available streams of the
        # youtube video and selecting the first
        # from the
        videoStream = getVideo.streams.get_highest_resolution()
     
        # Downloading the video to destination
        # directory
        videoStream.download(download_Folder)
     
        # Displaying the message
        messagebox.showinfo("SUCCESSFULLY",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_Folder)
 
 
# Creating object of tk class
root = tk.Tk()
 
# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader by Partymann2000")
root.config(background="Black")
 
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
 
# Calling the Widgets() function
Widgets()
 
# Defining infinite loop to run
# application
root.mainloop()