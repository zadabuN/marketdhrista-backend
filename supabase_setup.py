# supabase_setup.py
# ✅ Step 1: Install supabase client library first:
# pip install supabase

from supabase import create_client, Client

# Replace these with your own Supabase values
SUPABASE_URL = "https://ncemohxfwseymapmjntd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5jZW1vaHhmd3NleW1hcG1qbnRkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM2MzQ5NjksImV4cCI6MjA2OTIxMDk2OX0.grDMCrvdoR_tb4Kx5H630BMb2HSQuC1KQETWdXAXAyU"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Step 2: Table creation helper (optional — run only once)
def create_ohlcv_table():
    response = supabase.table("ohlcv_data").insert({
        "symbol": "DEMO",
        "date": "2025-07-27",
        "open": 100,
        "high": 105,
        "low": 98,
        "close": 104,
        "volume": 120000
    }).execute()
    print("✅ ohlcv_data table initialized (dummy row inserted)", response)


def create_signals_table():
    response = supabase.table("signals").insert({
        "symbol": "DEMO",
        "signal_date": "2025-07-27",
        "score": 0.85,
        "signal": "BUY",
        "ai_score": 0.76
    }).execute()
    print("✅ signals table initialized (dummy row inserted)", response)


# ✅ Run only once to initialize the schema
def initialize_all():
    create_ohlcv_table()
    create_signals_table()


if __name__ == "__main__":
    initialize_all()
