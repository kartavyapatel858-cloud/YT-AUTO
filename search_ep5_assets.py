import requests
import json
import os

API_KEY = "58313143-1ae9102078432fc7eabd59fde"
BASE_URL = "https://pixabay.com/api/"

queries = {
    "shot1": ["3d human hand", "hand anatomy 3d", "finger bones 3d", "skeleton hand medical"],
    "shot2": ["joint anatomy 3d", "bone joint medical 3d", "cartilage joint 3d", "human joint 3d"],
    "shot3": ["synovial fluid 3d", "microscopic fluid cell 3d", "molecules liquid 3d", "water drop macro 3d"],
    "shot4": ["cavitation bubble 3d", "water bubble macro 3d", "microscopic sphere 3d", "underwater bubble 3d"],
    "shot5": ["shockwave 3d", "acoustic wave 3d", "energy burst 3d", "explosion bubble 3d", "sound wave 3d"],
    "shot6": ["xray hands 3d", "skeleton hands 3d", "human hands anatomy 3d", "two hands medical 3d"]
}

for shot_name, query_list in queries.items():
    print(f"\n=== Searching for {shot_name} ===")
    found = []
    for q in query_list:
        params = {
            "key": API_KEY,
            "q": q,
            "image_type": "photo",
            "per_page": 10,
            "safesearch": "true"
        }
        res = requests.get(BASE_URL, params=params).json()
        hits = res.get("hits", [])
        for h in hits:
            # Filter out obvious 2d clipart or drawings
            tags = h.get("tags", "").lower()
            if any(bad in tags for bad in ["cartoon", "drawing", "vector", "clipart", "vintage", "child"]):
                continue
            found.append({
                "id": h["id"],
                "tags": h.get("tags"),
                "width": h.get("imageWidth"),
                "height": h.get("imageHeight"),
                "largeImageURL": h.get("largeImageURL"),
                "views": h.get("views"),
                "downloads": h.get("downloads")
            })
    # Remove duplicates
    unique = {item["id"]: item for item in found}.values()
    print(f"Found {len(unique)} candidate assets for {shot_name}:")
    for u in list(unique)[:4]:
        print(f"  ID: {u['id']}, Res: {u['width']}x{u['height']}, Tags: {u['tags']}")
