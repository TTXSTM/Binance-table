from dataclasses import field
from email.policy import strict
from importlib.util import spec_from_file_location
from os import access
import re
import time
from unittest import result
import pip
from urllib.request import urlopen
import json
import requests
import httplib2
import apiclient
import google_auth_httplib2
import google
import googleapiclient
from oauth2client.service_account import ServiceAccountCredentials	
from datetime import datetime



headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "content-type": "application/json",
    "Host": "p2p.binance.com",
    "Origin": "https://p2p.binance.com",
    "Pragma": "no-cache",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

USDT_RosBank_BUY= {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

USDT_RosBank1k_BUY = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY",
    "transAmount": "1000"  
}

BTC_RosBank_BUY= {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BTC_RosBank1k_BUY = {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000" 
}

BUSD_RosBank_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BUSD_RosBank1k_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BNB_RosBank_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BNB_RosBank1k_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

ETH_RosBank_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

ETH_RosBank1k_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

RUB_RosBank_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

RUB_RosBank1k_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

SHIB_RosBank_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

SHIB_RosBank1k_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["RosBankNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}


USDT_Tinkoff_BUY = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

USDT_Tinkoff1k_BUY = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY",
    "transAmount": "1000" 
}

BTC_Tinkoff_BUY = {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY",
}

BTC_Tinkoff1k_BUY = {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY",
    "transAmount": "1000"
}

BUSD_Tinkoff_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BUSD_Tinkoff1k_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BNB_Tinkoff_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BNB_Tinkoff1k_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

ETH_Tinkoff_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

ETH_Tinkoff1k_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

RUB_Tinkoff_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

RUB_Tinkoff1k_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

SHIB_Tinkoff_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

SHIB_Tinkoff1k_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["TinkoffNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

USDT_Qiwi_BUY = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

USDT_Qiwi1k_BUY = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BTC_Qiwi_BUY = {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BTC_Qiwi1k_BUY = {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BUSD_Qiwi_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BUSD_Qiwi1k_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BNB_Qiwi_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BNB_Qiwi1k_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

ETH_Qiwi_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

ETH_Qiwi1k_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

RUB_Qiwi_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

RUB_Qiwi1k_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

SHIB_Qiwi_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

SHIB_Qiwi1k_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["QIWI"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

USDT_YouMoney_BUY = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

USDT_YouMoney1k_BUY = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BTC_YouMoney_BUY = {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BTC_YouMoney1k_BUY = {
    "asset": "BTC",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BUSD_YouMoney_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BUSD_YouMoney1k_BUY = {
    "asset": "BUSD",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

BNB_YouMoney_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

BNB_YouMoney1k_BUY = {
    "asset": "BNB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

ETH_YouMoney_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

ETH_YouMoney1k_BUY = {
    "asset": "ETH",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

RUB_YouMoney_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

RUB_YouMoney1k_BUY = {
    "asset": "RUB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}

SHIB_YouMoney_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
}

SHIB_YouMoney1k_BUY = {
    "asset": "SHIB",
    "fiat": "RUB",
    "merchantCheck": False,
    "page": 1,
    "payTypes": ["YandexMoneyNew"],
    "publisherType": None,
    "rows": 1,
    "tradeType": "BUY", 
    "transAmount": "1000"
}



usdt_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_RosBank_BUY)
rs = usdt_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_usdt_s = float(price_s[0].strip('""'))

usdt_RosBank1k = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_RosBank1k_BUY)
rs = usdt_RosBank1k.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_usdt_s1k = float(price_s[0].strip('""'))

btc_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_RosBank_BUY)
rs = btc_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_btc_s = float(price_s[0].strip('""'))

btc_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_RosBank1k_BUY)
rs = btc_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_btc_s1k = float(price_s[0].strip('""'))

busd_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_RosBank1k_BUY)
rs = busd_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_busd_s1k = float(price_s[0].strip('""'))

busd_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_RosBank_BUY)
rs = busd_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_busd_s = float(price_s[0].strip('""'))

bnb_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_RosBank1k_BUY)
rs = bnb_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_bnb_s1k = float(price_s[0].strip('""'))

bnb_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_RosBank_BUY)
rs = bnb_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_bnb_s = float(price_s[0].strip('""'))

eth_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_RosBank1k_BUY)
rs = eth_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_eth_s1k = float(price_s[0].strip('""'))

eth_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_RosBank_BUY)
rs = eth_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_eth_s = float(price_s[0].strip('""'))

rub_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_RosBank1k_BUY)
rs = rub_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_rub_s1k = float(price_s[0].strip('""'))

