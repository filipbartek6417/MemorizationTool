from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Flashcard(Base):  # Declaration of the db table
    __tablename__ = 'flashcard'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box_number = Column(Integer, default=1)


# session.query(Flashcard).delete()  # These 2 lines clear the db
# session.commit()
Base.metadata.create_all(engine)  # Initializes the db

while (inp1 := input(f'1. Add flashcards\n'
                     f'2. Practice flashcards\n'
                     f'3. Exit\n')) != '3':
    if inp1 == '1':
        # show the submenu
        while (inp2 := input(f'1. Add a new flashcard\n'
                             f'2. Exit\n')) != '2':
            if inp2 == '1':
                # add a flash card to db
                while (question := input('Question:\n')) == '':
                    pass
                while (answer := input('Answer:\n')) == '':
                    pass
                session.add(Flashcard(question=question, answer=answer))
                session.commit()
            else:
                print(f'{inp2} is not an option')
    elif inp1 == '2':
        # iterate over all flashcards from db
        if flashcards := session.query(Flashcard).all():
            for card in flashcards:
                print(f'Question: {card.question}:')
                while (ans := input(f'press "y" to see the answer:\n'
                                    f'press "n" to skip:\n'
                                    f'press "u" to update:\n')) not in ['y', 'n', 'u']:
                    print(f'{ans} is not an option')
                if ans == 'u':
                    while (opt := input(f'press "d" to delete the flashcard:\n'
                                        f'press "e" to edit the flashcard:\n')) not in ['d', 'e']:
                        print(f'{opt} is not an option')
                    if opt == 'd':
                        # delete the flashcard
                        session.delete(card)
                    else:
                        # edit the flashcard
                        # I haven't found a reasonable way to iterate
                        # so I decided to do it one-by-one
                        if (new_question := input(f'current question: {card.question}\n'
                                                  f'please write a new question:\n')) != '':
                            card.question = new_question
                        if (new_answer := input(f'current answer: {card.answer}\n'
                                                f'please write a new answer:\n')) != '':
                            card.answer = new_answer
                else:
                    # if not updating
                    if ans == 'y':
                        print(f'Answer: {card.answer}')
                    while (cor := input(f'press "y" if your answer is correct:\n'
                                        f'press "n" if your answer is wrong:\n'))\
                            not in ['y', 'n']:
                        print(f'{cor} is not an option')
                    if cor == 'y':
                        # increase and delete by card numbers
                        card.box_number += 1
                        if card.box_number > 3:
                            session.delete(card)
                    else:
                        # if failed, return to 1
                        card.box_number = 1
                session.commit()
        else:
            print('There is no flashcard to practice!')
    else:
        print(f'{inp1} is not an option')
print('Bye!')
