user_input=input()
most_frequent_character=""
max_num=0
for i in user_input:
    b=0
    for i1 in user_input:
        if i1 == i:
            b+=1
    if b > max_num:
        max_num=b
        most_frequent_character=i
print(most_frequent_character)
