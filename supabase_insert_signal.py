import requests
import json

SUPABASE_URL = "https://ncemohxfwseymapmjntd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5jZW1vaHhmd3NleW1hcG1qbnRkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzYzNDk2OSwiZXhwIjoyMDY5MjEwOTY5fQ.GwKBjP7CNPqwQHpXRoPly64NLTrVDsYe8MI5sWi5YxI"  # your service_role key

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

data = {
    "symbol": "RELIANCE",
    "pattern": "Cup and Handle",
    "ai_score": 0.91,
    "signal": "BUY"
}

response = requests.post(
    f"{SUPABASE_URL}/rest/v1/signals",
    headers=headers,
    data=json.dumps(data)
)

if response.status_code == 201:
    print("✅ Insert successful!")
    if response.text:
        print(response.json())
    else:
        print("ℹ️ Inserted but no JSON returned.")
else:
    print(f"❌ Insert failed: {response.status_code}")
    print(response.text)
