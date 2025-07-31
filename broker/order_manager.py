from kiteconnect import KiteConnect
import os

API_KEY = "your_api_key_here"

def get_kite_client():
    # Load access token from file
    try:
        with open("access_token.txt", "r") as f:
            access_token = f.read().strip()
    except FileNotFoundError:
        raise Exception("⚠️ access_token.txt not found. Please login first.")

    kite = KiteConnect(api_key=API_KEY)
    kite.set_access_token(access_token)
    return kite

def place_order(symbol, qty=1, transaction_type="BUY", product="CNC", order_type="MARKET"):
    kite = get_kite_client()

    try:
        order_id = kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange=kite.EXCHANGE_NSE,
            tradingsymbol=symbol,
            transaction_type=transaction_type,
            quantity=qty,
            product=product,
            order_type=order_type
        )
        return {"status": "✅ Order placed", "order_id": order_id}
    except Exception as e:
        return {"status": "❌ Order failed", "error": str(e)}

def get_holdings():
    kite = get_kite_client()
    return kite.holdings()

def get_positions():
    kite = get_kite_client()
    return kite.positions()
