from telco.base import TelcoProvider


class MockTelcoProvider(TelcoProvider):
    def credit_data(self, msisdn: str, data_gb: float) -> bool:
        # Simulates successful data credit
        return True
