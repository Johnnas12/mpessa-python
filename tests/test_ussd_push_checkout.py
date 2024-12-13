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

if __name__ == "__main__":
    asyncio.run(main())
