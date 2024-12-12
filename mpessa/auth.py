import os
from dotenv import load_dotenv
import httpx

# Load environment variables from .env file
load_dotenv()
basic_access_token = os.getenv("ACCESS_TOKEN")


class Auth:
    def __init__(self, base_url: str):
        """
        Initialize the Auth class.
        :param base_url: The base URL for the authentication endpoint.
        """
        self.base_url = base_url
        self.access_token = None

    def authenticate(self):
        """
        Perform authentication and retrieve an access token.
        :return: A dictionary with authentication details.
        """
        headers = {
            "Authorization": f"Basic {basic_access_token}"
        }
        
        try:
            # Use httpx to make the request
            with httpx.Client() as client:
                response = client.get(self.base_url, headers=headers)

            # Check for successful response
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get("access_token")
                return data
            else:
                raise Exception(f"Authentication failed: {response.status_code}, {response.text}")

        except httpx.RequestError as e:
            raise Exception(f"Network error occurred: {str(e)}")
