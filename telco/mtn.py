import requests
from telco.base import TelcoProvider


class MTNProvider(TelcoProvider):
    def credit_data(self, msisdn: str, data_gb: float) -> bool:
        payload = {
            "msisdn": msisdn,
            "data": data_gb
        }
        headers = {"Authorization": "Bearer YOUR_API_KEY"}

        response = requests.post(
            "https://api.mtn.example/data-credit",
            json=payload,
            headers=headers,
            timeout=10
        )

        return response.status_code == 200
