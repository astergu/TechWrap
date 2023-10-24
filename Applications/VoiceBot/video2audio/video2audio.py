from moviepy.editor import VideoFileClip

# Define the folder path containing video files
folder_path = '../data/videos/'

# List of video file extensions to consider (e.g., .mp4, .avi, .mov)
video_extensions = ['.mp4', '.avi', '.mov']

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(tuple(video_extensions)):
            video_path = os.path.join(root, file)
            audio_output_path = os.path.splitext(video_path)[0] + '.wav'  # Change the extension if needed (e.g., .mp3)

            video = VideoFileClip(video_path)
            audio = video.audio

            audio.write_audiofile(audio_output_path)
            audio.close()
            video.close()