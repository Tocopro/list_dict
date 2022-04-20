


roll_numbers = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John':47, 'emma':69, 'kelly':76, 'Jason': 97}

print('List:', roll_numbers)
print('Dictionary', sample_dict)

roll_numbers[:] = [item for item in roll_numbers if item in sample_dict.values()]
print(roll_numbers)

speed = {'jan':47, 'feb':52, 'march':47, 'april':44, 'may':52, 'june':53, 'july':54, 'Aug':44
         , 'sep':54}
speed_list = list()

print('Dictionary values',speed.values())
for val in speed.values():
    if val not in speed_list:
        speed_list.append(val)
print('Unique list', speed_list)
