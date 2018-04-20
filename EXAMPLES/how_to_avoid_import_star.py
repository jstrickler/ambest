#!/usr/bin/env python
import sys

import electrical as elec # <1>
import navigation as nav  # <2>

print(elec.current()) # <3>
print(nav.current())  # <4>

for path in sys.path:
    print(path)
