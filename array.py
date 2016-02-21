def dict_array(list):
	final_array = []
	temp_array = []
	for dic in list:
		for key, value in dict.items():
			temp_array.append(value)
		temp_array = []

	return final_array