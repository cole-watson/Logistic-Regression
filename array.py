def dict_array(list_dict, headers, class_name):
	x_list = []
	y_list = []
	x_temp = []
	for data_point in list_dict:
		for name in headers:
			x_temp.append(data_point[name])
		x_list.append(x_temp)
		x_temp = []
		y_list.append(data_point[class_name])

	return x_list, y_list