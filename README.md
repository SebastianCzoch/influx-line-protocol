[![Build Status](https://travis-ci.org/SebastianCzoch/influx-line-protocol.svg?branch=master)](https://travis-ci.org/SebastianCzoch/influx-line-protocol/branches) [![PyPI version](https://badge.fury.io/py/influx-line-protocol.svg)](https://badge.fury.io/py/influx-line-protocol) [![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/SebastianCzoch/influx-line-protocol/blob/master/LICENSE)
# influx-line-protocol
Implementation of influxdata line protocol format in python

## Installation
```bash
$ pip install influx_line_protocol
```

## Usage
```python
from influx_line_protocol import Metric

metric = Metric("weather")
metric.with_timestamp(1465839830100400200)
metric.add_tag('location', 'Cracow')
metric.add_value('temperature', '29')

print metric
"""
  Will print:
  weather,location=Cracow temperature=29 1465839830100400200
"""
```

Multiple metrics example
```python
from influx_line_protocol import Metric, MetricCollection

collection = MetricCollection()
metric = Metric("weather")
metric.with_timestamp(1465839830100400200)
metric.add_tag('location', 'Cracow')
metric.add_value('temperature', '29')
collection.append(metric)

metric = Metric("weather")
metric.with_timestamp(1465839830100400200)
metric.add_tag('location', 'Nowy Sacz')
metric.add_value('temperature', '31')
collection.append(metric)

print collection
"""
  Will print
  weather,location="Cracow" temperature=29 1465839830100400200
  weather,location="Nowy Sacz" temperature=29 1465839830100400200
"""
```

## License
See [LICENSE](https://github.com/SebastianCzoch/influx-line-protocol/blob/master/LICENSE) file.
