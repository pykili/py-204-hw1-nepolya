user_input= input()
alphabet=""
for character in user_input:
    if character not in alphabet:
        alphabet=alphabet+character
print(alphabet)
