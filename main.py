"""Python Script that takes in the recorded video and transcribes it."""

#pip install openai-whisper
#pip install ffmpeg
#brew install ffmpeg

import subprocess
import whisper
model = whisper.load_model("base")

def transcribe():
  #path to recorded video on local device
  video_in = 'video.mp4'

  #path to mp3 for video conversion
  audio_out = 'audio.mp3'

  ffmpeg_cmd = f" ffmpeg -i {video_in} -vn -c:a libmp3lame -b:a 192k {audio_out}"

  subprocess.run(["ffmpeg", "-i", video_in, "-vn", "-c:a", "libmp3lame", "-b:a", "192k", audio_out])

  result = model.transcribe(audio_out)
  print(result["text"])
