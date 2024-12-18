import httpx


class Mpessa:
    """
    Mpessa class for handling M-Pesa payment APIs.
    """

    def __init__(self, auth):
        """
        Initialize Mpessa class.

        :param auth: Auth object used for authentication.
        """
        self.auth = auth

    async def ussd_push_checkout(self, payload):
        """
        Perform a USSD PUSH Checkout asynchronously.

        :param payload: dict
            The data required to initiate a USSD PUSH Checkout.
        :return: dict
            Response from the API if successful.
        :raises Exception: If authentication token is missing or the request fails.
        """
        if not self.auth.access_token:
            raise Exception("No authentication token available. Please authenticate first.")

        url = "https://apisandbox.safaricom.et/mpesa/stkpush/v3/processrequest"
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"USSD PUSH Checkout failed: {response.status_code}, {response.text}")
            except httpx.RequestError as e:
                raise Exception(f"Network error occurred during USSD PUSH Checkout: {str(e)}")
            
    async def customer_initiated_payment(self, payload):
        """
        Perform a Customer Initiated Payment synchronously.

        :param payload: dict
            The data required to initiate the payment.
        :return: dict
            Response from the API if successful.
        :raises Exception: If authentication token is missing or the request fails.
        """
        if not self.auth.access_token:
            raise Exception("No authentication token available. Please authenticate first.")
        

        url = "https://apisandbox.safaricom.et/mpesa/b2c/simulatetransaction/v1/request"
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"Customer Initiated Payment failed: {response.status_code}, {response.text}")
            except httpx.RequestError as e:
                raise Exception(f"Network error occurred during Customer Initiated Payment: {str(e)}")
    

    async def pay_out(self, payload):
        """
        Perform a Pay Out transaction asynchronously.

        :param payload: dict
            The data required to initiate the payment.
        :return: dict
            Response from the API if successful.
        :raises Exception: If authentication token is missing or the request fails.
        """
        if not self.auth.access_token:
            raise Exception("No authentication token available. Please authenticate first.")

        url = "https://apisandbox.safaricom.et/mpesa/b2c/v2/paymentrequest"
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"Pay Out failed: {response.status_code}, {response.text}")
            except httpx.RequestError as e:
                raise Exception(f"Network error occurred during Pay Out: {str(e)}")
            

    async def transaction_status(self, payload):
        """
        Check the status of a transaction asynchronously.

        :param payload: dict
            The data required to request transaction status.
        :return: dict
            Response from the API if successful.  
        :raises Exception: If authentication token is missing or the request fails.
        """
        if not self.auth.access_token:
            raise Exception("No authentication token available. Please authenticate first.")

        url = "https://apisandbox.safaricom.et/mpesa/transactionstatus/v1/query"
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"Transaction Status failed: {response.status_code}, {response.text}")
            except httpx.RequestError as e:
                raise Exception(f"Network error occurred during Transaction Status: {str(e)}")
            

    async def account_balance(self, payload):
        """
        Check the account balance asynchronously.

        :param payload: dict
            The data required to request account balance.
        :return: dict
            Response from the API if successful.
        :raises Exception: If authentication token is missing or the request fails.
        """
        if not self.auth.access_token:
            raise Exception("No authentication token available. Please authenticate first.")

        url = "https://apisandbox.safaricom.et/mpesa/accountbalance/v2/query"
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"Account Balance request failed: {response.status_code}, {response.text}")
            except httpx.RequestError as e:
                raise Exception(f"Network error occurred during Account Balance request: {str(e)}")
            

    async def transaction_reversal(self, payload):
        """
        Reverse a transaction asynchronously.

        :param payload: dict
            The data required to reverse a transaction.
        :return: dict
            Response from the API if successful.
        :raises Exception: If authentication token is missing or the request fails.
        """
        if not self.auth.access_token:
            raise Exception("No authentication token available. Please authenticate first.")

        url = "https://apisandbox.safaricom.et/mpesa/reversal/v2/request"
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"Transaction Reversal failed: {response.status_code}, {response.text}")
            except httpx.RequestError as e:
                raise Exception(f"Network error occurred during Transaction Reversal: {str(e)}")