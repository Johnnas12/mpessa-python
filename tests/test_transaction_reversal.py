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

if __name__ == "__main__":
    asyncio.run(main())