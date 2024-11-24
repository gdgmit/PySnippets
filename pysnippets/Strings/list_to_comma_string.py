# list_to_comma_string.py

from typing import List, Any

def list_to_comma_string(items: List[Any]) -> str:
    """
    Convert a list of items into a comma-separated string.

    Args:
        items (List[Any]): List of items to convert.

    Returns:
        str: A single comma-separated string.

    Example:
        >>> list_to_comma_string(['apple', 'banana', 'cherry'])
        'apple, banana, cherry'
    """
    return ", ".join(str(item) for item in items)

# Example usage
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry", 42, True]
    result = list_to_comma_string(my_list)
    print(result)
