from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from broker.kite_auth import start_login, generate_access_token
from broker.order_manager import place_order, get_holdings, get_positions

router = APIRouter()

@router.post("/buy")
def buy_stock(symbol: str, qty: int = 1):
    return place_order(symbol=symbol, qty=qty, transaction_type="BUY")

@router.post("/sell")
def sell_stock(symbol: str, qty: int = 1):
    return place_order(symbol=symbol, qty=qty, transaction_type="SELL")

@router.get("/holdings")
def view_holdings():
    return get_holdings()

@router.get("/positions")
def view_positions():
    return get_positions()

@router.get("/kite_login")
def kite_login():
    url = start_login()
    return RedirectResponse(url)

@router.get("/kite_callback")
def kite_callback(request: Request):
    request_token = request.query_params.get("request_token")
    if request_token:
        access_token = generate_access_token(request_token)
        return {"message": "✅ Login successful!", "access_token": access_token}
    return {"message": "❌ Login failed. Request token not found."}
