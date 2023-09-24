import yt_dlp as youtube_dl
import openai
import os

# Step 1: Download the Video

# URL of WINNIE THE POOH
video_url = "https://www.youtube.com/watch?v=RE2QClKir1E&ab_channel=Disney"

# Check if 'downloads' directory exists or create it
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Set up the ytdl options
ytdl_opts = {
    'format': 'best',  # Download best single file format (video+audio combined)
    'outtmpl': 'downloads/winnie_the_pooh.%(ext)s'
}

# Download video with yt_dlp
with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
    ytdl.download([video_url])

# Step 2: Transcribe the Audio

# OpenAI and file setup
API_KEY = 'YOUR_API_KEY_HERE'  # Replace this with your actual OpenAI API key
model_id = 'whisper-1'
audio_file_path = 'downloads/winnie_the_pooh.mp4'  # Make sure it matches the format downloaded

with open(audio_file_path, 'rb') as audio_file:
    # Transcribe the audio
    response = openai.Audio.transcribe(
        api_key=API_KEY,
        model=model_id,
        file=audio_file,
        language="en"
    )

transcription = response.get('text', 'Failed to get transcription')
print(transcription)
