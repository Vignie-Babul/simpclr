from simpclr.src.simpclr import dye_random_char, HSL

import unittest


class TestDyeRandomCharFunction(unittest.TestCase):
	def test_empty_string_empty_string(self):
		self.assertEqual(dye_random_char('', (0, 0, 0), (360, 1, 1)), '')

	# test values out of range exception
	# hsl from
	def test_hsl_from_h_minus1_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(-1, 0, 0), HSL(0, 0, 0))

	def test_hsl_from_h0_s_minus1_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, -1, 0), HSL(0, 0, 0))

	def test_hsl_from_h0_s0_l_minus1_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, -1), HSL(0, 0, 0))

	def test_hsl_from_h361_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(361, 0, 0), HSL(0, 0, 0))

	def test_hsl_from_h0_s2_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 2, 0), HSL(0, 0, 0))

	def test_hsl_from_h0_s0_l2_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, 2), HSL(0, 0, 0))

	# hsl to
	def test_hsl_to_h_minus1_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, 0), HSL(-1, 0, 0))

	def test_hsl_to_h0_s_minus1_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, 0), HSL(0, -1, 0))

	def test_hsl_to_h0_s0_l_minus1_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, 0), HSL(0, 0, -1))

	def test_hsl_to_h361_s0_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, 0), HSL(361, 0, 0))

	def test_hsl_to_h0_s2_l0_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, 0), HSL(0, 2, 0))

	def test_hsl_to_h0_s0_l2_value_error(self):
		with self.assertRaises(ValueError):
			dye_random_char('', HSL(0, 0, 0), HSL(0, 0, 2))


if __name__ == '__main__':
	unittest.main()