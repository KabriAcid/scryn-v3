class USSDHandler:
    def __init__(self, redemption_service):
        self.redemption_service = redemption_service

    def handle(self, text: str, msisdn: str) -> str:
        try:
            pin = self._extract_pin(text)
        except ValueError:
            return "Invalid input format."

        return self.redemption_service.redeem(pin, msisdn)

    @staticmethod
    def _extract_pin(text: str) -> str:
        if "*" not in text:
            raise ValueError
        return text.split("*")[-1]
