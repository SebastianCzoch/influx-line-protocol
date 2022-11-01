import unittest
from .metric import Metric
from .metric_collection import MetricCollection


class TestMetricCollection(unittest.TestCase):
    def test_empty_collection(self):
        collection = MetricCollection()

        self.assertEqual("", str(collection))

    def test_collection_with_one_metric(self):
        metric = Metric("test")
        metric.add_tag("a", 1)
        metric.add_value("b", 2)

        collection = MetricCollection()
        collection.append(metric)

        self.assertEqual("test,a=1 b=2i", str(collection))

    def test_collection_with_multiple_metrics(self):
        metric = Metric("test")
        metric.add_tag("a", 1)
        metric.add_value("b", 2)

        metric2 = Metric("test2")
        metric2.add_tag("c", 3)
        metric2.add_value("d", 4)

        collection = MetricCollection()
        collection.append(metric)
        collection.append(metric2)
        collection.append(metric)
        collection.append(metric2)

        self.assertEqual(
            "test,a=1 b=2i\ntest2,c=3 d=4i\ntest,a=1 b=2i\ntest2,c=3 d=4i",
            str(collection),
        )
