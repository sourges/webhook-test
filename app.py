from chalice import Chalice
import requests
import json 

API_KEY = ''
SECRET_KEY = ''

account_url = 'https://paper-api.alpaca.markets/v2/account'
headers = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
base_url = 'https://paper-api.alpaca.markets'
orders_url = 'https://paper-api.alpaca.markets/v2/orders'
positions_url = 'https://paper-api.alpaca.markets/v2/positions'
account_activities = 'https://paper-api.alpaca.markets/v2/account/activities'

app = Chalice(app_name='tradingview-webhook')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body
    

    data = {
        "symbol": webhook_message['ticker'],
        "qty": webhook_message['qty'],
        "side": webhook_message['side'],
        "type": "market",
        #"limit_price": webhook_message['close'],
        "time_in_force": "gtc",
        #"order_class": "bracket",
        #"take_profit": {
         #   "limit_price": webhook_message['close'] * 1.05
        }
        #"stop_loss": {
         #   "stop_price": webhook_message['close'] * 0.98,
       # }
    #}

    r = requests.post(orders_url, json = data, headers = headers)


    response = json.loads(r.content)
    print(r.content)
    

    return {
        'webhook_message': webhook_message,
        'id': response['id'],
        'client_order_id': response['client_order_id']
    }




