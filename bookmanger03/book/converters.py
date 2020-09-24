from django.urls import register_converter


class mobile:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return str(value)

register_converter(mobile, 'phone')
