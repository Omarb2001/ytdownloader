from pytubefix import YouTube, Playlist
import pathlib

yt = None
p = None
path = r"put path you want to save here"

def download_audio_file(yt_streams, folder):
    yt.streams.get_audio_only().download(output_path=folder, mp3=True)

def download_video_file(yt_stream, res, folder):
    video = yt.streams.get_by_resolution(resolution=res)
    if not video:
        video = yt.streams.get_highest_resolution(progressive=True)
    video.download(output_path=folder)


def downloader(resolution, file_format, yt_link):

    global yt

    if r'playlist?list=' in yt_link:
        playlist_downloader(resolution, file_format, yt_link)
    else:
        yt = YouTube(yt_link)

        new_dir = pathlib.Path(path, yt.title)
        new_dir.mkdir(parents=True, exist_ok=True)

        if 'audioonly' in file_format:
            download_audio_file(yt, new_dir)
        elif 'audio' in file_format:
            download_audio_file(yt, new_dir)
            download_video_file(yt, resolution, new_dir)
        else:
            download_video_file(yt, resolution, new_dir)

def playlist_downloader(resolution, file_format, yt_link):
    p = Playlist(yt_link)

    for vid in p.video_urls:
        downloader(resolution, file_format, vid)


