# Clean Code Practices in Python

This document outlines clean code practices and principles specifically for Python development. Following these practices will help maintain code readability, maintainability, and overall quality.

## 1. Naming Conventions

### Use Meaningful Names
```python
# Bad
def p(d):
    return d * 3.14

# Good
def calculate_circumference(diameter):
    return diameter * math.pi
```

### Follow Python Naming Conventions
- Use `snake_case` for variables, functions, and modules
- Use `PascalCase` for classes
- Use `UPPER_CASE` for constants
- Use single underscore prefix `_` for private attributes
- Use double underscore prefix `__` for name mangling

```python
# Good examples
MAX_RETRIES = 3
user_name = "john"
class UserManager:
    def __init__(self):
        self._internal_cache = {}
        self.__private_data = None
```

## 2. Functions

### Keep Functions Small and Focused
```python
# Bad: Function doing too many things
def process_user_data(user_data):
    # Validate data
    if not user_data.get('name'):
        raise ValueError("Name is required")
    if not user_data.get('email'):
        raise ValueError("Email is required")
    
    # Process data
    user_data['name'] = user_data['name'].strip()
    user_data['email'] = user_data['email'].lower()
    
    # Save to database
    db.save(user_data)
    
    # Send notification
    send_email(user_data['email'])

# Good: Split into focused functions
def validate_user_data(user_data):
    if not user_data.get('name'):
        raise ValueError("Name is required")
    if not user_data.get('email'):
        raise ValueError("Email is required")

def normalize_user_data(user_data):
    return {
        'name': user_data['name'].strip(),
        'email': user_data['email'].lower()
    }

def process_user_data(user_data):
    validate_user_data(user_data)
    normalized_data = normalize_user_data(user_data)
    db.save(normalized_data)
    send_email(normalized_data['email'])
```

### Use Type Hints
```python
# Bad: No type information
def process_data(data):
    return data * 2

# Good: With type hints
from typing import List, Dict, Optional

def process_data(data: List[int]) -> List[int]:
    return [x * 2 for x in data]

def get_user_info(user_id: int) -> Optional[Dict[str, str]]:
    # Implementation
    pass
```

## 3. Comments and Documentation

### Write Self-Documenting Code
```python
# Bad: Code needs comments to explain
# Check if user is active and has permission
if u.s and u.p:
    # Do something
    pass

# Good: Self-documenting code
if user.is_active and user.has_permission:
    process_user_request()
```

### Use Docstrings
```python
def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calculate the discounted price based on the original price and discount percentage.
    
    Args:
        price (float): The original price of the item
        discount_percentage (float): The discount percentage to apply (0-100)
        
    Returns:
        float: The final price after applying the discount
        
    Raises:
        ValueError: If discount_percentage is not between 0 and 100
    """
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    return price * (1 - discount_percentage / 100)
```

## 4. Error Handling

### Use Specific Exceptions
```python
# Bad: Using generic Exception
try:
    result = process_data(data)
except Exception:
    print("Something went wrong")

# Good: Using specific exceptions
try:
    result = process_data(data)
except ValueError as e:
    logger.error(f"Invalid data format: {e}")
except ConnectionError as e:
    logger.error(f"Network error: {e}")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise
```

## 5. Code Organization

### Use Context Managers
```python
# Bad: Manual resource management
file = open('data.txt', 'r')
try:
    data = file.read()
finally:
    file.close()

# Good: Using context manager
with open('data.txt', 'r') as file:
    data = file.read()
```

### Use List Comprehensions and Generator Expressions
```python
# Bad: Using loops for simple transformations
squares = []
for x in range(10):
    squares.append(x * x)

# Good: Using list comprehension
squares = [x * x for x in range(10)]

# For large datasets, use generator expressions
squares_gen = (x * x for x in range(1000000))
```

## 6. Testing

### Write Unit Tests
```python
# tests/test_calculator.py
import pytest
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0
```

## Best Practices Checklist

When writing or reviewing code, consider these questions:

1. **Readability**
   - Is the code easy to read and understand?
   - Are variable and function names descriptive?
   - Is the code properly formatted?

2. **Maintainability**
   - Is the code modular and well-organized?
   - Are functions small and focused?
   - Is there minimal code duplication?

3. **Reliability**
   - Are edge cases handled?
   - Is error handling appropriate?
   - Are there unit tests?

4. **Performance**
   - Are there any obvious performance bottlenecks?
   - Are appropriate data structures used?
   - Is memory usage optimized?

5. **Security**
   - Are input validations in place?
   - Are sensitive data handled properly?
   - Are there any potential security vulnerabilities?

Remember: Clean code is not just about making the code work, but about making it maintainable and understandable for other developers (including your future self). 