rub_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_RosBank_BUY)
rs = rub_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_rub_s = float(price_s[0].strip('""'))

shib_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_RosBank1k_BUY)
rs = shib_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_shib_s1k = float(price_s[0].strip('""'))

shib_RosBank = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_RosBank_BUY)
rs = shib_RosBank.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_s = ss.split()
buy_shib_s = float(price_s[0].strip('""'))

usdt_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_Tinkoff_BUY )
rt = usdt_Tinkoff.content
jt=json.loads(rt)
st = json.dumps(jt["data"][0]["adv"]["price"])
price_t = st.split()
buy_usdt_t = float(price_t[0].strip('""'))

usdt_Tinkoff1k = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_Tinkoff1k_BUY )
rt = usdt_Tinkoff1k.content
jt=json.loads(rt)
st = json.dumps(jt["data"][0]["adv"]["price"])
price_t = st.split()
buy_usdt_t1k = float(price_t[0].strip('""'))

btc_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_Tinkoff_BUY )
rt = btc_Tinkoff.content
jt=json.loads(rt)
st = json.dumps(jt["data"][0]["adv"]["price"])
price_t = st.split()
buy_btc_t = float(price_t[0].strip('""'))

btc_Tinkoff1k = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_Tinkoff1k_BUY )
rt = btc_Tinkoff.content
jt=json.loads(rt)
st = json.dumps(jt["data"][0]["adv"]["price"])
price_t = st.split()
buy_btc_t1k = float(price_t[0].strip('""'))

busd_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_Tinkoff1k_BUY)
rs = busd_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_busd_t1k = float(price_t[0].strip('""'))

busd_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_Tinkoff_BUY)
rs = busd_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_busd_t = float(price_t[0].strip('""'))

bnb_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_Tinkoff1k_BUY)
rs = bnb_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_bnb_t1k = float(price_t[0].strip('""'))

bnb_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_Tinkoff_BUY)
rs = bnb_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_bnb_t = float(price_t[0].strip('""'))

eth_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_Tinkoff1k_BUY)
rs = eth_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_eth_t1k = float(price_t[0].strip('""'))

eth_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_Tinkoff_BUY)
rs = eth_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_eth_t = float(price_t[0].strip('""'))

rub_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_Tinkoff1k_BUY)
rs = rub_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_rub_t1k = float(price_t[0].strip('""'))

rub_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_Tinkoff_BUY)
rs = rub_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_rub_t = float(price_t[0].strip('""'))

shib_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_Tinkoff1k_BUY)
rs = shib_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_shib_t1k = float(price_t[0].strip('""'))

shib_Tinkoff = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_Tinkoff_BUY)
rs = shib_Tinkoff.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_t = ss.split()
buy_shib_t = float(price_t[0].strip('""'))

usdt_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_Qiwi1k_BUY)
rs = usdt_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_usdt_q = float(price_q[0].strip('""'))

usdt_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_Qiwi1k_BUY)
rs = usdt_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_usdt_q1k = float(price_q[0].strip('""'))

btc_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_Qiwi_BUY)
rs = btc_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_btc_q = float(price_q[0].strip('""'))

btc_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_Qiwi1k_BUY)
rs = btc_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_btc_q1k = float(price_q[0].strip('""'))

busd_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_Qiwi_BUY)
rs = busd_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_busd_q = float(price_q[0].strip('""'))

busd_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_Qiwi1k_BUY)
rs = busd_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_busd_q1k = float(price_q[0].strip('""'))

bnb_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_Qiwi_BUY)
rs = bnb_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_bnb_q = float(price_q[0].strip('""'))

bnb_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_Qiwi1k_BUY)
rs = bnb_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_bnb_q1k = float(price_q[0].strip('""'))

eth_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_Qiwi_BUY)
rs = eth_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_eth_q = float(price_q[0].strip('""'))

eth_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_Qiwi1k_BUY)
rs = eth_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_eth_q1k = float(price_q[0].strip('""'))

rub_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_Qiwi_BUY)
rs = rub_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_rub_q = float(price_q[0].strip('""'))

rub_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_Qiwi1k_BUY)
rs = rub_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_rub_q1k = float(price_q[0].strip('""'))

shib_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_Qiwi_BUY)
rs = shib_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_shib_q = float(price_q[0].strip('""'))

shib_Qiwi = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_Qiwi1k_BUY)
rs = shib_Qiwi.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_q = ss.split()
buy_shib_q1k = float(price_q[0].strip('""'))

usdt_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_YouMoney_BUY)
rs = usdt_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_usdt_y = float(price_y[0].strip('""'))

