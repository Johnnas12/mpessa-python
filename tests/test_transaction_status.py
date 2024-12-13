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

if __name__ == "__main__":
    asyncio.run(main())
    
