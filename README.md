[![](https://img.shields.io/pypi/pyversions/public.svg?longCache=True)](https://pypi.org/pypi/public/)
[![](https://img.shields.io/pypi/v/public.svg?maxAge=3600)](https://pypi.org/pypi/public/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/public.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/public.py/)

#### Install
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

#### Functions
function|description
-|-
`public.add(*objects)`|add objects to `__all__`
`public.public(*objects)`|add objects to `__all__`. deprecated
`public.test(module)`|test module `__all__`

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>