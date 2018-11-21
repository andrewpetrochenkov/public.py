#!/usr/bin/env python
import sys
import public

__all__ = ["name"]


module = sys.modules[__name__]
try:
    public.test(module)
except ValueError as e:
    print(str(e))


@public.add
def name(): pass


public.test(module)
