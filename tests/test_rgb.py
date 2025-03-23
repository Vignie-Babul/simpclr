from simpclr.src.simpclr import RGB

import unittest


class TestRGB(unittest.TestCase):
	# lower edge
	def test_r0_g0_b0_red_0(self):
		self.assertEqual(RGB(0, 0, 0).red, 0)

	def test_r0_g0_b0_green_0(self):
		self.assertEqual(RGB(0, 0, 0).green, 0)

	def test_r0_g0_b0_blue_0(self):
		self.assertEqual(RGB(0, 0, 0).blue, 0)

	# upper edge
	def test_r255_g0_b0_red_255(self):
		self.assertEqual(RGB(255, 0, 0).red, 255)

	def test_r0_g255_b0_green_255(self):
		self.assertEqual(RGB(0, 255, 0).green, 255)

	def test_r0_g0_b255_blue_255(self):
		self.assertEqual(RGB(0, 0, 255).blue, 255)

	# test values out of range exception
	def test_r_minus1_g0_b0_value_error(self):
		with self.assertRaises(ValueError):
			RGB(-1, 0, 0)

	def test_r0_g_minus1_b0_value_error(self):
		with self.assertRaises(ValueError):
			RGB(0, -1, 0)

	def test_r0_g0_b_minus1_value_error(self):
		with self.assertRaises(ValueError):
			RGB(0, 0, -1)

	def test_r256_g0_b0_value_error(self):
		with self.assertRaises(ValueError):
			RGB(256, 0, 0)

	def test_r0_g256_b0_value_error(self):
		with self.assertRaises(ValueError):
			RGB(0, 256, 0)

	def test_r0_g0_b256_value_error(self):
		with self.assertRaises(ValueError):
			RGB(0, 0, 256)


if __name__ == '__main__':
	unittest.main()