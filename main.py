from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# Include signal routes AFTER app is created
from routes import signals
app.include_router(signals.router)

# Enable CORS so frontend can access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "MarketDhrista API is running ✅"}

@app.get("/ohlcv")
def get_ohlcv(symbol: str = Query(...), limit: int = Query(10)):
    try:
        response = supabase.table("OHLCV") \
            .select("*") \
            .eq("symbol", symbol) \
            .order("date", desc=True) \
            .limit(limit) \
            .execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}
