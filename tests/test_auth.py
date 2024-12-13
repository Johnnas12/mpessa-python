import asyncio
from mpessa.auth import Auth

async def main():
    base_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"

    auth = Auth(base_url=base_url)
    try:
        result = await auth.authenticate()
        print("Authentication successful:", result)
    except Exception as e:
        print("Error during authentication:", str(e))

if __name__ == "__main__":
    asyncio.run(main())
