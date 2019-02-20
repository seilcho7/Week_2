from characters import characters
allegiance_dict = {}
house_number = ""
for k in characters:
   if k['allegiances'] != []:
   # print(k['allegiances'])
       house_number = (k['allegiances'])
print(house_number)
for i in house_number:
   if i in allegiance_dict:
       allegiance_dict[i] += 1
   else:
       allegiance_dict[i] = 1

print(allegiance_dict)