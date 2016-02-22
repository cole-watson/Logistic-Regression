#!/usr/bin/env python3

from data_reader import data_reader
from array import *
from calculations import *
import sys


def main():
    # check if the user entered in correct ammount of arguments
    if len(sys.argv) != 6:
        print("Please add arguments")
        sys.exit(2)

        # read the training set and test set
    try:
        data = data_reader(sys.argv[1])
        test_data = data_reader(sys.argv[2])[0]
    except FileNotFoundError:
        print("File location in parameters are incorrect")
        sys.exit(2)

        # get the sigma and learning rate values
    learning = float(sys.argv[3])
    sigma = float(sys.argv[4])
    training_data = data[0]
    class_name = data[1]
    headers = list(training_data[0].keys())
    headers.sort()
    headers.remove(class_name)


    x_train, y_train = dict_array(training_data, headers, class_name)

    #convert arrays to np arrays
    x_train = np.array(x_train)
    y_train = np.array(y_train)

    x_test, y_test = dict_array(test_data, headers, class_name)

    #convert arrays to np arrays
    x_test = np.array(x_test)
    y_test = np.array(y_test)

    w = train(x_train, y_train, sigma, learning)

    for i in range(0,len(w)):
        print(headers[i] + " " + str(w[i]))

    percentage = correct(x_test, y_test, w) * 100

    print ("Percent Correct: " +  str(percentage) + "%")

if __name__ == "__main__":
    main()
