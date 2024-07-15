from moviepy.editor import VideoFileClip #type: ignore

def read_video(video):
    video_clip = VideoFileClip(video)
    return video_clip