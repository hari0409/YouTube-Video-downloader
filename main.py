import tkinter.ttk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog
import os,sys,subprocess,shutil
import winsound

# For Naming
file_name = ""


# File Location
def openlocation():
    global file_name
    file_name = filedialog.askdirectory()
    if len(file_name) > 1:
        locationerror.config(text=file_name, fg="green")
    else:
        locationerror.config(text="Please choose a valid location!!", fg="red")
# download video
def downloadvideo():
    choice = ytchoice.get()
    url = ytlink.get()
    print(choice)
    if len(url) > 1:
        yterror.config(text="")
        yt = YouTube(url)
        if choice == choices[0]:
            yt.streams.filter(file_extension="mp4", res="4320p").first().download(filename="video")
        elif choice == choices[1]:
            yt.streams.filter(file_extension="mp4", res="2880p").first().download(filename="video")
        elif choice == choices[2]:
            yt.streams.filter(file_extension="mp4", res="2160p").first().download(filename="video")
        elif choice == choices[3]:
            yt.streams.filter(file_extension="mp4", res="1440p").first().download(filename="video")
        if choice == choices[4]:
            yt.streams.filter(file_extension="mp4", res="1080p").first().download(filename="video")
        elif choice == choices[5]:
            yt.streams.filter(res="720p", file_extension="mp4").first().download(filename="video")
        elif choice == choices[6]:
            yt.streams.filter(res="480p", file_extension="mp4").first().download(filename="video")
        elif choice == choices[7]:
            yt.streams.filter(res="360p", file_extension="mp4").first().download(filename="video")
        elif choice == choices[8]:
            yt.streams.filter(res="240p", file_extension="mp4").first().download(filename="video")
        elif choice == choices[9]:
            yt.streams.filter(res="144p", file_extension="mp4").first().download(filename="video")
    else:
        yterror.config(text="Paste the link correctly!!", fr="red")
    yterror.config(text="Downladed", fg="green")
    winsound.Beep(1500,2000)


def wavfile():
    # url input from user
    url=ytlink.get()
    if len(url)>1:
        yt = YouTube(url)
        # extract only audio
        audio = yt.streams.get_audio_only()
        # check for destination to save file
        destination = file_name
        # download the file
        out_file = audio.download(output_path=destination)
        # save the file
        base, ext = os.path.splitext(out_file)
        base = "audio"
        new_file = base + '.wav'
        os.rename(out_file, new_file)
        # result of success
        print(yt.title + " audio has been successfully downloaded.Download video next")

# Object
root = Tk()
# Title
root.title("Youtube Downloader")
# Dimension of Window
root.geometry("350x400")
# To align all component to center
root.columnconfigure(0, weight=1)
# Link input label
linklabel = Label(root, text="Enter the link of the Youtube Video", font=("Consoles", 16))
linklabel.grid(padx=5, pady=5)
# Get input link
ytlinkvar = StringVar()
ytlink = Entry(root, width=50, textvariable=ytlinkvar)
ytlink.grid()
# Error for wrong link
yterror = Label(root, text="Error in the link", fg="red", font=("Consoles", 10))
yterror.grid()
# Save Label
savelabel = Label(root, text="Video Path", font=("Consoles", 14, "bold"))
savelabel.grid(padx=5, pady=5)
# Button for save location
savevideo = Button(root, width=10, bg="red", fg="black", text="Choose path", command=openlocation)
savevideo.grid()
# Error for wrong location
locationerror = Label(root, text="Error in the location selected", fg="red", font=("Consoles", 10))
locationerror.grid()
# Label of download quality
ytqualitylabel = Label(root, text="Select Quality", font=("Consoles", 14))
ytqualitylabel.grid(padx=5, pady=5)
# List for quality
choices = ["4320p 8K", "2880p 5K", "2160p 4K", "1440p 2K", "1080p FHD", "720p HD", "480p", "360p", "240p", "144p"]
ytchoice = tkinter.ttk.Combobox(root, values=choices)
ytchoice.grid()
# Download Button audio
downloadba = Button(root, width=10, bg="red", fg="black", text="Download audio", command=wavfile)
downloadba.grid(padx=10, pady=10)
# Download Button video
downloadbv = Button(root, width=10, bg="red", fg="black", text="Download Video", command=downloadvideo)
downloadbv.grid(padx=10, pady=10)
# Credit
credit = Label(root, text="**By everyone to everyone**", font=("Consoles", 7, "italic"))
credit.grid()
# To display Window endlessly
root.mainloop()




name=input("Save as :")
cmd=f"ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac {name}.mp4"
if sys.platform.startswith('win32'):
    subprocess.call(cmd,shell=True)
if sys.platform.startswith('linux'):
    subprocess.call(cmd)
os.remove("video.mp4")
# dl=input("Do you want to delete the audio(y/n)")
# if dl.lower()=='y':
#     os.remove("audio.wav")
# else:#rename
#     newname=name
#     os.rename("audio.wav",newname)
os.remove("audio.wav")
#movie video to specified loc
cp=os.getcwd()
cp+=f"\{name}.mp4"
file_name+=f"\{name}.mp4"
shutil.move(cp,file_name)

