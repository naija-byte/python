from moviepy import VideoFileClip

video = VideoFileClip("fifa clip.MP4")

video.audio.write_audiofile("audio.wav")

print("audio extracted")
import librosa
import numpy as np


y, sr = librosa.load("audio.wav", sr=None)


rms = librosa.feature.rms(y=y)[0]

times = librosa.times_like(rms, sr=sr)


threshold = np.percentile(rms, 90)

highlight_times = times[rms > threshold]

print("potential highlight moments:")

for time in highlight_times:
    print(f"{time:.2f} seconds")

from moviepy import VideoFileClip


video = VideoFileClip("fifa clip.MP4")


highlights = []

if len(highlight_times) > 0:
    start = highlight_times[0]
    end = highlight_times[0]

    for time in highlight_times[1:]:
        if time - end < 10:
            end = time
        else:
            highlights.append((start, end))
            start = time
            end = time

    highlights.append((start, end))


for i, (start, end) in enumerate(highlights):
    clip_start = max(0, start - 10)
    clip_end = min(video.duration, end + 10)

    clip = video.subclipped(clip_start, clip_end)

    clip.write_videofile(
        f"highlight_{i+1}.mp4",
        codec="libx264",
        audio_codec="aac"
    )

print("highlights have been created")
