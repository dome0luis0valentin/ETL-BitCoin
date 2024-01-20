"""
Extract the price of bitcoin and dolar of two API´s, and save a csv, and return 
the price of dolar
"""

import requests
import pandas as pd

def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    
    # You can replace 'usd' with your preferred currency code
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False,
        'price_change_percentage': '1h,24h,7d',  # You can customize the time intervals
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        return data
        # print(data)
        """
        Retorna:
        {
            'id': 'bitcoin',
            'symbol': 'btc',
            'name': 'Bitcoin',
            'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400',
            'current_price': 42016,
            'market_cap': 823660202892,
            'market_cap_rank': 1,
            'fully_diluted_valuation': 883212938134,
            'total_volume': 17164356980,
            'high_24h': 43097,
            'low_24h': 42058,
            'price_change_24h': -522.8870479872858,
            'price_change_percentage_24h': -1.2292,
            'market_cap_change_24h': -7679387506.593628,
            'market_cap_change_percentage_24h': -0.92374,
            'circulating_supply': 19584025.0,
            'total_supply': 21000000.0,
            'max_supply': 21000000.0,
            'ath': 69045,
            'ath_change_percentage': -39.09085,
            'ath_date': '2021-11-10T14:24:11.849Z',
            'atl': 67.81,
            'atl_change_percentage': 61919.17889,
            'atl_date': '2013-07-06T00:00:00.000Z',
            'roi': None,
            'last_updated': '2023-12-29T17:01:07.740Z',
            'price_change_percentage_1h_in_currency': -0.4566512799001862,
            'price_change_percentage_24h_in_currency': -1.2292023360685795,
            'price_change_percentage_7d_in_currency': -3.535490077528651
        },
        """
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_dolar_prices():
    api_key = "YOUR_API_KEY"  # Replace with your API key from exchangeratesapi.io
    base_url = "https://open.er-api.com/v6/latest/USD"  # API endpoint for USD as the base currency

    try:
        response = requests.get(base_url, params={"apikey": api_key})
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()
        
        # Extract exchange rates
        price_peso = data["rates"]["ARS"]
        
        return price_peso

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
  
def extract():
    """
    Extract the information of price of bitcoin and price of dolar
    """
    path_target = "./target/Precio_Bitcoin.csv"
    
    price_peso = get_dolar_prices()
    if price_peso is None:
        return None
    
    df_crypto = pd.DataFrame(columns = ["Name","Price"]) 
    dict = get_crypto_prices()
    if dict is None:
        return None
    
    for bitcoin in dict:
        new_bitcoin = {"Name": bitcoin["id"],
                    "Price": bitcoin["current_price"]}
        
        new_df = pd.DataFrame(new_bitcoin, index=[0])
        
        df_crypto = pd.concat([df_crypto, new_df], ignore_index=True)
        
    df_crypto.to_csv(path_target, index=False)    
    
    return price_peso