from utils import download_video, download_playlist, download_channel

# get playlist/channel/video choice
urltype = input("(p)laylist, (c)hannel, or (v)ideo?\n>> ")
urltype = urltype[0].lower() # strip to first letter lowercase
# get url
url = str(input("Enter the URL: \n>> "))
# get output folder
print("Enter the destination folder (blank for current):")
destination = str(input(">> ")) or "."


# handle logic based on which type was selected
match urltype:
    case "p":
        download_playlist(url, destination)
    case "v":
        download_video(url, destination)
    case "c":
        download_channel(url, destination)