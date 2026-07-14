import importlib.util
import sys
import traceback
from pathlib import Path

# Ensure 'lib' is on sys.path so 'cash_register' can be imported
root = Path(__file__).parent
lib_dir = str(root / 'lib')
if lib_dir not in sys.path:
    sys.path.insert(0, lib_dir)

spec = importlib.util.spec_from_file_location("cash_register_test", str(root / 'lib' / 'testing' / 'cash_register_test.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TestClass = getattr(mod, 'TestCashRegister')

instance = TestClass()

failures = []

# Run test methods in class definition order to match pytest behavior
for name, value in TestClass.__dict__.items():
    if name.startswith('test_') and callable(value):
        func = getattr(instance, name)
        try:
            func()
            print(f"OK: {name}")
        except AssertionError:
            failures.append((name, traceback.format_exc()))
            print(f"FAIL: {name}")
        except Exception:
            failures.append((name, traceback.format_exc()))
            print(f"ERROR: {name}")

print('\nSummary:')
print(f"Ran {len([n for n in dir(instance) if n.startswith('test_')])} tests, {len(failures)} failures")
if failures:
    for name, tb in failures:
        print('---')
        print(name)
        print(tb)
