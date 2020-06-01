from tkinter import *
from tkinter.ttk import Progressbar
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size = 0


def on_progress(stream=None, chunk=None, file_handle=None, bytes_remaining=0):
    # progress_var.set(file_size)
    # MAX.set(file_size)
    # root.update()
    file_downloaded = (file_size - bytes_remaining)
    percentage = ((file_downloaded / file_size) * 100)
    d_btn.config(text="{:00.0f} % downloaded".format(percentage))

    # Video download on button click


def video_download():
    global file_size
    input_user = url_field.get()
    d_btn.config(text="Please Wait...")
    d_btn.config(state=DISABLED)
    # Asks for directory to save file

    save_path = askdirectory(title="select folder")

    my_video = YouTube(input_user, on_progress_callback=on_progress)
    # print(my_video)
    my_stream = my_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    file_size = my_stream.filesize
    print(file_size)
    my_stream.download(save_path)
    print("DONE")
    d_btn.config(text="Start Download")
    d_btn.config(state=NORMAL)
    showinfo("Download Finished", "Download Successful")
    url_field.delete(0, END)


def call_threading():
    thread = Thread(target=video_download)
    thread.start()


root = Tk()
# Setting geometry of window
root.geometry("655x500")
sb=Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
# title for YTD
root.title("YTDownloader")
# setting icon for YTD
p1 = PhotoImage(file="youtube-dl.png")
root.iconphoto(False, p1)
# Starting project GUI
name = Label(root, text="YTDownloader", foreground="red", font=("Forte", 40))
name.pack()
# progress_var=0
# MAX=0
# progress = Progressbar(root, orient=HORIZONTAL,
#                        variable=progress_var, maximum=MAX, mode='indeterminate')
# progress.pack()
p2 = PhotoImage(file="youtube-dl.png")
pic = Label(root, image=p2)
pic.pack()
# taking values from users
link_name = Label(root, text="Enter Link", font=("Bell MT", 20))
link_name.pack()
url_field = Entry(root, font=("Bell MT", 20), justify=CENTER)
url_field.pack(padx=100)
d_btn = Button(root, text="Start Download", font=("Bell MT", 20), command=call_threading)
d_btn.pack(pady=10)
root.mainloop()
