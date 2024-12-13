This is not offical SDK for mpesa API

# Introduction
This is comprensihive guide on how to use mpessa payment gateway SDK in your appilication. M-PESA is a mobile money transfer service that allows users to send and receive money, pay bills, and shop cashlessly in Ethiopia 
# Usage
## USSD push Checkout
```
import asyncio
from mpessa.auth import Auth
from mpessa.api import Mpessa

async def main():
    # Initialize authentication and authenticate
    base_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"
    auth = Auth(base_url=base_url)
    try:
        await auth.authenticate()
        print("Authentication successful.")
    except Exception as e:
        print(f"Error during authentication: {e}")
        return

    # Initialize Mpessa
    mpessa = Mpessa(auth=auth)

    # Define the payload
    payload = {
            "BusinessShortCode": "174379",
            "Password": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
            "Timestamp": "20241212110954",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 500,
            "PartyA": 600992,
            "PartyB": 600000,
            "PartyB": 600000,
            "PhoneNumber": "251987892311",
            "TransactionDesc": "my demo description",
            "CallBackURL": "http://172.29.65.59:13345",
            "AccountReference": "myfbwehjfbhwe",
            "MerchantRequestID": "wefwefwr23",
            "ReferenceData": [{"Key":"BundleName","Value":"Monthly Unlimited Bundle"}],
    }

    # Perform USSD PUSH Checkout
    try:
        response = await mpessa.ussd_push_checkout(payload=payload)
        print("USSD PUSH Checkout successful:", response)
    except Exception as e:
        print(f"Error during USSD PUSH Checkout: {e}")
```

## Customer Initiated payment
```
import asyncio
from  mpessa.api  import Mpessa
from mpessa.auth import Auth

async def main():
    """
    Test for the customer_initiated_payment method in the Mpessa class.
    """
    # Initialize authentication and authenticate
    auth_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"
    auth = Auth(base_url=auth_url)  

    try:
        await auth.authenticate()
        print("Authentication successful.")
    except Exception as e:
        print(f"Error during authentication: {e}")
        return

    #initialize Mpessa
    mpessa = Mpessa(auth=auth)

    # Define the payload
    payload = {
        "CommandID": "CustomerPayBillOnline",
        "Amount":"11",
        "Msisdn":"251700100100",
        "BillRefNumber":"101010",
        "ShortCode":"101010",
    } 

    # Perform Customer Initiated Payment
    try:
        response = await mpessa.customer_initiated_payment(payload=payload)
        print("Customer Initiated Payment successful:", response)
    except Exception as e:
        print(f"Error during Customer Initiated Payment: {e}")

```

