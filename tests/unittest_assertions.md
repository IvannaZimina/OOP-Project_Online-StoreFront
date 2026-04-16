# unittest assertion methods used in this project

This note summarizes the unittest assertion methods used in tests/test_store.py.

## assertAlmostEqual(first, second, places=7, msg=None, delta=None)

Compares two numbers for approximate equality.

How it works:
- Computes the difference: abs(first - second).
- If delta is provided, the test passes when the difference <= delta.
- Otherwise, it rounds the difference to the given number of decimal places
  (default 7) and expects the rounded difference to be 0.

Typical use:
- Floating-point results where tiny rounding errors are normal.

Example:
- assertAlmostEqual(2.5 * 2.50, 6.25)

## assertEqual(first, second, msg=None)

Compares two values for exact equality using the == operator.

How it works:
- The test passes if first == second.
- Otherwise it fails and reports both values.

Typical use:
- Integers, strings, enums, or any values where exact match is expected.

Example:
- assertEqual(0.0, 0.0)

## assertRaises(expected_exception)

Checks that a block of code raises a specific exception.

How it works:
- Used as a context manager with the with statement.
- The test passes only if the specified exception is raised inside the block.

Typical use:
- Validating error handling and input validation.

Example:
- with assertRaises(ValueError):
  price = -1
