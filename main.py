op_values = [
    "ADJECTIVE : ",
    "BODY PART : ",
    "PERSON IN ROOM : ",
    "PLURAL NOUN : ",
    "PLURAL NOUN : ",
    "VERB ENDING IN “ING” : ",
    "ADJECTIVE : ",
    "ADJECTIVE : ",
    "ADJECTIVE : ",
    "ADJECTIVE : ",
    "PLURAL NOUN : ",
    "VERB : ",
    "VERB ENDING IN “ING” : ",
    "VERB : ",
    "BODY PART : ",
    "NOUN : ",
    "ADJECTIVE : ",
    "PLURAL NOUN : ",
    "ADJECTIVE : ",
    "PLURAL NOUN : ",
    "VERB : ",
    "ADJECTIVE : ",
    "ADJECTIVE : ",
    "VERB ENDING IN “ING” : ",
    "VERB : "
]

formating_values = list()

for op in op_values:
    formating_values.append(input(op))

formated_string = ""

content = "In today’s [0] digital landscape, content marketers must be sure to keep their [1] on the pulse of the customer. Online, you have no more than a few seconds to grab [2]’s attention. So how can marketers keep the “fun factor” in mind when it comes to communications? First, think like your [3] or [4]. What are they [5]? What are their likes or dislikes? Once you have your [6] audience in mind, you can get to work on your messaging. There’s no magic formula for going viral; rather, you can increase your chances of being seen by coming up with [7], [8] ideas that are cleverly packaged. Remember, Content is King but, with more than 53 million WordPress blogs online, what makes yours [9]? What are your [10] writing about? Do your research!  The key is to [11] your prospects something new, introduce them to a new way of [12] or doing business, and provide content they can’t wait to share with their colleagues. One way to [13] the word is through social media platforms like [14]-book and Twitter. Face-[15] allows you to create an/an [16] profile, add other [17] as friends, and exchange [18] messages. Twitter is a great way to stay in touch with clients and [19] and share relevant content. But be careful not to [20] content where it doesn’t belong. Be [21] and judicious in this practice to avoid ending up in the [22] box. These are just some suggestions for [23] compelling content; above all, be sure to [24] the right message to the right audience at the right time."
# with open('Materials', 'r') as file:
#     content = str(file.readlines())

tmp_content = content.split(' ')
for index in range(len(formating_values)):
    if(tmp_content[index] == f'[{index}]'):
        tmp_content[index] = formating_values[index]

tmp_content = str(tmp_content.join(' '))

print(f"{content}, {tmp_content}, {formated_string}, {formating_values}")