import unittest
from .metric import Metric


class TestMetric(unittest.TestCase):

    def test_metric_without_tags_values_and_timestamp(self):
        metric = Metric("test")

        self.assertEqual("test ", str(metric))

    def test_metric_without_values_and_timestamp(self):
        metric = Metric("test")
        metric.add_tag("tag1", "string")

        self.assertEqual("test,tag1=string ", str(metric))

    def test_metric_with_tag_string_space_without_values_and_timestamp(self):
        metric = Metric("test")
        metric.add_tag("tag name", "string with space")

        self.assertEqual("test,tag\\ name=string\\ with\\ space ", str(metric))

    def test_metric_with_tag_value_and_timestamp(self):
        metric = Metric("test")
        metric.add_tag("tag", "string")
        metric.add_value("value", "string")
        metric.with_timestamp(687744000)

        self.assertEqual(
            "test,tag=string value=\"string\" 687744000", str(metric))

    def test_metric_multiple_tags_without_values_and_timestamp(self):
        metric = Metric("test")
        metric.add_tag("tag1", "string1")
        metric.add_tag("tag2", 1)
        metric.add_tag("tag3", 0.25)

        self.assertIn("tag1=string1", str(metric))
        self.assertIn("tag2=1", str(metric))
        self.assertIn("tag3=0.25", str(metric))
        self.assertIn("test,tag", str(metric))

    def test_metric_without_tags_and_timestamp(self):
        metric = Metric("test")
        metric.add_value("foo", "bar")

        self.assertEqual("test foo=\"bar\"", str(metric))

    def test_metric_multiple_values_without_tags_and_timestamp(self):
        metric = Metric("test")
        metric.add_value("value1", "string1")
        metric.add_value("value2", 1)
        metric.add_value("value3", 0.25)
        metric.add_value("value4", True)
        metric.add_value("value5", False)

        self.assertIn("value1=\"string1\"", str(metric))
        self.assertIn("value2=1", str(metric))
        self.assertIn("value3=0.25", str(metric))
        self.assertIn("value4=t", str(metric))
        self.assertIn("value5=f", str(metric))
        self.assertIn("test value", str(metric))

    def test_metric_multiple_values_tags_and_timestamp(self):
        metric = Metric("test")
        metric.add_value("value1", "string1")
        metric.add_value("value2", 1)
        metric.add_value("value3", 0.25)
        metric.add_value("value4", True)
        metric.add_value("value5", False)
        metric.add_tag("tag1", "string1")
        metric.add_tag("tag2", 1)
        metric.add_tag("tag3", 0.25)
        metric.with_timestamp(687744000)

        self.assertIn("tag1=string1", str(metric))
        self.assertIn("tag2=1", str(metric))
        self.assertIn("tag3=0.25", str(metric))
        self.assertIn("value1=\"string1\"", str(metric))
        self.assertIn("value2=1", str(metric))
        self.assertIn("value3=0.25", str(metric))
        self.assertIn("value4=t", str(metric))
        self.assertIn("value5=f", str(metric))
        self.assertIn("test,tag", str(metric))
        self.assertIn(" value", str(metric))
        self.assertIn(" 687744000", str(metric))
