import asyncio
from mpessa.auth import Auth
from mpessa.api import Mpessa

async def main():
    #initialize authentication and authenticate
    base_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"
    auth = Auth(base_url=base_url)
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
        "Initiator": "testapi",
        "SecurityCredential": "K2tH8KzkmIjCSEOAwgiI6T4ThpQT2DQa/rZfRc8+6iYA62vIsCUhhV0yxM84p0O/70aAiJ6EZwr/bE17Ww1VPMpzPwBadgf+dTwdz8LueZi4kUyZleoIYiJ3jNjkaXMT2g29JHJKRePbd4fsk+y38avf9zl5HG1N9UrpjaT2LhZOjmmPj4U1P/l3NP9C+AlcbAtHmtrkyIhvPrH4XwtDZasRcxUpPMbVcvajaBrcixIga8I4bvfBJfsnspSmpSDoTZ1f9glMYy1qRD83NX6R4/ToD0K0n7z0tKo35rJIn6a1bpVqKXuPmrkcK9ck0nAtmPQy8om6pwCmzDu+sG6slg==",
        "CommandID": "AccountBalance",
        "PartyA": "101010",
        "IdentifierType": "4",
        "Remarks": "remark",
        "ResultURL": "https://mydomain.com/api/account-balance/result",
        "QueueTimeOutURL": "https://mydomain.com/account-balance/timeout"
    }

    # Perform Account Balance request
    try:
        response = await mpessa.account_balance(payload=payload)
        print("Account Balance request successful:", response)
    except Exception as e:
        print(f"Error during Account Balance request: {e}")

if __name__ == "__main__":
    asyncio.run(main())
