d = {'a': 4, 'b': 2, 'c': 7, 'd': 1}

sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))

print(sorted_dict)