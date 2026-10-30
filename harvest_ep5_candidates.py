import requests
import json
import os

API_KEY = "58313143-1ae9102078432fc7eabd59fde"
BASE_URL = "https://pixabay.com/api/"

shots_queries = {
    "shot1_hand": ["hand bone", "finger skeleton", "skeleton hand", "human hand 3d"],
    "shot2_joint": ["joint", "knee joint", "bone joint", "cartilage"],
    "shot3_fluid": ["liquid gold", "liquid amber", "fluid macro", "water drop macro"],
    "shot4_bubble": ["underwater bubble", "air bubble macro", "soap bubble macro", "bubble sphere"],
    "shot5_shockwave": ["shockwave", "water splash macro", "energy wave", "acoustic wave"],
    "shot6_xray": ["x-ray hand", "xray hands", "skeleton hands", "human skeleton"]
}

OUTPUT_DIR = r"D:\Youtube automation\remotion-shorts\public\ep5\candidates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

downloaded_catalog = {}

for shot_name, queries in shots_queries.items():
    print(f"\nSearching for {shot_name}...")
    candidates = []
    for q in queries:
        for itype in ["photo", "illustration"]:
            params = {
                "key": API_KEY,
                "q": q,
                "image_type": itype,
                "per_page": 6,
                "safesearch": "true"
            }
            res = requests.get(BASE_URL, params=params).json()
            for h in res.get("hits", []):
                tags = h.get("tags", "").lower()
                if any(bad in tags for bad in ["cartoon", "drawing", "vector", "clipart", "vintage", "child", "shark", "brochure", "furniture"]):
                    continue
                candidates.append({
                    "id": h["id"],
                    "tags": h.get("tags"),
                    "width": h.get("imageWidth"),
                    "height": h.get("imageHeight"),
                    "url": h.get("largeImageURL")
                })
    unique = list({c["id"]: c for c in candidates}.values())
    print(f"  Found {len(unique)} candidates for {shot_name}")
    
    # Download top 2 candidates for inspection
    shot_downloads = []
    for idx, c in enumerate(unique[:2]):
        ext = "jpg"
        if ".png" in c["url"]:
            ext = "png"
        filepath = os.path.join(OUTPUT_DIR, f"{shot_name}_cand{idx+1}_{c['id']}.{ext}")
        img_data = requests.get(c["url"]).content
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"  Downloaded: {filepath} ({len(img_data)/1024:.1f} KB, {c['width']}x{c['height']})")
        shot_downloads.append({
            "id": c["id"],
            "path": filepath,
            "res": f"{c['width']}x{c['height']}",
            "tags": c["tags"]
        })
    downloaded_catalog[shot_name] = shot_downloads

with open(os.path.join(OUTPUT_DIR, "catalog.json"), "w") as f:
    json.dump(downloaded_catalog, f, indent=2)
print("\nDownload complete! Catalog saved.")
