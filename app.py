import os
import random
import requests
import logging
from flask import Flask, jsonify
from dotenv import load_dotenv

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler()
            ]
        )

load_dotenv()
app = Flask(__name__)

DEEZER_PLAYLIST_API ="https://api.deezer.com/playlist/"
DEEZER_PLAYLIST_ID  = os.getenv("DEEZER_PLAYLIST_ID")

def get_random_preview_url():
    playlist_url = f"{DEEZER_PLAYLIST_API}{DEEZER_PLAYLIST_ID}"

    logging.info(f"{PLAYLIST_URL}")
    res = requests.get(playlist_url)
    tracks = res.json().get("tracks", [])

    logging.info(f"TRACKS: {tracks}")

    if not tracks:
        return f"Failed to retrieve tracks from playlist {DEEZER_PLAYLIST_ID}; res={json}"

    previews = [tracks['data'][n]['preview'] for n in len(tracks['data']) ]

    if not previews:
        return "Failed to parse previews from json"

    logging.info(f"PREVIEWS: {previews}")
    random_track = random.choice(previews)
    return {"preview_url": random_track}

@app.route("/random-track")
def random_track():
    track = get_random_preview_url()
    if isinstance(track, str):
        return jsonify({"error": f"No track with preview found. ERR={track}"}), 404
    return jsonify(track)

if __name__ == "__main__":
    app.run(debug=True)
