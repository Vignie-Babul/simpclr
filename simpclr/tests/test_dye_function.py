from simpclr.src.simpclr import dye

import unittest


class TestDyeFunction(unittest.TestCase):
	def setUp(self):
		self.foreground = '\033[38;2;0;0;0m'
		self.background = '\033[48;2;255;255;255m'
		self.string_code = 'string\033[0m'

		self.fg_str = self.foreground + self.string_code
		self.bg_str = self.background + self.string_code
		self.fg_bg_str = self.foreground + self.background + self.string_code

		self.string = 'string'
		self.fg_color = '#000000'
		self.bg_color = '#ffffff'

	def test_string_string(self):
		self.assertEqual(dye(self.string), self.string)

	def test_string_fg_color_fg_str(self):
		self.assertEqual(dye(self.string, self.fg_color), self.fg_str)

	def test_string_bg_color_bg_str(self):
		self.assertEqual(dye(self.string, background=self.bg_color), self.bg_str)

	def test_string_fg_color_bg_color_fg_str(self):
		self.assertEqual(dye(self.string, self.fg_color, self.bg_color), self.fg_bg_str)


if __name__ == '__main__':
	unittest.main()