import pytest
import calculator as cal

# Determine if calculation could be done correctly

def test_sum_method1():
	a=6
	b=5
	assert cal.sum(a, b) == 11, "Summation Error: Please check cal.sum()."


def test_discrepancy_test():
	# benchmark= 178.75
	benchmark = 5
	threshold = 0.05
	a = 0.53515
	b = 334

	calculated = cal.multiply(a, b)
	difference = abs(benchmark - calculated)

	assert difference <= threshold, "Discrepancy over the threshold, further investigation required"