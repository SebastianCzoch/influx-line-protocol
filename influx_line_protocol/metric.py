class Metric(object):

    def __init__(self, measurement):
        self.measurement = measurement
        self.values = {}
        self.tags = dict()
        self.timestamp = None

    def with_timestamp(self, timestamp):
        self.timestamp = timestamp

    def add_tag(self, name, value):
        if ' ' in str(value):
            value = value.replace(' ', '\\ ')
        self.tags[name] = value

    def add_value(self, name, value):
        self.values[name] = self.__parse_value(value)

    def __str__(self):
        protocol = self.measurement
        tags = ["%s=%s" % (key.replace(' ', '\\ '), self.tags[key]) for key in self.tags]
        if len(tags) > 0:
            protocol = "%s,%s" % (protocol, ",".join(tags))

        values = ["%s=%s" % (key, self.values[key]) for key in self.values]
        protocol = "%s %s" % (protocol, ",".join(values))

        if self.timestamp is not None:
            protocol = "%s %d" % (protocol, self.timestamp)

        return protocol

    def __parse_value(self, value):
        if type(value).__name__ == 'int':
            return "%di" % value

        if type(value).__name__ == 'float':
            return "%g" % value

        if type(value).__name__ == 'bool':
            return value and "t" or "f"

        return "\"%s\"" % value
