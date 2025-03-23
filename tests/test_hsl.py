from simpclr.src.simpclr import HSL

import unittest


class TestHSL(unittest.TestCase):
	# lower edge
	def test_h0_s0_l0_hue_0(self):
		self.assertEqual(HSL(0, 0, 0).hue, 0)

	def test_h0_s0_l0_saturation_0(self):
		self.assertEqual(HSL(0, 0, 0).saturation, 0)

	def test_h0_s0_l0_lightness_0(self):
		self.assertEqual(HSL(0, 0, 0).lightness, 0)

	# upper edge
	def test_h0_s0_l0_hue_360(self):
		self.assertEqual(HSL(360, 0, 0).hue, 360)

	def test_h0_s0_l0_saturation_1(self):
		self.assertEqual(HSL(0, 1, 0).saturation, 1)

	def test_h0_s0_l0_lightness_1(self):
		self.assertEqual(HSL(0, 0, 1).lightness, 1)

	# test values out of range exception
	def test_h_minus1_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			HSL(-1, 0, 0)

	def test_h0_s_minus1_l0_value_error(self):
		with self.assertRaises(ValueError):
			HSL(0, -1, 0)

	def test_h0_s0_l_minus1_value_error(self):
		with self.assertRaises(ValueError):
			HSL(0, 0, -1)

	def test_h361_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			HSL(361, 0, 0)

	def test_h0_s2_l0_value_error(self):
		with self.assertRaises(ValueError):
			HSL(0, 2, 0)

	def test_h0_s0_l2_value_error(self):
		with self.assertRaises(ValueError):
			HSL(0, 0, 2)


if __name__ == '__main__':
	unittest.main()