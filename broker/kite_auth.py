from kiteconnect import KiteConnect
import webbrowser
import os

API_KEY = "gshctnzvqk0m0qx5"
API_SECRET = "gdjjcjnieu1x59j3ohg9d0ha60qw9asi"
REDIRECT_URI = "http://127.0.0.1:8000/kite_callback"

kite = KiteConnect(api_key=API_KEY)

def start_login():
    login_url = kite.login_url()
    print(f"🔗 Please copy and open this link in your browser manually:\n{login_url}")
    return login_url

def generate_access_token(request_token):
    try:
        data = kite.generate_session(request_token, api_secret=API_SECRET)
        access_token = data["access_token"]
        
        # Save token for future use
        with open("access_token.txt", "w") as f:
            f.write(access_token)
        print(f"✅ Access token saved: {access_token}")
        return access_token
    except Exception as e:
        print(f"❌ Failed to generate token: {e}")
        return None