usdt_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=USDT_YouMoney1k_BUY)
rs = usdt_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_usdt_y1k = float(price_y[0].strip('""'))

btc_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_YouMoney_BUY)
rs = btc_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_btc_y = float(price_y[0].strip('""'))

btc_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BTC_YouMoney1k_BUY)
rs = btc_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_btc_y1k = float(price_y[0].strip('""'))

busd_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_YouMoney_BUY)
rs = busd_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_busd_y = float(price_y[0].strip('""'))

busd_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BUSD_YouMoney1k_BUY)
rs = busd_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_busd_y1k = float(price_y[0].strip('""'))

bnb_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_YouMoney_BUY)
rs = bnb_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_bnb_y = float(price_y[0].strip('""'))

bnb_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=BNB_YouMoney1k_BUY)
rs = bnb_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_bnb_y1k = float(price_y[0].strip('""'))

eth_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_YouMoney_BUY)
rs = eth_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_eth_y = float(price_y[0].strip('""'))

eth_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=ETH_YouMoney1k_BUY)
rs = eth_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_eth_y1k = float(price_y[0].strip('""'))

rub_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_YouMoney_BUY)
rs = rub_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_rub_y = float(price_y[0].strip('""'))

rub_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=RUB_YouMoney1k_BUY)
rs = rub_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_rub_y1k = float(price_y[0].strip('""'))

shib_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_YouMoney_BUY)
rs = shib_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_shib_y = float(price_y[0].strip('""'))

shib_YouMoney = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=SHIB_YouMoney1k_BUY)
rs = shib_YouMoney.content
js = json.loads(rs)
ss = json.dumps(js["data"][0]["adv"]["price"])
price_y = ss.split()
buy_shib_y1k = float(price_y[0].strip('""'))

CREDENTIALS_FILE = "p2p-spred-2f9fa1af4e50.json"


credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 


spreadsheetId = "1Y94AuKGaXngilOuie8uR5lByybo7Yg63AyQwQie5dIc"



results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
    "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
    "data": [
        {"range": "B3:I10",
         "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
         "values": [
                    ["Любая сумма", "USDT", "BTC", "BUSD", "BNB", "ETH", "RUB", "SHIB"],
                    ["Tinkoff", buy_usdt_t, buy_btc_t, buy_busd_t, buy_bnb_t, buy_eth_t, buy_rub_t, buy_shib_t], # Заполняем первую строку
                    ["Росбанк", buy_usdt_s, buy_btc_s, buy_busd_s, buy_bnb_s, buy_eth_s, buy_rub_s, buy_shib_s],
                    ["Юмани", buy_usdt_y, buy_btc_y, buy_busd_y, buy_bnb_y, buy_eth_y, buy_rub_y, buy_shib_y],
                    ["Райфайзен", "0", "0", "0", "0", "0"],
                    ["Qiwi", buy_usdt_q, buy_btc_q, buy_busd_q, buy_bnb_q, buy_eth_q, buy_rub_q, buy_shib_q],
                    ["Фиат", "0", "0", "0", "0", "0"],
                    ["Payeer", "0", "0", "0", "0", "0"]  # Заполняем вторую строку
                   ]}
    ]
}).execute()
results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
    "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
    "data": [
        {"range": "B12:I20",
         "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
         "values": [
                    ["От 1000", "USDT", "BTC", "BUSD", "BNB", "ETH", "RUB", "SHIB"],
                    ["Tinkoff", buy_usdt_t1k, buy_btc_t1k, buy_busd_t1k, buy_bnb_t1k, buy_eth_t1k, buy_rub_t1k, buy_shib_t1k], # Заполняем первую строку
                    ["Росбанк", buy_usdt_s1k, buy_btc_s1k, buy_busd_s1k, buy_bnb_s1k, buy_eth_s1k, buy_rub_s1k, buy_shib_t1k],
                    ["Юмани", buy_usdt_y1k, buy_btc_y1k, buy_busd_y1k, buy_bnb_y1k, buy_eth_y1k, buy_rub_y1k, buy_shib_y1k],
                    ["Райфайзен", "0", "0", "0", "0", "0"],
                    ["Qiwi", buy_usdt_q1k, buy_btc_q1k, buy_busd_q1k, buy_bnb_q1k, buy_eth_q1k, buy_rub_q1k, buy_shib_q1k],
                    ["Фиат", "0", "0", "0", "0", "0"],
                    ["Payeer", "0", "0", "0", "0", "0"]  # Заполняем вторую строку
                   ]}
        
    ]
}).execute()






current_datetime = datetime.now()


print("Update RUB-BUY", current_datetime)


    













