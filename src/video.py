from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip
import textwrap, os, datetime
def generate_video(script: str, out_dir="output"):
    os.makedirs(out_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_path = os.path.join(out_dir, f"voice_{ts}.mp3")
    img_path = os.path.join(out_dir, f"frame_{ts}.png")
    video_path = os.path.join(out_dir, f"video_{ts}.mp4")
    # TTS
    tts = gTTS(script)
    tts.save(audio_path)
    # Create image with text
    W, H = 1080, 1920
    img = Image.new("RGB", (W, H), color=(10, 10, 10))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    wrapped = textwrap.fill(script, width=30)
    draw.text((60, 200), wrapped, fill="white", font=font)
    img.save(img_path)
    # Combine image + audio
    audio = AudioFileClip(audio_path)
    clip = ImageClip(img_path).set_duration(audio.duration).set_audio(audio)
    clip.write_videofile(video_path, fps=24)
    return video_path
