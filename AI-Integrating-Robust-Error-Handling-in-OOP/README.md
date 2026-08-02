# AI: Integrating Robust Error Handling in OOP

## Objective
Apply AI-driven scaffolding to enhance a Product/InventoryManager class
by integrating robust exception handling and data validation using
Python's `@property` decorators and a custom exception.

## Files
- `inventory_manager_initial.py` — the original, unvalidated starting code.
- `inventory_manager_refactored.py` — the AI-assisted refactored version,
  with `@property` validation on `price` and `quantity`, and a custom
  `InvalidProductDataError` exception.

## Test Case
```python
print("\n--- Testing Invalid Input ---")
try:
    manager.inventory[0].quantity = -5
except Exception as e:
    print(f"Test result: {e}")
```

Output:
