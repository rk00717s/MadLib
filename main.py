import json
from random import randrange

# op_values = [
#     "ADJECTIVE : ",
#     "BODY PART : ",
#     "PERSON IN ROOM : ",
#     "PLURAL NOUN : ",
#     "PLURAL NOUN : ",
#     "VERB ENDING IN “ING” : ",
#     "ADJECTIVE : ",
#     "ADJECTIVE : ",
#     "ADJECTIVE : ",
#     "ADJECTIVE : ",
#     "PLURAL NOUN : ",
#     "VERB : ",
#     "VERB ENDING IN “ING” : ",
#     "VERB : ",
#     "BODY PART : ",
#     "NOUN : ",
#     "ADJECTIVE : ",
#     "PLURAL NOUN : ",
#     "ADJECTIVE : ",
#     "PLURAL NOUN : ",
#     "VERB : ",
#     "ADJECTIVE : ",
#     "ADJECTIVE : ",
#     "VERB ENDING IN “ING” : ",
#     "VERB : "
# ]

with open("Materials.json", mode = 'r', encoding = 'utf-8', errors = 'strict', buffering = 1) as file:
    contents = json.load(file)

keypick = str(randrange(0, len(contents)+1))

formating_values = list()

counter=0

# print(f"Number of values to be taken : {len(contents[keypick]["inputs"])}")
for op in contents[keypick]["inputs"]:
    counter+=1
    formating_values.append(input(f"{counter}. {op}"))

formated_string = (contents[keypick]["paragraph"]).format(*formating_values)

# content = "In today’s {} digital landscape, content marketers must be sure to keep their {} on the pulse of the customer. Online, you have no more than a few seconds to grab {}’s attention. So how can marketers keep the “fun factor” in mind when it comes to communications? First, think like your {} or {}. What are they {}? What are their likes or dislikes? Once you have your {} audience in mind, you can get to work on your messaging. There’s no magic formula for going viral; rather, you can increase your chances of being seen by coming up with {}, {} ideas that are cleverly packaged. Remember, Content is King but, with more than 53 million WordPress blogs online, what makes yours {}? What are your {} writing about? Do your research!  The key is to {} your prospects something new, introduce them to a new way of {} or doing business, and provide content they can’t wait to share with their colleagues. One way to {} the word is through social media platforms like {}-book and Twitter. Face-{} allows you to create an/an {} profile, add other {} as friends, and exchange {} messages. Twitter is a great way to stay in touch with clients and {} and share relevant content. But be careful not to {} content where it doesn’t belong. Be {} and judicious in this practice to avoid ending up in the {} box. These are just some suggestions for {} compelling content; above all, be sure to {} the right message to the right audience at the right time.".format(*formating_values)

# with open('Materials', 'r') as file:
#     content = str(file.readlines())

# content = content.split(" ")
# print(content)

# counter = 0
# for word in content:
#     pattern = f"[{counter}]"
#     if(pattern == word):
#         content[content.index(word)] = formating_values[counter]
#         counter+=1

# content = str(" ".join(content))
# print(content)

# print(f"a.\n {content} \n\n\n b.\n {formated_string} \n\n\n c.\n {formating_values}")

print(formated_string)