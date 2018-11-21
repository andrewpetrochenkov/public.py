#!/usr/bin/env python
import public


@public.add
class Cls():
    pass


assert __all__ == ["Cls"]


@public.add
def func(): pass


assert __all__ == ["Cls", "func"]


__all__ = []
public.add("name1", "name2")
assert __all__ == ["name1", "name2"]
