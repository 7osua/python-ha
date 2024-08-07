# link: https://www.pythontutorial.net/python-oop/python-overriding-method/


import re


class Parser:

    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(r"\d{3}-\d{3}-\d{4}", self.text)
        if match:
            return match.group()
        return None

    def parse(self):
        return {"email": self.email(), "phone": self.phone()}


class UkParser(Parser):

    def phone(self):
        match = re.search(r"(\+\d{1}-\d{3}-\d{3}-\d{4})", self.text)
        if match:
            return match.group(0)
        return None


if __name__ == "__main__":
    s = "Contact us via 408-205-5663 or email@test.com"
    parser = Parser(s)
    print(parser.parse())
    # [Output] {'email': 'email@test.com', 'phone': '408-205-5663'}

    s2 = "Contact me via +1-650-453-3456 or email@test.co.uk"
    parser = UkParser(s2)
    print(parser.parse())
    # [Output] {'email': 'email@test.co.uk', 'phone': '+1-650-453-3456'}
