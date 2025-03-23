from simpclr.src.simpclr import rgb

import unittest


class TestRGBFunction(unittest.TestCase):
	# test values in range
	def test_r0_g0_b0_000000(self):
		self.assertEqual(rgb(0, 0, 0), '#000000')

	def test_r0_g0_b255_0000ff(self):
		self.assertEqual(rgb(0, 0, 255), '#0000ff')

	def test_r0_g255_b255_00ffff(self):
		self.assertEqual(rgb(0, 255, 255), '#00ffff')

	def test_r0_g255_b0_00ff00(self):
		self.assertEqual(rgb(0, 255, 0), '#00ff00')

	def test_r255_g255_b0_ffff00(self):
		self.assertEqual(rgb(255, 255, 0), '#ffff00')

	def test_r255_g0_b0_ff0000(self):
		self.assertEqual(rgb(255, 0, 0), '#ff0000')

	def test_r255_g0_b255_ff00ff(self):
		self.assertEqual(rgb(255, 0, 255), '#ff00ff')

	def test_r255_g255_b255_ffffff(self):
		self.assertEqual(rgb(255, 255, 255), '#ffffff')

	# test color
	def test_r57_g28_b74_391c4a(self):
		self.assertEqual(rgb(57, 28, 74), '#391c4a')

	# test values out of range exception
	def test_r0_g0_b_minus1_value_error(self):
		with self.assertRaises(ValueError):
			rgb(0, 0, -1)

	def test_r0_g_minus1_b0_value_error(self):
		with self.assertRaises(ValueError):
			rgb(0, -1, 0)

	def test_r_minus1_g0_b0_value_error(self):
		with self.assertRaises(ValueError):
			rgb(-1, 0, 0)

	def test_r0_g0_b256_value_error(self):
		with self.assertRaises(ValueError):
			rgb(0, 0, 256)

	def test_r0_g256_b0_value_error(self):
		with self.assertRaises(ValueError):
			rgb(0, 256, 0)

	def test_r256_g0_b0_value_error(self):
		with self.assertRaises(ValueError):
			rgb(256, 0, 0)


if __name__ == '__main__':
	unittest.main()