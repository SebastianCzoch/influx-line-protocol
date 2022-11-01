class Metric(object):
    def __init__(self, measurement):
        self.measurement = measurement
        self.values = {}
        self.tags = dict()
        self.timestamp = None

    def with_timestamp(self, timestamp):
        self.timestamp = timestamp

    def add_tag(self, name, value):
        self.tags[str(name)] = str(value)

    def add_value(self, name, value):
        self.values[str(name)] = value

    def __str__(self):
        # Escape measurement manually
        escaped_measurement = self.measurement.replace(",", "\\,")
        escaped_measurement = escaped_measurement.replace(" ", "\\ ")
        protocol = escaped_measurement

        # Create tag strings
        tags = []
        for key, value in self.tags.items():
            escaped_name = self.__escape(key)
            escaped_value = self.__escape(value)

            tags.append("%s=%s" % (escaped_name, escaped_value))

        # Concatenate tags to current line protocol
        if len(tags) > 0:
            protocol = "%s,%s" % (protocol, ",".join(tags))

        # Create field strings
        values = []
        for key, value in self.values.items():
            escaped_name = self.__escape(key)
            escaped_value = self.__parse_value(value)
            values.append("%s=%s" % (escaped_name, escaped_value))

        # Concatenate fields to current line protocol
        protocol = "%s %s" % (protocol, ",".join(values))

        if self.timestamp is not None:
            protocol = "%s %d" % (protocol, self.timestamp)

        return protocol

    def __escape(self, value):
        # Escape backslashes first since the other characters are escaped with
        # backslashes
        new_value = value.replace("\\", "\\\\")

        new_value = new_value.replace(" ", "\\ ")
        new_value = new_value.replace("=", "\\=")
        new_value = new_value.replace(",", "\\,")

        return new_value

    def __escape_value(self, value):
        new_value = value.replace("\\", "\\\\")
        new_value = new_value.replace('"', '\\"')

        return new_value

    def __parse_value(self, value):
        if type(value) is int:
            return "%di" % value

        if type(value) is float:
            return "%g" % value

        if type(value) is bool:
            return value and "t" or "f"

        return '"%s"' % self.__escape_value(value)
