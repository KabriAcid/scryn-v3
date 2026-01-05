from abc import ABC, abstractmethod


class TelcoProvider(ABC):
    @abstractmethod
    def credit_data(self, msisdn: str, data_gb: float) -> bool:
        pass
