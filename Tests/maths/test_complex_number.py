import unittest
from pysnippets.maths.complex_number_operations import (
    add_complex,
    multiply_complex,
    normalize_complex,
    conjugate_complex,
    reciprocal_complex,
    magnitude_complex,
    phase_complex,
    nth_roots_complex,
    rotate_complex,
    is_conjugate
)

class TestComplexNumbers(unittest.TestCase):

    def test_add_complex(self):
        # Test case for normal behavior
        self.assertEqual(add_complex((1, 2), (3, 4)), (4, 6))

    def test_multiply_complex(self):
        # Test case for normal behavior
        self.assertEqual(multiply_complex((1, 2), (3, 4)), (-5, 10))

    def test_add_complex_invalid(self):
        # Test case for invalid input
        with self.assertRaises(TypeError):
            add_complex((1, 2), "string")

    def test_normalize_complex(self):
        # Test case for normal behavior
        self.assertEqual(normalize_complex((3, 4)), (0.6, 0.8))

        # Test case for zero input
        self.assertEqual(normalize_complex((0, 0)), (0, 0))

    def test_conjugate_complex(self):
        # Test case for normal behavior
        self.assertEqual(conjugate_complex((3, 4)), (3, -4))

    def test_reciprocal_complex(self):
        # Test case for normal behavior
        self.assertEqual(reciprocal_complex((3, 4)), (0.12, -0.16))

        # Test case for zero input (should raise ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            reciprocal_complex((0, 0))

    def test_magnitude_complex(self):
        # Test case for normal behavior
        self.assertEqual(magnitude_complex((3, 4)), 5.0)

    def test_phase_complex(self):
        # Test case for normal behavior
        self.assertEqual(phase_complex((3, 4)), 0.9272952180016122)

    def test_nth_roots_complex(self):
        # Test case for finding 3rd roots of a complex number
        self.assertEqual(nth_roots_complex((1, 0), 3), [(1.0, 0.0), (-0.5, 0.8660254037844386), (-0.5, -0.8660254037844386)])

    def test_rotate_complex(self):
        # Test case for rotating a complex number by 90 degrees
        self.assertEqual(rotate_complex((1, 2), 90, degrees=True), (-2.0, 1.0))

    def test_is_conjugate(self):
        # Test case for checking conjugates
        self.assertTrue(is_conjugate((3, 4), (3, -4)))
        self.assertFalse(is_conjugate((3, 4), (5, 6)))

if __name__ == '__main__':
    unittest.main()
