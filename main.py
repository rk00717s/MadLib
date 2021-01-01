import json
from random import randrange

with open("Materials.json", mode = 'r', encoding = 'utf-8', errors = 'strict', buffering = 1) as file:
    contents = json.load(file)

keypick = str(randrange(1, len(contents)+1))

formating_values = list()

print(f'Number of inputs to be taken : {len(contents[keypick]["inputs"])}')
counter=0
for op in contents[keypick]["inputs"]:
    counter+=1
    formating_values.append(input(f"{counter}. {op}"))

formated_string = (contents[keypick]["paragraph"]).format(*formating_values)

print(formated_string)