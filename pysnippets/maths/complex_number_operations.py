# complex_number_operations.py

def add_complex(c1, c2):
    """
    Add two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The sum of the two complex numbers as (real, imag).

    Example:
        >>> add_complex((1, 2), (3, 4))
        (4, 6)
    """
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    return (real, imag)

def subtract_complex(c1, c2):
    """
    Subtract the second complex number from the first.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The difference of the two complex numbers as (real, imag).

    Example:
        >>> subtract_complex((5, 7), (2, 3))
        (3, 4)
    """
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    return (real, imag)

def multiply_complex(c1, c2):
    """
    Multiply two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The product of the two complex numbers as (real, imag).

    Example:
        >>> multiply_complex((1, 2), (3, 4))
        (-5, 10)
    """
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imag)


import math

def normalize_complex(c):
    """Normalize a complex number to have a magnitude of 1."""
    # Args: c (tuple): The complex number (real, imag).
    # Returns: tuple: A unit vector with the same direction, or (0, 0) if the input is (0, 0).
    real, imag = c
    magnitude = math.sqrt(real**2 + imag**2)
    if magnitude == 0:
        return (0, 0)
    return (real / magnitude, imag / magnitude)

def conjugate_complex(c):
    """Return the conjugate of a complex number."""
    # Args: c (tuple): The complex number (real, imag).
    # Returns: tuple: The conjugate (real, -imag).
    real, imag = c
    return (real, -imag)

def reciprocal_complex(c):
    """Return the reciprocal of a complex number."""
    # Args: c (tuple): The complex number (real, imag).
    # Returns: tuple: The reciprocal.
    # Raises: ZeroDivisionError if the input is (0, 0).
    real, imag = c
    if real == 0 and imag == 0:
        raise ZeroDivisionError("Reciprocal of zero is undefined.")
    magnitude_squared = real**2 + imag**2
    return (real / magnitude_squared, -imag / magnitude_squared)

def magnitude_complex(c):
    """Calculate the magnitude of a complex number."""
    # Args: c (tuple): The complex number (real, imag).
    # Returns: float: The magnitude of the number.
    real, imag = c
    return math.sqrt(real**2 + imag**2)

def phase_complex(c):
    """Calculate the phase angle of a complex number."""
    # Args: c (tuple): The complex number (real, imag).
    # Returns: float: The phase angle in radians.
    real, imag = c
    return math.atan2(imag, real)

def nth_roots_complex(c, n):
    """Find the nth roots of a complex number."""
    # Args: c (tuple): The complex number (real, imag).
    # n (int): The root degree.
    # Returns: list: A list of tuples representing the nth roots.
    roots = []
    real, imag = c
    magnitude = math.sqrt(real**2 + imag**2) ** (1 / n)
    theta = math.atan2(imag, real)
    for k in range(n):
        angle = (theta + 2 * math.pi * k) / n
        roots.append((magnitude * math.cos(angle), magnitude * math.sin(angle)))
    return roots

def rotate_complex(c, theta, degrees=False):
    """Rotate a complex number by a given angle."""
    # Args: c (tuple): The complex number (real, imag).
    # theta (float): The angle in radians or degrees.
    # degrees (bool): If True, interpret theta in degrees.
    # Returns: tuple: The rotated complex number.
    real, imag = c
    if degrees:
        theta = math.radians(theta)
    magnitude = math.sqrt(real**2 + imag**2)
    new_angle = math.atan2(imag, real) + theta
    return (magnitude * math.cos(new_angle), magnitude * math.sin(new_angle))

def is_conjugate(c1, c2):
    """Check if two complex numbers are conjugates."""
    # Args: c1, c2 (tuple): The complex numbers (real, imag).
    # Returns: bool: True if the numbers are conjugates, False otherwise.
    real1, imag1 = c1
    real2, imag2 = c2
    return real1 == real2 and imag1 == -imag2

# Example usage
if __name__ == "__main__":
    # Example usage of the functions
    c1 = (1, 2)  # 1 + 2i
    c2 = (3, 4)  # 3 + 4i

    sum_result = add_complex(c1, c2)
    print("Sum:", sum_result)

    difference_result = subtract_complex(c1, c2)
    print("Difference:", difference_result)

    product_result = multiply_complex(c1, c2)
    print("Product:", product_result)

    print("Normalize:", normalize_complex(c1))

    print("Conjugate:", conjugate_complex(c1))
    
    print("Reciprocal:", reciprocal_complex(c1))
    
    print("Magnitude:", magnitude_complex(c1))
    
    print("Phase:", phase_complex(c1))
    
    print("Nth roots:", nth_roots_complex((1, 0), 3))
    
    print("Rotate by 90 degrees:", rotate_complex(c1, 90, degrees=True))
    
    print("Are conjugates:", is_conjugate(c1, c2))

