import streamlit as st
import yt_dlp

from yt_dlp import YoutubeDL


@st.cache   #_data
def download_video_from_url(url):
    videoinfo = YoutubeDL().extract_info(url=url, download=False)
    filename = f"./youtube/{videoinfo['id']}.mp4"
    options = {
        'format': 'best', # Use 'best' to download both video and audio
        'keepvideo': True,
        'outtmpl': filename,
    }
    with YoutubeDL(options) as ydl:
        ydl.download([videoinfo['webpage_url']])
    return filename


@st.cache    #_data
def download_audio_from_url(url):
    videoinfo = YoutubeDL().extract_info(url=url, download=False)
    filename = f"./youtube/{videoinfo['id']}.mp3"
    options = {
        'format': 'bestaudio/best',  # Download the best audio
        'keepvideo': False,  # Don't keep the video
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # Audio quality
        }],
    }
    with YoutubeDL(options) as ydl:
        ydl.download([videoinfo['webpage_url']])
    return filename





st.title("YouTube Downloader")


st.info("Kopiere den Link rein der bei Share angegeben wird ")
url = st.text_input('Url reinkopieren:', '')

if url !="":
    filename_video = download_video_from_url(url)
    st.video(filename_video)
    with open(filename_video, "rb") as f:
        st.download_button("Download Video", data=f, file_name="YT_video.mp4")
    
    _="""

   # Add an option to download the audio - 
   Please install or provide the path using --ffmpeg-location," indicates that the yt-dlp library requires FFmpeg to be installed and properly configured in your system.
    if st.button("Download Audio (MP3)"):
        filename_audio = download_audio_from_url(url)
        with open(filename_audio, "rb") as f:
            st.download_button("Download Audio (MP3)", data=f, file_name="audio.mp3")

    """
    


