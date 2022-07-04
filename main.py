from fastapi import FastAPI
from utils import RandomYoutubeVideos
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


top_videos = RandomYoutubeVideos()
oldtime = time.time()


@app.get("/")
async def root():
    global oldtime
    global top_videos
    if (time.time() - oldtime > 5400):
        top_videos = RandomYoutubeVideos()
        oldtime = time.time()
    random_two = top_videos.sample(n=2)
    print(random_two)
    return {"video1_id": random_two.iloc[0]['video_id']
            , "video1_views": random_two.iloc[0]['num_views']
            , "video2_id": random_two.iloc[1]['video_id']
            , "video2_views": random_two.iloc[1]['num_views']}
    