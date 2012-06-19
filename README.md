simplest
========

Working with Redis should be simple and Pythonic.


Installation
------------

```
pip install simplest
```


Usage
-----

```python
>>> from simplest import Redis

>>> r = Redis(db="test")

>>> r['abc'] is None
True

>>> r['abc'] = 'xyz'

>>> r['abc']
'xyz'

>>> r['abc'] = (1, 2, 3)

>>> r['abc']
['1', '2', '3']

>>> r['abc'] = set([1, 2, 3])

>>> r['abc']
set([1, 2, 3])
```
