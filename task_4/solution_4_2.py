print("ID	form	lemma	что_то_ещё")
for i in "a"*10:
    user_input=input()
    if user_input !="" and user_input[0]!="#":
        num_of_tabs = 0
        form = ""
        for character in user_input:
            if num_of_tabs == 1:
                form+=character
            if character=="\t":
                num_of_tabs += 1
        num_of_tabs=0
        lemma = ""
        for character in user_input:
            if num_of_tabs == 2:
                lemma+=character
            if character=="\t":
                num_of_tabs += 1
        num_of_characters=0
        condition=""
        lenght_of_lemma=len(lemma)
        for i in lemma:
            if lemma[num_of_characters]==form[num_of_characters]:
                num_of_characters+=1
            if num_of_characters==lenght_of_lemma-1:
                condition="True"
        if condition !="True":
            print(form,lemma)
        #после просмотра записи разбора 2 часть задачи решилась по-другому, но так вроде симпатичнее и без всяких знаков неравенств
