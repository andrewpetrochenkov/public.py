<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/public.svg?maxAge=3600)](https://pypi.org/project/public/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/public.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/public.py/actions)

### Installation
```bash
$ [sudo] pip install public
```

#### Features
+   replace [`__all__`](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python) with `@public.add` decorator


before
```python
__all__ = ["func"]

def func():
```

after
```python
import public

@public.add
def func():
```

#### Examples
```python
>>> import public
>>> @public.add
    def func(): pass

>>> @public.add
    class Cls: pass

>>> __all__
['Cls','func']

>>> public.add("name")
>>> public.add(*["name1","name2"])

>>> __all__
['Cls','func','name','name1','name2']
```

#### Links
+   [Importing * From a Package. Python documentation](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package)
+   [Can someone explain __all__ in Python? Stackoverflow](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>