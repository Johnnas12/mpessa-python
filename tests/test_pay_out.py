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

if __name__ == "__main__":
    asyncio.run(main())





