def addition(a: int, b: int) -> int:
    return a + b

def subtraction(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def division(a: int, b: int) -> float:
    return a / b


PI = 3.14

if __name__ == "__main__":
    print(f"calculator file __name__ = {__name__}")
    result = addition(2, 3)
    print(result)

print("hello word")