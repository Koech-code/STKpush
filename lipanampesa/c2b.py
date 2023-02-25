import requests
import json
from .import utils
from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth
from .models import STKPushResponse


unformated_timestamp = datetime.now()
formated_timestamp = unformated_timestamp.strftime("%Y%m%d%H%M%S") 

data_to_encode = utils.business_Shortcode + utils.lipa_na_mpesa_passkey + formated_timestamp
encoded_data = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_data.decode()

consumer_key = utils.consumer_key
consumer_secret = utils.consumer_secret

api_URL = (
    "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
)

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
print(r.json())

json_response = r.json() 

my_access_token = json_response['access_token']


def lipa_na_mpesa():
    access_token = my_access_token

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": utils.business_Shortcode,
        "Password": decoded_password,
        "Timestamp": formated_timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": utils.phone_number,
        "PartyB": utils.business_Shortcode,
        "PhoneNumber": utils.phone_number,
        "CallBackURL": "https://bongasport.com/lipanampesa",
        "AccountReference": "123456",
        "TransactionDesc": "Join premium"
    }

    res = requests.post(api_url, json=request, headers=headers)
    mystr = res.text
    objstr = json.loads(mystr)

    print(objstr)

    MerchantRequestID = objstr['MerchantRequestID']
    CheckoutRequestID = objstr['CheckoutRequestID']
    ResponseCode = objstr['ResponseCode']
    ResponseDescription = objstr['ResponseDescription']
    # CustomerMessage = objstr['CustomerMessage']

    data= {
        "requestId": MerchantRequestID,
        "checkoutRequestId": CheckoutRequestID,
        "responseCode": ResponseCode,
        "responseDescription": ResponseDescription,
        # "CustomerMessage": CustomerMessage
        }

    stkpush_response = STKPushResponse.objects.create(
        merchant_request_id=data['requestId'],
        checkout_request_id=data['checkoutRequestId'],
        response_code=data['responseCode'],
        response_description=data['responseDescription'],
        # customer_message=data['CustomerMessage'],
        )

    stkpush_response.save()
    return data
    
lipa_na_mpesa()
