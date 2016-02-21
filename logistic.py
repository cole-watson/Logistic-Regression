#!/usr/bin/env python3

from data_reader import data_reader
from array import dict_array
from calculations import * 
import sys

def main():
	#check if the user entered in correct ammount of arguments
	if len(sys.argv)!= 6:
		print("Please add arguments")
		sys.exit(2)

	#read the training set and test set
	try:
		data = data_reader(sys.argv[1])
		test_data = data_reader(sys.argv[2])[0]
	except FileNotFoundError:
		print("File location in parameters are incorrect")
		sys.exit(2)

	#get the sigma and learning rate values
	learning = sys.argv[3]
	sigma = sys.argv[4]
	training_data = data[0]
	class_name = data[1]
	headers = list(training_data[0].keys())
	headers.remove(class_name)

	train = dict_array(training_data)

if __name__ == "__main__":
	main()
