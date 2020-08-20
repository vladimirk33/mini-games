# Виселица
import random

# константы
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
---------
""",
"""
 ------
 |    |
 |    0
 |
 |
 |
 |
 |
---------
""",
"""
 ------
 |    |
 |    0
 |   -+-
 |
 |
 |
 |
---------
""",
"""
 ------
 |    |
 |    0
 |  /-+-
 |
 |
 |
 |
---------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |
 |
 |
 |
---------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |    |
 |
 |
 |
---------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |    |
 |   |
 |   |
 |
---------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |    |
 |   | |
 |   | |
 |
---------
""")
MAX_WRONG = len(HANGMAN) - 1
WORDS = ('питон', 'планшет', 'клавиатура', 'ноутбук', 'монитор', 'телефон',
         'виселица', 'натюрморт', 'подсветка', 'ответ', 'подстаканник')

# инициализация переменных
word = random.choice(WORDS).upper()
so_far = '-' * len(word)
wrong = 0
used = []

# начало игры
print('Добро пожаловать в игру \'Виселица\'. Удачи вам!')
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print(f'\nВы уже предлагали следующие буквы:\n{used}')
    print(f'\nОтгаданное вами в слове сейчас выглядит так:\n{so_far}')
    guess = input('\n\nВведите букву: ')
    guess = guess.upper()
    while guess in used:
        print(f'Вы уже предлагали букву {guess}.')
        guess = input('\n\nВведите букву: ')
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print(f'\nДа! Буква {guess} есть в слове!')
        # новая строка so_far с отгаданной буквой или буквами
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f'\nК сожалению, буквы {guess} нет в слове.')
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print('\nВас повесили!')
else:
    print('\nПоздравляем! Вы отгадали.')
print(f'\nБыло загадано слово "{word.lower().title()}".')
input('\n\nНажмите Enter, чтобы выйти.')
