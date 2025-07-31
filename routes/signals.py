from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase import create_client
import os

# Environment
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

router = APIRouter()

# Request model
class Signal(BaseModel):
    symbol: str
    pattern: str
    ai_score: float
    signal: str

# POST /signals
@router.post("/signals")
def insert_signal(signal: Signal):
    try:
        data = {
            "symbol": signal.symbol,
            "pattern": signal.pattern,
            "ai_score": signal.ai_score,
            "signal": signal.signal
        }
        response = supabase.table("signals").insert(data).execute()
        
        if response.data:
            return {"status": "✅ Signal inserted", "data": response.data}
        else:
            raise HTTPException(status_code=400, detail="Insert failed or returned empty response.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
