class MetricCollection(object):
    def __init__(self):
        self.metrics = []

    def append(self, metric):
        self.metrics.append(metric)

    def __str__(self):
        return "\n".join(str(m) for m in self.metrics)
