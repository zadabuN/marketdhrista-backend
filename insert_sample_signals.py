import asyncio
from supabase import create_client, Client

# ✅ Step 1: Use correct service role key
SUPABASE_URL = "https://ncemohxfwseymapmjntd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5jZW1vaHhmd3NleW1hcG1qbnRkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzYzNDk2OSwiZXhwIjoyMDY5MjEwOTY5fQ.grDMCrvdoR_tb4Kx5H630BMb2HSQuC1KQETWdXAXAyU"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def insert_signal():
    data = {
        "symbol": "RELIANCE",
        "date": "2025-07-27",
        "signal_type": "Buy",
        "score": 8.7,
        "pattern": "Cup & Handle",
        "sector": "Energy",
        "volume_spike": True,
        "rs_vs_nifty": 1.4,
        "adx": 28,
        "rsi": 62,
        "macd_hist": 1.1,
        "ema_stack": "20>50>100"
    }

    try:
        response = await supabase.table("signals").insert(data).execute()
        print("✅ Insert successful:", response)
    except Exception as e:
        print("❌ Insert failed:", e)

# ✅ Step 3: Run the async function
asyncio.run(insert_signal())
