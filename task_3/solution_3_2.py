alphabet=""
new_alphabet=""  
for i in 'a'*10:
    user_input = input()
    new_alphabet+=user_input
for character in new_alphabet:
    if character not in  alphabet:
        alphabet+=character
print(alphabet)
