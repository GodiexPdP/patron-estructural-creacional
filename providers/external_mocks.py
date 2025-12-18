import time
import random

def bank_api(payload):
    time.sleep(1)
    return {"status": "OK", "bank_id": random.randint(1000, 9999)}

def gateway_sdk(data):
    time.sleep(0.5)
    return {"code": "00", "transaction": random.randint(10000, 99999)}

def instant_service(amount):
    time.sleep(0.2)
    return True
