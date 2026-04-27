from typing import Optional


def safe_div(a: float, b: float) -> Optional[float]:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None


print(safe_div(10, 2))
print(safe_div(10, 0))

try:
    int("abc")
except ValueError as e:
    print("caught:", e)
finally:
    print("cleanup runs")
