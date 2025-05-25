def get_num_words(text):
	return (len(text.split()))


def get_num_chars(text):
	char_dict = {}	
	for char in text:
		char = char.lower()
		if char in char_dict:
			char_dict[char] += 1			
		else:
			char_dict[char] = 1
	return char_dict


def sort_on(d):
    return d["num"]


def get_sorted(char_dict):
	sorted_list = []
	for i in char_dict:
		if i.isalpha():
			sorted_list.append({"char": i, "num": char_dict[i]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
	



