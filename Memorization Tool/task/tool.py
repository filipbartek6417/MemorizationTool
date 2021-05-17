flashcards = {}
while (inp1 := input(f'1. Add flashcards\n'
                     f'2. Practice flashcards\n'
                     f'3. Exit\n')) != '3':
    if inp1 == '1':
        # show the submenu
        while (inp2 := input(f'1. Add a new flashcard\n'
                             f'2. Exit\n')) != '2':
            if inp2 == '1':
                # add a flash card
                while (question := input('Question:\n')) == '':
                    pass
                while (answer := input('Answer:\n')) == '':
                    pass
                flashcards[question] = answer
            else:
                print(f'{inp2} is not an option')
    elif inp1 == '2':
        # iterate over all flashcards
        if flashcards:
            for key, value in flashcards.items():
                while (ans := input(f'Question: {key}\n'
                                    f'Please press "y" to see the answer '
                                    f'or press "n" to skip:\n')) not in ['y', 'n']:
                    pass
                if ans == 'y':
                    print(f'Answer: {value}')
        else:
            print('There is no flashcard to practice!')
    else:
        print(f'{inp1} is not an option')
print('Bye!')
