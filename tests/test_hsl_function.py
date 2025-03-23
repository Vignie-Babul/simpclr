from simpclr.src.simpclr import hsl

import unittest


class TestHSLFunction(unittest.TestCase):
	# test values in range
	# black (lightness 0)
	def test_h0_s0_l0_000000(self):
		self.assertEqual(hsl(0, 0, 0.0), '#000000')

	def test_h0_s1_l0_000000(self):
		self.assertEqual(hsl(0, 1, 0), '#000000')

	def test_h360_s0_l0_000000(self):
		self.assertEqual(hsl(360, 0, 0.0), '#000000')

	def test_h360_s1_l0_000000(self):
		self.assertEqual(hsl(360, 1, 0), '#000000')

	# white (lightness 1)
	def test_h0_s0_l1_ffffff(self):
		self.assertEqual(hsl(0, 0, 1), '#ffffff')

	def test_h0_s1_l1_ffffff(self):
		self.assertEqual(hsl(0, 1, 1), '#ffffff')

	def test_h360_s0_l1_ffffff(self):
		self.assertEqual(hsl(360, 0, 1), '#ffffff')

	def test_h360_s1_l1_ffffff(self):
		self.assertEqual(hsl(360, 1, 1), '#ffffff')

	# test color
	def test_h278_s045_l02_391c4a(self):
		self.assertEqual(hsl(278, 0.45, 0.20), '#391c4a')

	# test values out of range exception
	def test_h_minus1_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			hsl(-1, 0, 0)

	def test_h0_s_minus1_l0_value_error(self):
		with self.assertRaises(ValueError):
			hsl(0, -1, 0)

	def test_h0_s0_l_minus1_value_error(self):
		with self.assertRaises(ValueError):
			hsl(0, 0, -1)

	def test_h361_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			hsl(361, 0, 0)

	def test_h0_s2_l0_value_error(self):
		with self.assertRaises(ValueError):
			hsl(0, 2, 0)

	def test_h0_s0_l2_value_error(self):
		with self.assertRaises(ValueError):
			hsl(0, 0, 2)


if __name__ == '__main__':
	unittest.main()