import requests
import json

def get_gold_prices():
    prices = {
        "world_price": "Updating...",
        "sjc_buy": "Updating...",
        "sjc_sell": "Updating..."
    }

    try:
        # Fetch data from tygia.com (Common VN financial source)
        url = "http://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now"
        response = requests.get(url, timeout=10)
        
        # Clean the response (API wraps json in brackets sometimes)
        content = response.text.replace('(', '').replace(')', '').replace(';', '')
        data = json.loads(content)

        # 1. Get SJC Price
        for item in data['golds']:
            if 'SJC' in item['code']:
                prices['sjc_buy'] = item['buy']
                prices['sjc_sell'] = item['sell']
                break
        
        # 2. Get World Price (from same source if available)
        for item in data['golds']:
            if 'WORLD' in item['code']:
                prices['world_price'] = item['sell']
                break

    except Exception as e:
        print(f"Error fetching data: {e}")

    return prices