## Pay Out
```
import asyncio
from mpessa.auth import Auth
from mpessa.api import Mpessa

async def main():
    # Initialize authentication and authenticate
    base_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"
    auth = Auth(base_url=base_url)
    try:
        await auth.authenticate()
        print("Authentication successful.")
    except Exception as e:
        print(f"Error during authentication: {e}")
        return

    # Initialize Mpessa
    mpessa = Mpessa(auth=auth)

    # Define the payload
    payload = {
        "InitiatorName": "testapi",
        "SecurityCredential": "iSHJEgQYt3xidNVJ7lbXZqRXUlBqpM/ytL5incRQISaAYX/daObQopdHWiSVXJvexSoYCt9mmb6+TiikmTrGZm5fbaT1BeuPKDF9NFpOLG3n3hUZE2s5wNJvFxD3sM62cBdCQulFquFBc0CwHpq/K2cU1MN8lahvYp+vHnmGODogMBDk8/5Q+5CuRRFNRIt50xM0r10kUHVeWgUa71H6oK2RqXnog4EPTnanMlswz7N3J8jeIKzgGUwnJA8va5CvuNWu2B2L1cAm9g6pGribcgFZ2sgzByJpRWBkfntjGgzsYXh+K3fPZmxWyTQi7TscSvujH1EaS7JxvCIWMM3K0Q==",
        "Occassion": "Disbursement",
        "CommandID": "BusinessPayment",
        "PartyA": "101010",
        "PartyB": "251700100100",
        "Remarks": "Test B2C",
        "Amount": 12,
        "QueueTimeOutURL": "https://mydomain.com/b2c/timeout",
        "ResultURL": "https://mydomain.com/b2c/result"
    }

    # perform pay out
    try:
        response = await mpessa.pay_out(payload=payload)
        print("Pay out successful:", response)
    except Exception as e:
        print(f"Error during Pay out: {e}")

```
## Transaction Status 
```
import asyncio
from mpessa.auth import Auth
from mpessa.api import Mpessa

async def main():
    # Initialize authentication and authenticate
    auth_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"
    auth = Auth(base_url=auth_url)
    try:
        await auth.authenticate()
        print("Authentication successful.")
    except Exception as e:
        print(f"Error during authentication: {e}")
        return
    
    # Initialize Mpessa
    mpessa = Mpessa(auth=auth)

    # Define the payload
    payload = {
        "Initiator": "apitest",
        "SecurityCredential": "K2tH8KzkmIjCSEOAwgiI6T4ThpQT2DQa/rZfRc8+6iYA62vIsCUhhV0yxM84p0O/70aAiJ6EZwr/bE17Ww1VPMpzPwBadgf+dTwdz8LueZi4kUyZleoIYiJ3jNjkaXMT2g29JHJKRePbd4fsk+y38avf9zl5HG1N9UrpjaT2LhZOjmmPj4U1P/l3NP9C+AlcbAtHmtrkyIhvPrH4XwtDZasRcxUpPMbVcvajaBrcixIga8I4bvfBJfsnspSmpSDoTZ1f9glMYy1qRD83NX6R4/ToD0K0n7z0tKo35rJIn6a1bpVqKXuPmrkcK9ck0nAtmPQy8om6pwCmzDu+sG6slg==",
        "CommandID": "TransactionStatusQuery",
        "TransactionID": "RHJ4BTOYS8",
        "OriginalConversationID": "AG_20190826_0000777ab7d848b9e721",
        "PartyA": "101010",
        "IdentifierType": "4",
        "ResultURL": "https://mydomain.com/api/transaction-status/result",
        "QueueTimeOutURL": "https://mydomain.com/transaction-status/timeout",
        "Remarks": "OK",
        "Occasion": "OK"
    }

    # Perform Transaction Status request
    try:
        response = await mpessa.transaction_status(payload=payload)
        print("Transaction Status request successful:", response)
    except Exception as e:
        print(f"Error during Transaction Status request: {e}")    

```
## Transaction Reversal
```
import asyncio
from mpessa.auth import Auth
from mpessa.api import Mpessa

async def main():
    # Initialize authentication and authenticate
    base_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"
    auth = Auth(base_url=base_url)
    try:
        await auth.authenticate()
        print("Authentication successful.")
    except Exception as e:
        print(f"Error during authentication: {e}")
        return
    
    # Initialize Mpessa
    mpessa = Mpessa(auth=auth)

    # Define the payload
    payload = {
           "Initiator":"testapiuser",  
            "SecurityCredential":"dsam==",  
            "CommandID":"TransactionReversal",  
            "TransactionID":"A644545RED",  
            "Amount":"2000",  
            "ReceiverParty":"600610",  
            "RecieverIdentifierType":"4", 
            "ResultURL":"https://darajambili.herokuapp.com/b2c/result",  
            "QueueTimeOutURL":"https://darajambili.herokuapp.com/b2c/timeout",  
            "Remarks":"please",  
            "Occasion":"work"
    }

    # Perform Transaction Reversal request
    try:
        response = await mpessa.transaction_reversal(payload=payload)
        print("Transaction Reversal request successful:", response)
    except Exception as e:
        print(f"Error during Transaction Reversal request: {e}")
```
