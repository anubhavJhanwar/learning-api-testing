import requests

BASE_URL = "http://localhost:8000/users"

# ── STEP 4: DELETE ───────────────────────────────────────────────────────────
res = requests.delete(f"{BASE_URL}/6")
print(f"DELETE → {res.status_code} | {res.json()}")
