from .test_rgb import TestRGB
from .test_hsl import TestHSL
from .test_rgb_function import TestRGBFunction
from .test_hsl_function import TestHSLFunction
from .test_dye_function import TestDyeFunction
from .test_dye_random_char_function import TestDyeRandomCharFunction

import unittest


def run_tests(
		test_classes: tuple[unittest.TestCase, ...]
	) -> unittest.runner.TextTestResult:

	loader = unittest.TestLoader()
	runner = unittest.TextTestRunner()

	return runner.run(
		unittest.TestSuite(
			[
				loader.loadTestsFromTestCase(
					test_class
				) for test_class in test_classes
			]
		)
	)


def main() -> None:
	test_classes = (
		TestRGB,
		TestHSL,
		TestRGBFunction,
		TestHSLFunction,
		TestDyeFunction,
		TestDyeRandomCharFunction,
	)

	run_tests(test_classes=test_classes)