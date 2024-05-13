import os
import json

def extract_formate_data(formate_data):
    extension = formate_data["ext"]
    video_format = formate_data["format"]
    url = formate_data["url"]
    return {"extension": extension, 
            "video_format": video_format, 
            "url": url}


def get_video_data(url):
    command = f'youtube-dl "{url}" -j --no-playlist'
    output = os.popen(command).read()
    video_data = json.loads(output)
    title = video_data["title"]
    formats = video_data["formats"]
    all_formats = [extract_formate_data(i) for i in formats]
    thumbnail = video_data["thumbnail"]
    return {"title": title, "thumbnail": thumbnail, "formats": all_formats}

get_video_data("https://www.youtube.com/watch?v=P838MAC3wJc&t=1312s")