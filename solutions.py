from pprint import pprint
from src.WordCounter import WordCounter
from src.TaxMan import TaxMan
from src.Calculator import Calculator 

# def ex1():
#     people_list = [
#     {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
#     {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
#     {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
# ]

# sort_people(people_list, 'weight', 'disc')
# print

def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.

if __name__ == '__main__':
    ex5()

def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())
    

if __name__ == '__main__':
    ex6()

def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

if __name__ == '__main__':
    ex7()
