import requests

def get_exchange_rate(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200 or data['result'] != 'success':
        raise Exception("Error fetching exchange rate")
    
    return data['conversion_rates']['BGN']

def usd_to_bgn(usd_amount, exchange_rate):
    bgn_amount = usd_amount * exchange_rate
    return bgn_amount

def main():
    api_key = "b25e68d99553ebb8cacbbfb2"  
    try:
        exchange_rate = get_exchange_rate(api_key)
        usd_amount = float(input("Enter the amount in USD: "))
        if usd_amount < 0:
            raise ValueError("The amount cannot be negative.")
        
        bgn_amount = usd_to_bgn(usd_amount, exchange_rate)
        print(f"{usd_amount} USD is equal to {bgn_amount:.2f} BGN")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



