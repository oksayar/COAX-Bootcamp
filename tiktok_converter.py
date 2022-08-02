import os
import re
from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip


# Helper function that retracts TikTok id from url
def ID_from_URL(str):
    id_match = re.search(pattern = "[0-9]+",
                            string = str) # find number sequence substring
    return id_match.group()

# Helper function that downloads TikTok video
def download_video(tt_id):
    with TikTokApi() as api:
        video = api.video(id = tt_id) # get TikTok by id
        video_data = video.bytes() # bytes of the TikTok video

        with open(f"{tt_id}.mp4", "wb") as out_file: # save TikTok as mp4
            out_file.write(video_data)

# Function that converts TikTok to GIF
def tiktok_to_gif(str):
    tiktok_id = ID_from_URL(str)
    download_video(tiktok_id)

    clip = VideoFileClip(f"{tiktok_id}.mp4")
    print(os.path.abspath(f"{tiktok_id}.gif"))
    clip.write_gif(f"{tiktok_id}.gif") # mp4 to GIF


url = "https://www.tiktok.com/@_yu.jung/video/7083684752301083946?_t=8UU7kNK4zFm"
tiktok_to_gif(url)
