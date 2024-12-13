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

if __name__ == "__main__":
    asyncio.run(main())
