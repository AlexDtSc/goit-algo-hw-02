##### ДЗ. Тема 1. Що таке алгоритми? Вступ до концепції алгоритмів
##### ДЗ. Тема 2. Основні структури даних



### Завдання 1
'''

Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.



Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для системи обробки заявок:

import Queue

Створити чергу заявок
queue = Queue()

Функція generate_request():
    Створити нову заявку
    Додати заявку до черги

Функція process_request():
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста

Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок



У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує нові заявки та додає їх до черги, та process_request(), яка обробляє заявки, видаляючи їх із черги. Головний цикл програми виконує ці функції, імітуючи постійний потік нових заявок та їх обробку.
'''

import queue
import time
import random

def generate_request(request_queue, request_id):
    request_data = f'Заявка № {request_id}'
    request_queue.put(request_data)
    print(f'Згенеровано нову заявку: {request_data}')


def process_request(request_queue):
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f'Обробка заявки: {request_data}')
        # Симуляція затримки обробки запиту
        time.sleep(random.uniform(0.5, 2.0))
    else:
        print('Черга порожня. Немає заявок для обробки')


def main():
    request_queue = queue.Queue()
    request_id = 0

    try:
        while True:
            time.sleep(1) # Симуляція часу між генерацією заявок

            # Генерування нових заявок
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)

            # Обробка заявок
            if random.choice([True, False]):
                process_request(request_queue)
    
    except KeyboardInterrupt:
        print('\nПрограма завершена користувачем')

if __name__ == '__main__':
    main()


'Примітка:'
'Програма виконується автоматично після запуску виконання файлу. '
'Щоб зупинити програму і завершити її виконання треба натиснути Ctrl + C у терміналі або командному рядку, де вона запущена - відбудеться KeyboardInterrupt'




### Завдання 2

'''
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, 
так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.

Код виконується, використано deque з модуля collections у Python.
Програма перевіряє, чи є заданий рядок паліндромом, враховуючи рядки з парною та непарною кількістю символів, та є нечутливою до регістру та пробілів.
'''

import re
from collections import deque

def is_palindrome(string) -> bool:
    modified_string = re.sub(r'[^a-zA-Z]', '', string).lower()   # прибираємо всі символи окрім буквенних (в т.ч. коми, пробіли тощо) та приводимо до нижнього регістру
    q = deque(modified_string)                                   # перетворюємо в двосторонню чергу (по факту в список з двох сторін редагуємий)
    while len(q) > 1:                                            # доки довжина q більше 1
        if q.popleft() != q.pop():
            return False
    return True                                                  # True - паліндром, якщо q.popleft() == q.pop(), або довжина в q залишилося 0 або 1 символів


# === ТЕСТИ ===

def test_true_palindromes():
    # Навмисно
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Madam In Eden, I'm Adam") == True, "Провалено: 'Madam In Eden, I'm Adam'"
    assert is_palindrome("A Santa at NASA") == True, "Провалено: 'A Santa at NASA'"

def test_not_palindromes():
    # Не паліндроми
    assert is_palindrome("Python") == False, "Провалено: 'Python'"
    assert is_palindrome("Opera") == False, "Провалено: 'Opera'"

def test_true_palindromes_with_punctuation():
    # Із пунктуацією
    assert is_palindrome("Was it a car or a cat I saw?") == True, "Провалено: 'Was it a car or a cat I saw?'"
    assert is_palindrome("No 'x' in Nixon") == True, "Провалено: 'No 'x' in Nixon'"

def test_short_palindromes():
    # Короткі рядки та пустий рядок
    assert is_palindrome("a") == True, "Провалено: 'a'"
    assert is_palindrome("") == True, "Провалено: пустий рядок"

def test_mixed_upper_lower():
    # Змішані регістри
    assert is_palindrome("Eva, Can I Stab Bats In A Cave?") == True, "Провалено: 'Eva, Can I Stab Bats In A Cave?'"
    assert is_palindrome("Mr. Owl Ate My Metal Worm") == True, "Провалено: 'Mr. Owl Ate My Metal Worm'"



# === ЗАПУСК ТЕСТІВ ===

if __name__ == "__main__":
    test_true_palindromes()
    test_not_palindromes()
    test_true_palindromes_with_punctuation()
    test_short_palindromes()
    test_mixed_upper_lower()
    print("✅ Усі тести пройдено успішно!")

    

### Завдання 3

'''
Завдання 3 (необов'язкове завдання)

У багатьох мовах програмування ми маємо справу з виразами, виділеними символами-розділювачами, такими як круглі ( ), квадратні [ ] або фігурні дужки { }.



Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.

 💡 Використовуйте стек, щоб запам'ятати відкриті в даний момент символи-розділювачі.


Приклад очікуваного результату:

( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично
( 23 ( 2 - 3);: Несиметрично
( 11 }: Несиметрично


Завдання 3 (необов'язкове завдання):
Завдання є додатковим, тому не оцінюється, проте, за бажанням, ви можете отримати конструктивний зворотний зв'язок від ментора.
'''

import re

def check_brackets(expression):                               
    # Очищаємо рядок: залишаємо лише дужки
    brackets = re.sub(r'[^\[\]\(\)\{\}]', '', expression)
    
    # Словник відповідностей
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    # Стек для відкритих дужок
    stack = []
    
    for char in brackets:                                          # 1 проходимо по кожному символу у виразі.
        if char in '([{':                                           # 1.1 Якщо символ дорівнює одну з видів відкритих дужок ([{
            stack.append(char)                                       #  1.1.1 всі відкриті дужки кладемо у стек
        elif char in ')]}':                                         # 1.2 Якщо символ дорівнює одну з видів закритих дужок )]}
            if not stack or stack[-1] != bracket_pairs[char]:        # 1.2.1 Або стек порожній (Якщо ми першою зустріли закриту дужку, але ще не було жодної відкритої, то це вже помилка) або якщо натрапляємо на закриту дужку — перевіряємо, чи вона відповідає останній відкритій
                return f"{expression}: Несиметрично"                  # 1.2.1.1 якщо ні — вираз несиметричний.
            stack.pop()                                              # 1.2.2 Закрита правильна — тому останню відкриту дужку прибираємо зі стеку
    
    # Якщо після проходу стек порожній — дужки симетричні
    if not stack:                                                 # Якщо після проходу стек порожній — усе збалансовано.
        return f"{expression}: Симетрично"
    else:
        return f"{expression}: Несиметрично"

# Тести
examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for ex in examples:
    print(check_brackets(ex))
