from presidio_anonymizer.operators import Operator


class Initial(Operator):

    @staticmethod
    def operator_name():
        return "initial"

    @staticmethod
    def operator_type():
        return "Anonymize"

    def validate(self, params: dict = None):
        # No params required for minimal version
        pass

    def operate(self, text: str, params: dict = None):
        parts = text.split()
        initials = [p[0].upper() + "." for p in parts if p]
        return " ".join(initials)
