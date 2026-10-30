import urllib.request
import os

url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/3D_Medical_Animation_Mid-Brain_Different_Parts.jpg"
dst = r"C:\Users\Kartavya\.gemini\antigravity\brain\8b92f3a4-dcf5-4f68-be3b-563b23a7bbe4\reference_midbrain_3d.jpg"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
        with open(dst, "wb") as f:
            f.write(data)
    print(f"SUCCESS: Downloaded {len(data)} bytes to {dst}")
except Exception as e:
    print(f"FAILED: {e}")
