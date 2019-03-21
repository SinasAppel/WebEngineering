class CarrierCodeConverter:
    regex = '[A-Z]{2}'

    def __init__(self):
        pass

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return '%02d' % value


class AirportCodeConverter:
    regex = '[A-Z]{3}'

    def __init__(self):
        pass

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return '%03d' % value
