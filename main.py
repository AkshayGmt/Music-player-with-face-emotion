from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
from googleapiclient.discovery import build

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)

emotions = ["happy", "sad", "angry", "neutral"]

search_map = {
    "happy": "happy songs",
    "sad": "sad songs",
    "angry": "relaxing music",
    "neutral": "focus music"
}

def search_youtube(query):
    req = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=3
    )
    res = req.execute()

    videos = []
    for item in res["items"]:
        vid = item["id"]["videoId"]
        title = item["snippet"]["title"]
        url = f"https://www.youtube.com/watch?v={vid}"
        videos.append((title, url))
    return videos


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    
    # Mock emotion
    emotion = random.choice(emotions)

    videos = search_youtube(search_map[emotion])

    return templates.TemplateResponse("index.html", {
        "request": request,
        "emotion": emotion,
        "videos": videos
    })
