#!/usr/bin/env python3

from data import data_reader
from probability import cost_function
import sys

def main():

	if len(sys.argv)!= 6:
		print("Please add arguments")
		sys.exit(2)

	try:
		data = data_reader(sys.argv[1])
		test_data = data_reader(sys.argv[2])[0]
	except FileNotFoundError:
		print("File location in parameters are incorrect")
		sys.exit(2)

	training_data = data[0]
	class_name = data[1]
	headers = list(training_data[0].keys())
	headers.remove(class_name)

	bias = 1
	num_samples = len(training_data)



if __name__ =="__main__":
    main()