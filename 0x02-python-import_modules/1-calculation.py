#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    add_result = add(a, b)
    print(f"Add: {add_result}")

    sub_result = sub(a, b)
    print(f"Sub: {sub_result}")

    mul_result = mul(a, b)
    print(f"Mul: {mul_result}")

    div_result = div(a, b)
    print(f"Div: {div_result}")
