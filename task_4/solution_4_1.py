print("ID	form	lemma	что_то_ещё")
for smth in 'a'*10:
    num_of_tabs=0
    tab_1=0
    tab_2=0
    tab_3=0
    form=""
    lemma=""
    user_input = input()
    if user_input != "" and user_input[0] != "#":
        for i in user_input:
            if i == "\t":
                if tab_1==0:
                    tab_1=num_of_tabs
                else:
                    if tab_2==0:
                        tab_2=num_of_tabs
                    else:
                        if tab_3==0:
                            tab_3=num_of_tabs
            num_of_tabs+=1
        character_position=0
        for n in user_input:
            if tab_1 < character_position < tab_2:
                form+=n
            if tab_2 < character_position < tab_3:
                lemma+=n
            character_position+=1
        my_cool_condition = lemma != form
        if my_cool_condition == True:
            print(form, lemma)
