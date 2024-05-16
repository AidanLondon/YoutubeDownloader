from pytube import Playlist, YouTube, Channel
from pytube.innertube import _default_clients
import os

_default_clients["ANDROID_MUSIC"] = _default_clients["IOS"]

def download_mp3(video, destination):
    try:
        # get audio stream
        stream = video.streams.filter(only_audio=True).first()
        # download audio
        out_file = stream.download(output_path=destination)
        # change file type
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        # result
        print(video.title + " has been successfully downloaded!")
    except Exception as e:
        print("!!!!!!!!!! ERROR downloading video: ", video.title)
        print(e)
        print("Continuing to next video...")


def download_video(url, destination):
    # get video from url
    v = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    download_mp3(v, destination)


def download_playlist(url, destination):
    # get playlist from url
    p = Playlist(url)
    for video in p.videos:
        download_mp3(video, destination)

def download_channel(url, destination):
    c = Channel(url)
    for video in c.videos:
        download_mp3(video, destination)