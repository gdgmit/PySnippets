# Mathematics - PySnippets

Wellcome To PySnippet's Mathematics Module Section, This Section Contains The Documatation Of Each And Every Function That Is Available In The Mathematics Module.

## Table of Contents

- [Introduction](#introduction)
- [Matrix Operations](#matrix-operations)
  - [Matrix Inverse](#matrix-inverse)
  - [Matrix Addition](#matrix-addition)
  - [Matrix Transpose](#matrix-transpose)
  - [Matrix Multiplication](#matrix-multiplication)
  - [Matrix Scalar Multiplication](#matrix-scalar-multiplication)
- [Determinant](#determinant)
  - [Determinant](#determinant-of-a-matrix)
  - [Minor](#minor)
  - [Cofactor](#cofactor)
  - [Adjugate](#adjugate)
- [Complex Numbers](#complex-numbers)
  - [Complex Addition](#complex-addition)
  - [Complex Conjugate](#complex-conjugate)
  - [Normalize Complex Number](#normalize-complex-number)
  - [Conjugate Complex Number](#conjugate-complex-number)
  - [Reciprocal of a Complex Number](#reciprocal-of-a-complex-number)
  - [Magnitude of a Complex Number](#magnitude-of-a-complex-number)
  - [Phase of a Complex Number](#phase-of-a-complex-number)
  - [Nth Roots of a Complex Number](#nth-roots-of-a-complex-number)
  - [Rotate a Complex Number](#rotate-a-complex-number)
- [Complex Form Conversion](#complex-form-conversion)
  - [Polar to Rectangular](#polar-to-rectangular)
  - [Rectangular to Polar](#rectangular-to-polar)
  - [Bulk Polar to Rectangular](#bulk-polar-to-rectangular)
  - [Bulk Rectangular to Polar](#bulk-rectangular-to-polar)
  - [Cylindrical to Rectangular](#cylindrical-to-rectangular)
  - [Rectangular to Cylindrical](#rectangular-to-cylindrical)
  - [Polar to Complex](#polar-to-complex)
  - [Complex to Polar](#complex-to-polar)

---

## Introduction

The **Mathematics Module** simplifies the handling of matrix operations and complex numbers. It is designed to be easy to use with clean syntax and built-in error handling for invalid inputs.

---

## Matrix Operations

### Matrix Inverse

Calculates the inverse of a square matrix.

```python
matrix_inverse(matrix)
```

- **Args**: A square matrix `matrix`.
- **Returns**: The inverse of the matrix.
- **Example**:
  ```python
  >>> matrix_inverse([[1, 2], [3, 4]])
  [[-2.0, 1.0], [1.5, -0.5]]
  ```

### Matrix Addition

Performs element-wise addition of two matrices.

```python
matrix_addition(matrix_a, matrix_b)
```

- **Args**: Two matrices `matrix_a` and `matrix_b`.
- **Returns**: The resulting matrix after addition.
- **Example**:
  ```python
  >>> matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]])
  [[6, 8], [10, 12]]
  ```

### Matrix Multiplication

Multiplies two matrices using matrix multiplication rules.

```python
matrix_multiplication(matrix_a, matrix_b)
```

- **Args**: Two matrices `matrix_a` and `matrix_b`.
- **Returns**: The product matrix.
- **Example**:
  ```python
  >>> matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]])
  [[19, 22], [43, 50]]
  ```

### Matrix Transpose

Calculates the transpose of a given matrix.

```python
transpose(matrix)
```

- **Args**: A matrix `matrix`.
- **Returns**: The transposed matrix.
- **Example**:
  ```python
  >>> matrix_transpose([[1, 2], [3, 4]])
  [[1, 3], [2, 4]]
  ```

### Matrix Scalar Multiplication

Multiplies a matrix by a scalar value.

```python
matrix_scalar_multiplication(matrix, scalar)
```

- **Args**: A matrix `matrix` and a scalar value `scalar`.
- **Returns**: The resulting matrix after scalar multiplication.
- **Example**:
  ```python
  >>> matrix_scalar_multiplication([[1, 2], [3, 4]], 2)
  [[2, 4], [6, 8]]
  ```

---

## Determinant

### Determinant of a Matrix

Calculates the determinant of a square matrix.

```python
determinant(matrix)
```

- **Args**: A square matrix `matrix`.
- **Returns**: The determinant of the matrix.
- **Example**:
  ```python
  >>> determinant([[1, 2], [3, 4]])
  -2
  ```

### Minor

Calculates the minor of a matrix element.

```python
minor(matrix, row, col)
```

- **Args**: A matrix `matrix`, row index `row`, and column index `col`.
- **Returns**: The minor of the element at the specified row and column.
- **Example**:
  ```python
  >>> minor([[1, 2], [3, 4]], 0, 0)
  4
  ```

### Cofactor

Calculates the cofactor of a matrix element.

```python
cofactor(matrix, row, col)
```

- **Args**: A matrix `matrix`, row index `row`, and column index `col`.
- **Returns**: The cofactor of the element at the specified row and column.
- **Example**:
  ```python
  >>> cofactor([[1, 2], [3, 4]], 0, 0)
  4
  ```

### Adjugate

Calculates the adjugate of a matrix.

```python
adjugate(matrix)
```

- **Args**: A matrix `matrix`.
- **Returns**: The adjugate matrix, which is the transpose of the cofactor matrix of the given input square matrix.
- **Example**:
  ```python
  >>> adjugate([1, 2, 3], [0, 1, 4], [5, 6, 0])
  [[-24, 12, -2], [20, -15, 3], [-5, 4, -1]]
  ```

---

## Complex Numbers

### Complex Addition

Adds two complex numbers.

```python
complex_addition(complex_a, complex_b)
```

- **Args**: Two complex numbers `complex_a` and `complex_b`.
- **Returns**: The sum of the complex numbers.
- **Example**:
  ```python
  >>> complex_addition(1 + 2j, 3 + 4j)
  (4+6j)
  ```

### Complex Conjugate

Finds the conjugate of a complex number.

```python
complex_conjugate(complex_number)
```

- **Args**: A complex number `complex_number`.
- **Returns**: The conjugate of the complex number.
- **Example**:
  ```python
  >>> complex_conjugate(3 + 4j)
  (3-4j)
  ```
### Normalize Complex Number

Normalizes a complex number to have a magnitude of 1.

```python
normalize_complex(c)
```

- **Args**: 
  - `c` (tuple): The complex number (real, imag).
- **Returns**: 
  - tuple: A unit vector with the same direction, or `(0, 0)` if the input is `(0, 0)`.
- **Example**:
```python
>>> normalize_complex((3, 4))
(0.6, 0.8)
```

---

### Conjugate Complex Number

Returns the conjugate of a complex number.

```python
conjugate_complex(c)
```

- **Args**: 
  - `c` (tuple): The complex number (real, imag).
- **Returns**: 
  - tuple: The conjugate `(real, -imag)`.
- **Example**:
```python
>>> conjugate_complex((3, 4))
(3, -4)
```

---

### Reciprocal of a Complex Number

Returns the reciprocal of a complex number.

```python
reciprocal_complex(c)
```

- **Args**: 
  - `c` (tuple): The complex number (real, imag).
- **Returns**: 
  - tuple: The reciprocal of the complex number.
- **Raises**: 
  - `ZeroDivisionError` if the input is `(0, 0)`.
- **Example**:
```python
>>> reciprocal_complex((3, 4))
(0.12, -0.16)
```

---

### Magnitude of a Complex Number

Calculates the magnitude of a complex number.

```python
magnitude_complex(c)
```

- **Args**: 
  - `c` (tuple): The complex number (real, imag).
- **Returns**: 
  - float: The magnitude of the number.
- **Example**:
```python
>>> magnitude_complex((3, 4))
5.0
```

---

### Phase of a Complex Number

Calculates the phase angle of a complex number.

```python
phase_complex(c)
```

- **Args**: 
  - `c` (tuple): The complex number (real, imag).
- **Returns**: 
  - float: The phase angle in radians.
- **Example**:
```python
>>> phase_complex((3, 4))
0.9272952180016122
```

---

### Nth Roots of a Complex Number

Finds the nth roots of a complex number.

```python
nth_roots_complex(c, n)
```

- **Args**: 
  - `c` (tuple): The complex number (real, imag).
  - `n` (int): The root degree.
- **Returns**: 
  - list: A list of tuples representing the nth roots.
- **Example**:
```python
>>> nth_roots_complex((1, 0), 3)
[(1.0, 0.0), (-0.5, 0.8660254037844386), (-0.5, -0.8660254037844386)]
```

---

### Rotate a Complex Number

Rotates a complex number by a given angle.

```python
rotate_complex(c, theta, degrees=False)
```

- **Args**: 
  - `c` (tuple): The complex number (real, imag).
  - `theta` (float): The angle in radians or degrees.
  - `degrees` (bool): If `True`, interpret theta in degrees.
- **Returns**: 
  - tuple: The rotated complex number.
- **Example**:
```python
>>> rotate_complex((1, 2), 90, degrees=True)
(-2.0, 1.0)
```

---

## Complex Form Conversion

### Polar to Rectangular

Converts polar coordinates to rectangular coordinates.

```python
polar_to_rectangular(r, theta, degrees=False)
```

- **Args**:
  - `r` (float): The radial distance from the origin.
  - `theta` (float): The angle in radians (or degrees if `degrees=True`).
  - `degrees` (bool): Whether the angle is in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Rectangular coordinates as `(x, y)`.

- **Example**:
  ```python
  >>> polar_to_rectangular(5, 45, degrees=True)
  (3.5355339059327378, 3.5355339059327373)
  ```

---

### Rectangular to Polar

Converts rectangular coordinates to polar coordinates.

```python
rectangular_to_polar(x, y, degrees=False)
```

- **Args**:
  - `x` (float): The x-coordinate.
  - `y` (float): The y-coordinate.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Polar coordinates as `(r, theta)`.

- **Example**:
  ```python
  >>> rectangular_to_polar(3, 4)
  (5.0, 0.9272952180016122)
  ```

---

### Bulk Polar to Rectangular

Converts a list of polar coordinates to rectangular coordinates.

```python
bulk_polar_to_rectangular(polar_list, degrees=False)
```

- **Args**:
  - `polar_list` (list): List of tuples containing polar coordinates `(r, theta)`.
  - `degrees` (bool): Whether the angles are in degrees. Defaults to `False`.

- **Returns**:
  - `list`: List of rectangular coordinates.

- **Example**:
  ```python
  >>> bulk_polar_to_rectangular([(5, 45), (10, 30)], degrees=True)
  [(3.5355339059327378, 3.5355339059327373), (8.660254037844386, 4.999999999999999)]
  ```

---

### Bulk Rectangular to Polar

Converts a list of rectangular coordinates to polar coordinates.

```python
bulk_rectangular_to_polar(rectangular_list, degrees=False)
```

- **Args**:
  - `rectangular_list` (list): List of tuples containing rectangular coordinates `(x, y)`.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `list`: List of polar coordinates.

- **Example**:
  ```python
  >>> bulk_rectangular_to_polar([(3, 4), (5, 12)])
  [(5.0, 0.9272952180016122), (13.0, 1.176005207095135)]
  ```

---

### Cylindrical to Rectangular

Converts cylindrical coordinates to rectangular coordinates.

```python
cylindrical_to_rectangular(r, theta, z, degrees=False)
```

- **Args**:
  - `r` (float): The radial distance.
  - `theta` (float): The angle in radians (or degrees if `degrees=True`).
  - `z` (float): The height along the z-axis.
  - `degrees` (bool): Whether `theta` is in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: The rectangular coordinates as `(x, y, z)`.

- **Example**:
  ```python
  >>> cylindrical_to_rectangular(5, 45, 10, degrees=True)
  (3.5355339059327378, 3.5355339059327373, 10)
  ```

---

### Rectangular to Cylindrical

Converts rectangular coordinates to cylindrical coordinates.

```python
rectangular_to_cylindrical(x, y, z, degrees=False)
```

- **Args**:
  - `x` (float): The x-coordinate.
  - `y` (float): The y-coordinate.
  - `z` (float): Height along the z-axis.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Cylindrical coordinates as `(r, theta, z)`.

- **Example**:
  ```python
  >>> rectangular_to_cylindrical(3, 4, 10)
  (5.0, 0.9272952180016122, 10)
  ```

---

### Polar to Complex 

Converts polar coordinates to a complex number.

```python
polar_to_complex(r, theta, degrees=False)
```

- **Args**:
  - `r` (float): Radial distance.
  - `theta` (float): Angle in radians (or degrees if `degrees=True`).
  - `degrees` (bool): Whether the angle is in degrees. Defaults to `False`.

- **Returns**:
  - `complex`: Complex number.

- **Example**:
  ```python
  >>> polar_to_complex(5, 45, degrees=True)
  (3.5355339059327378+3.5355339059327373j)
  ```

---

### Complex to Polar

Converts a complex number to polar coordinates.

```python
complex_to_polar(c, degrees=False)
```

- **Args**:
  - `c` (complex): A complex number.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Polar coordinates as `(r, theta)`.

- **Example**:
  ```python
  >>> complex_to_polar(3 + 4j)
  (5.0, 0.9272952180016122)
  ```

---

## Complex Form Conversion

### Polar to Rectangular

Converts polar coordinates to rectangular coordinates.

```python
polar_to_rectangular(r, theta, degrees=False)
```

- **Args**:
  - `r` (float): The radial distance from the origin.
  - `theta` (float): The angle in radians (or degrees if `degrees=True`).
  - `degrees` (bool): Whether the angle is in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Rectangular coordinates as `(x, y)`.

- **Example**:
  ```python
  >>> polar_to_rectangular(5, 45, degrees=True)
  (3.5355339059327378, 3.5355339059327373)
  ```

---

### Rectangular to Polar

Converts rectangular coordinates to polar coordinates.

```python
rectangular_to_polar(x, y, degrees=False)
```

- **Args**:
  - `x` (float): The x-coordinate.
  - `y` (float): The y-coordinate.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Polar coordinates as `(r, theta)`.

- **Example**:
  ```python
  >>> rectangular_to_polar(3, 4)
  (5.0, 0.9272952180016122)
  ```

---

### Bulk Polar to Rectangular

Converts a list of polar coordinates to rectangular coordinates.

```python
bulk_polar_to_rectangular(polar_list, degrees=False)
```

- **Args**:
  - `polar_list` (list): List of tuples containing polar coordinates `(r, theta)`.
  - `degrees` (bool): Whether the angles are in degrees. Defaults to `False`.

- **Returns**:
  - `list`: List of rectangular coordinates.

- **Example**:
  ```python
  >>> bulk_polar_to_rectangular([(5, 45), (10, 30)], degrees=True)
  [(3.5355339059327378, 3.5355339059327373), (8.660254037844386, 4.999999999999999)]
  ```

---

### Bulk Rectangular to Polar

Converts a list of rectangular coordinates to polar coordinates.

```python
bulk_rectangular_to_polar(rectangular_list, degrees=False)
```

- **Args**:
  - `rectangular_list` (list): List of tuples containing rectangular coordinates `(x, y)`.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `list`: List of polar coordinates.

- **Example**:
  ```python
  >>> bulk_rectangular_to_polar([(3, 4), (5, 12)])
  [(5.0, 0.9272952180016122), (13.0, 1.176005207095135)]
  ```

---

### Cylindrical to Rectangular

Converts cylindrical coordinates to rectangular coordinates.

```python
cylindrical_to_rectangular(r, theta, z, degrees=False)
```

- **Args**:
  - `r` (float): The radial distance.
  - `theta` (float): The angle in radians (or degrees if `degrees=True`).
  - `z` (float): The height along the z-axis.
  - `degrees` (bool): Whether `theta` is in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: The rectangular coordinates as `(x, y, z)`.

- **Example**:
  ```python
  >>> cylindrical_to_rectangular(5, 45, 10, degrees=True)
  (3.5355339059327378, 3.5355339059327373, 10)
  ```

---

### Rectangular to Cylindrical

Converts rectangular coordinates to cylindrical coordinates.

```python
rectangular_to_cylindrical(x, y, z, degrees=False)
```

- **Args**:
  - `x` (float): The x-coordinate.
  - `y` (float): The y-coordinate.
  - `z` (float): Height along the z-axis.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Cylindrical coordinates as `(r, theta, z)`.

- **Example**:
  ```python
  >>> rectangular_to_cylindrical(3, 4, 10)
  (5.0, 0.9272952180016122, 10)
  ```

---

### Polar to Complex 

Converts polar coordinates to a complex number.

```python
polar_to_complex(r, theta, degrees=False)
```

- **Args**:
  - `r` (float): Radial distance.
  - `theta` (float): Angle in radians (or degrees if `degrees=True`).
  - `degrees` (bool): Whether the angle is in degrees. Defaults to `False`.

- **Returns**:
  - `complex`: Complex number.

- **Example**:
  ```python
  >>> polar_to_complex(5, 45, degrees=True)
  (3.5355339059327378+3.5355339059327373j)
  ```

---

### Complex to Polar

Converts a complex number to polar coordinates.

```python
complex_to_polar(c, degrees=False)
```

- **Args**:
  - `c` (complex): A complex number.
  - `degrees` (bool): Whether to return the angle in degrees. Defaults to `False`.

- **Returns**:
  - `tuple`: Polar coordinates as `(r, theta)`.

- **Example**:
  ```python
  >>> complex_to_polar(3 + 4j)
  (5.0, 0.9272952180016122)
  ```

---
