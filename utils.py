from pytube import Playlist, YouTube, Channel
from pytube.innertube import _default_clients
import os

# Fixes issue with "mature" videos throwing errors
_default_clients["ANDROID_MUSIC"] = _default_clients["IOS"] 

def download_mp3(video, destination):
    ### Downloads a video to a specific destination as an MP3
    ### @param video - pytube Video object
    ### @param destination - string, destination folder to save to
    try:
        # get audio stream
        stream = video.streams.filter(only_audio=True).first()
        # download audio (usually as mp4)
        out_file = stream.download(output_path=destination)
        # change file type to mp3
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        # print result
        print(video.title + " has been successfully downloaded!")
    except Exception as e:
        # alert user of error and move on to next video (if relevant)
        print("!!!!!!!!!! ERROR downloading video: ", video.title)
        print(e)
        print("Continuing to next video...")


def download_video(url, destination):
    # get video from url
    v = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    # download video as mp3
    download_mp3(v, destination)


def download_playlist(url, destination):
    # get playlist from url
    p = Playlist(url)
    for video in p.videos:
        # download each video in playlist as mp3
        download_mp3(video, destination)

def download_channel(url, destination):
    # get channel from url
    c = Channel(url)
    for video in c.videos:
        # download each video from channel as mp3
        download_mp3(video, destination)