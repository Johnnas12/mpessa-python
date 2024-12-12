from mpessa.auth import Auth

def main():
    base_url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"  # Replace with the actual endpoint
    auth = Auth(base_url=base_url)

    try:
        result = auth.authenticate()
        print("Authentication successful:", result)
    except Exception as e:
        print("Error during authentication:", e)

if __name__ == "__main__":
    main()
