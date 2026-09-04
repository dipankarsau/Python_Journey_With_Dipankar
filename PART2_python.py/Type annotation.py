# ============================================
# Python Type Annotation
# ============================================

# Variable Type Annotation
name: str = "Dipankar"
age: int = 22
height: float = 5.8
is_student: bool = True


# Function Parameter Annotation
def add(a: int, b: int) -> int:
    return a + b


# String Function
def greet(name: str) -> str:
    return f"Hello, {name}"


# List Type Annotation
numbers: list[int] = [10, 20, 30, 40]
names: list[str] = ["Rahul", "Anirudh", "David"]


# Function with List
def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)


# Examples
print(add(10, 20))
print(greet(name))
print(calculate_total(numbers))