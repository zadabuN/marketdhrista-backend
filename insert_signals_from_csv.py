import csv
import requests
import json

# Supabase Config
SUPABASE_URL = "https://ncemohxfwseymapmjntd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5jZW1vaHhmd3NleW1hcG1qbnRkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzYzNDk2OSwiZXhwIjoyMDY5MjEwOTY5fQ.GwKBjP7CNPqwQHpXRoPly64NLTrVDsYe8MI5sWi5YxI"  # Replace with real key

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# Load CSV and send each row
csv_file_path = "C:/Users/zadbu/AITradingApp/backend/signals_to_insert.csv"

with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

print("🚀 Data to insert:")
print(json.dumps(data, indent=2))


response = requests.post(
    f"{SUPABASE_URL}/rest/v1/signals",
    headers=headers,
    data=json.dumps(data)
)

if response.status_code == 201:
    print("✅ All rows inserted successfully!")
    print(response.json())
else:
    print(f"❌ Insert failed: {response.status_code}")
    print(response.text)
