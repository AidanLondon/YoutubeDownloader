from utils import download_video, download_playlist, download_channel

# get playlist or video choice
pv = input("(p)laylist or (v)ideo?\n>> ")
# get url
url = str(input("Enter the URL: \n>> "))
# get output folder
print("Enter the destination folder (blank for current):")
destination = str(input(">> ")) or "."


if pv[0].lower() == "p":
    download_playlist(url, destination)
elif pv[0].lower() == "v":
    download_video(url, destination)
