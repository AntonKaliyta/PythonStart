list_dict = [{"V": "S001"}, {"V": "S002"},
	         {"VI": "S001"}, {"VI": "S005"},
	         {"VII": " S005 "}, {"V": " S009 "},
	         {"VIII": " S007 "}]


# temp = [list(i.values())[0].strip() for i in list_dict]
# print(set(temp))

print(set([list(i.values())[0].strip() for i in list_dict]))