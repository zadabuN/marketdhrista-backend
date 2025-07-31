from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/dashboard/summary")
def get_summary():
    return JSONResponse({
        "topStock": "INFY",
        "signalScore": 8.7,
        "portfolioValue": 492000,
        "marketSentiment": "Positive"
    })

@router.get("/dashboard/top-gainers")
def get_top_gainers():
    return JSONResponse([
        {"symbol": "TATAMOTORS", "change": "+5.12%"},
        {"symbol": "SBIN", "change": "+4.75%"},
        {"symbol": "RELIANCE", "change": "+3.65%"},
        {"symbol": "TCS", "change": "+2.90%"},
        {"symbol": "ADANIENT", "change": "+2.85%"}
    ])

@router.get("/dashboard/sector-heatmap")
def get_sector_heatmap():
    return JSONResponse({
        "IT": "+3.2%",
        "Banks": "+2.1%",
        "Pharma": "-1.4%",
        "Auto": "+0.9%",
        "Energy": "-0.5%"
    })
