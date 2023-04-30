import re


class Validator:
    @classmethod
    def persian_text(cls, text, length=20):
        if len(text) <= 20:
            persian_pattern = r'^[\u0600-\u06FF0-9\s]+$'
            english_pattern = r'^[a-zA-Z0-9\s]+$'
            return bool(re.match(persian_pattern, text)) or bool(re.match(english_pattern, text))
        else:
            return None

    @classmethod
    def national_code(cls, national_code, sep="-"):
        result = re.match("^\d{3}-?\d{6}-?\d{1}$", national_code)
        # year = re.match("^\d{4}")
        # month = re.match("")
        # print(year,month,day)
        if result:
            return result.string.replace("-", sep)
        else:
            return None

    @classmethod
    def zero_positive(cls, number):
        if number >= 0:
            return number
        else:
            return None

    @classmethod
    def email(cls, email):
        result = list(re.finditer("^[\w\.]*@[\w\.]*[gmail|yahoo]\.com$", email))
        if result:
            return result[0].string
        else:
            return None

    @classmethod
    def address(cls, address_string):
        result = list(re.finditer("^[\w\-\s]*$", address_string))
        if result:
            return result[0].string
        else:
            return None

    @classmethod
    def date(cls, date):
        result = list(re.finditer("^\d{4}-\d{2}-\d{2}$", date))
        if result:
            return result[0].string
        else:
            return None
