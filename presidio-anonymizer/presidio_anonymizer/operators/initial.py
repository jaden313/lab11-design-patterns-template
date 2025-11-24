from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def operate(self, text: str, params: dict = None) -> str:

        words = text.strip().split()
        initials = []
        for w in words:
            for ch in w:
                if ch.isalnum():
                    initials.append(ch.upper() + ".")
                    break
        return " ".join(initials)
