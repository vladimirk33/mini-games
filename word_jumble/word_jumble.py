# Анаграммы
import random

# формирование анаграммы
WORDS = ('питон', 'планшет', 'клавиатура', 'ноутбук', 'монитор', 'телефон',
         'анаграмма', 'простая', 'сложная', 'ответ', 'подстаканник')
word = random.choice(WORDS)
correct = word
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[position + 1:]

# начало игры
print(
'''

                Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
        (Для выхода нажмите Enter, не вводя своего варианта)
'''
)
print(f'Вот анаграмма: {jumble}')
guess = input('\nПопробуйте отгадать исходное слово: ')
while guess != correct and guess != '':
    print('К сожалению, вы неправы.')
    guess = input('\nПопробуйте отгадать исходное слово: ')
if guess == correct:
    print('Да, именно так! Вы отгадали!\n')

print('Спасибо за игру.')
input('\n\nНажмите Enter, чтобы выйти.')
