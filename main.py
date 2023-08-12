from moviepy.editor import VideoFileClip

def remove_audio(video_path, output_path):
    video = VideoFileClip(video_path)
    video_without_audio = video.without_audio()
    video_without_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Usage example
video_path = "video path"
output_path = "video without audio path"

remove_audio(video_path, output_path)
