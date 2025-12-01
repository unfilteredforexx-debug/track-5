import requests

# 1. Define your RapidAPI Key and Headers
RAPIDAPI_KEY = "8e8de8cf74msh443bcf0b166c66ap104bb6jsnb5c5058ca44c"
HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "real-time-african-stock.p.rapidapi.com" # Updated host
}

# --- 2. Get all available markets ---
print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

# --- 3. Get top gainers ---
print("### Top Gainers (JSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/jse/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Top Gainers (nSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/nse/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Top Gainers (uSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/use/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Top Gainers (mSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/mse/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Top Gainers (luSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/luse/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Top Gainers (ngx) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/ngx/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Top Gainers (bSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/bse/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)



print("### Top Gainers (gSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/gse/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Top Gainers (zSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/zse/top-gainers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (zSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/zse/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (uSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/use/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (ngx) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/ngx/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (nSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/nse/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (mSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/mse/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (mSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/mse/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (luSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/luse/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

print("### Bottom Losers (jSE) ###")
url_gainers = "https://real-time-african-stock.p.rapidapi.com/exchange/jse/bottom-losers"
response_gainers = requests.get(url_gainers, headers=HEADERS)
gainers = response_gainers.json()
print(gainers)
print("-" * 30)

# Deleted gse and bse bottom losers

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)

print("### Markets ###")
url_markets = "https://real-time-african-stock.p.rapidapi.com/markets"
response_markets = requests.get(url_markets, headers=HEADERS) 
markets = response_markets.json()
print(markets)
print("-" * 30)
