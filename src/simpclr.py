from dataclasses import dataclass
import os
import random


__all__ = (
	'RGB', 'HSL', 'rgb', 'hsl',
	'dye', 'dye_random_char',
	'is_windows',
	'WHITE', 'GREY', 'DARK_GREY', 'BLACK',
	'RED', 'ORANGE', 'YELLOW', 'GREEN',
	'LIGHT_BLUE', 'BLUE', 'PURPLE', 'MAGENTA'
)


# colored text output fix
os.system('')


def _validate_rgb(red: int, green: int, blue: int) -> None:
	if not (0 <= red <= 255):
		raise ValueError('Red must be in range 0 <= red <= 255')
	elif not (0 <= green <= 255):
		raise ValueError('Green must be in range 0 <= green <= 255')
	elif not (0 <= blue <= 255):
		raise ValueError('Blue must be in range 0 <= blue <= 255')

def _validate_hsl(hue: int, saturation: float, lightness: float) -> None:
	if not (0 <= hue <= 360):
		raise ValueError('Hue must be in range 0 <= hue <= 360')
	elif not (0 <= saturation <= 1):
		raise ValueError('Saturation must be in range 0 <= saturation <= 1')
	elif not (0 <= lightness <= 1):
		raise ValueError('Lightness must be in range 0 <= lightness <= 1')


@dataclass
class RGB:
	red: int
	green: int
	blue: int

	def __post_init__(self):
		_validate_rgb(self.red, self.green, self.blue)

	def __repr__(self):
		return f'RGB({self.red}, {self.green}, {self.blue})'

	def hex(self):
		return rgb(self.red, self.green, self.blue)


@dataclass
class HSL:
	hue: int
	saturation: int | float
	lightness: int | float

	def __post_init__(self):
		_validate_hsl(self.hue, self.saturation, self.lightness)

	def __repr__(self):
		return f'HSL({self.hue}, {self.saturation}, {self.lightness})'

	def hex(self):
		return rgb(self.hue, self.saturation, self.lightness)


def rgb(red: int, green: int, blue: int) -> str:
	"""RGB color function. Converts RGB to HEX

	Args:
		red - 0 <= red <= 255
		green - 0 <= green <= 255
		blue - 0 <= blue <= 255

	Return:
		1. Returns ValueError if the arguments are outside the specified range
		2. HEX color string
	"""

	_validate_rgb(red, green, blue)

	return f'#{red:02x}{green:02x}{blue:02x}'

def hsl(hue: int, saturation: float, lightness: float) -> str:
	"""HSL color function. Converts HSL to HEX

	Conversion formula was taken from
		https://www.rapidtables.com/convert/color/hsl-to-rgb.html
	
	Args:
		hue: 0 <= hue <= 360
		saturation: 0 <= saturation <= 1
		lightness: 0 <= lightness <= 1

	Return:
		1. Returns ValueError if the arguments are outside the specified range
		2. HEX color string
	"""

	_validate_hsl(hue, saturation, lightness)

	hue %= 360

	c = (1 - abs(2*lightness - 1)) * saturation
	x = c * (1 - abs((hue/60)%2 - 1))
	m = lightness - c/2

	rgbd_table = (
		(c, x, 0),
		(x, c, 0),
		(0, c, x),
		(0, x, c),
		(x, 0, c),
		(c, 0, x),
	)

	r, g, b = rgbd_table[int(hue // 60)]

	r = round((r+m) * 255)
	g = round((g+m) * 255)
	b = round((b+m) * 255)

	return f'#{r:02x}{g:02x}{b:02x}'

def dye(
		string: str,
		foreground: str | None = None,
		background: str | None = None
	) -> str:

	"""String coloring function in HEX color scheme using ANSI code
	
	Args:
		string: string that would be colored
		foreground: foreground color in HEX
		background: background color in HEX

	Return:
		Colored string using ANSI code
	"""

	if (background is None) and (foreground is None):
		return string

	foreground_code = ''
	background_code = ''
	string_code = f'{string}\033[0m' 

	if foreground is not None:
		foreground_hex = foreground.lstrip('#')
		foreground_rgb = tuple(
			int(foreground_hex[i:i+2],16) for i in (0, 2, 4)
		)
		foreground_code = '\033[38;2;{};{};{}m'.format(*foreground_rgb)

	if background is not None:
		background_hex = background.lstrip('#')
		background_rgb = tuple(
			int(background_hex[i:i+2],16) for i in (0, 2, 4)
		)
		background_code = '\033[48;2;{};{};{}m'.format(*background_rgb)

	return foreground_code + background_code + string_code

def dye_random_char(
		string: str,
		hsl_from: HSL,
		hsl_to: HSL,
		shades_number: int = 15
	) -> str:

	"""Coloring every char of string in random or
	selected shade of HSL color scheme.

	Args:
		string: string that would be colored
		hsl_from: instance of HSL dataclass or tuple with HSL arguments
		hsl_to: instance of HSL dataclass or tuple with HSL arguments
		shades_number: number of shades

	Return:
		Colored string with every char colored in shade
	"""

	if isinstance(hsl_from, HSL):
		hsl_from = (hsl_from.hue, hsl_from.saturation, hsl_from.lightness)
	elif isinstance(hsl_to, HSL):
		hsl_to = (hsl_to.hue, hsl_to.saturation, hsl_to.lightness)

	max_hue = max(hsl_from[0], hsl_to[0])
	min_hue = min(hsl_from[0], hsl_to[0])

	max_saturation = max(hsl_from[1], hsl_to[1])
	min_saturation = min(hsl_from[1], hsl_to[1])

	max_lightness = max(hsl_from[2], hsl_to[2])
	min_lightness = min(hsl_from[2], hsl_to[2])

	shades_hsl = [
		[
			random.randint(min_hue, max_hue),
			random.randint(min_saturation*100, max_saturation*100) / 100,
			random.randint(min_lightness*100, max_lightness*100) / 100,
		] for _ in range(shades_number)
	]

	# converting HSL to HEX
	shades_hex = tuple(
		map(
			lambda shade: hsl(*shade),
			shades_hsl
		)
	)

	# coloring
	colored_string = ''

	for char in string:
		random_shade = random.choice(shades_hex)
		colored_char = dye(char, random_shade)

		colored_string += colored_char

	return colored_string


def is_windows() -> bool:
	return os.name == 'nt'


WHITE = hsl(0, 0, 1)
GREY = hsl(0, 0, 0.6)
DARK_GREY = hsl(0, 0, 0.35)
BLACK = hsl(0, 0, 0)

RED = hsl(0, 0.7, 0.5)
ORANGE = hsl(24, 0.7, 0.5)
YELLOW = hsl(60, 0.7, 0.5)
GREEN = hsl(120, 0.7, 0.5)
LIGHT_BLUE = hsl(180, 0.7, 0.5)
BLUE = hsl(240, 0.7, 0.5)
PURPLE = hsl(280, 0.7, 0.5)
MAGENTA = hsl(300, 0.7, 0.5)


if __name__ == '__main__':
	print(dye('Hello World!', WHITE))
	print(dye('Hello World!', GREY))
	print(dye('Hello World!', DARK_GREY))
	print(dye('Hello World!', BLACK))
	print(dye('Hello World!', RED))
	print(dye('Hello World!', ORANGE))
	print(dye('Hello World!', YELLOW))
	print(dye('Hello World!', GREEN))
	print(dye('Hello World!', LIGHT_BLUE))
	print(dye('Hello World!', BLUE))
	print(dye('Hello World!', PURPLE))
	print(dye('Hello World!', MAGENTA))