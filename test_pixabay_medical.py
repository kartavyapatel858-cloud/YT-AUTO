import requests

API_KEY = "58313143-1ae9102078432fc7eabd59fde"
BASE_URL = "https://pixabay.com/api/"

test_queries = [
    "skeleton hand",
    "hand anatomy",
    "human bones",
    "joint bone",
    "synovial",
    "cartilage",
    "microscopic bubble",
    "water bubble",
    "bubble macro",
    "shockwave",
    "x-ray hand",
    "medical 3d"
]

for q in test_queries:
    for itype in ["photo", "illustration"]:
        params = {
            "key": API_KEY,
            "q": q,
            "image_type": itype,
            "per_page": 5,
            "safesearch": "true"
        }
        res = requests.get(BASE_URL, params=params).json()
        hits = res.get("hits", [])
        med_hits = [h for h in hits if any(k in h.get("tags","").lower() for k in ["bone", "hand", "anatomy", "medical", "skeleton", "bubble", "fluid", "joint", "science", "biology"])]
        if med_hits:
            print(f"[{itype.upper()}] Query: '{q}' -> {len(med_hits)} relevant matches:")
            for h in med_hits[:2]:
                print(f"   ID: {h['id']}, {h['imageWidth']}x{h['imageHeight']}, URL: {h['largeImageURL']}")
                print(f"   Tags: {h['tags']}")
