#!/usr/bin/env python3

import sys
from pathlib import Path

# Add parent directory to path so 'cash_register' can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))