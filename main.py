from proekt640Tursunov import most_frequent
from funk320Jahongir import funk320QJK

if __name__== "__main__":
    choice  = input("1 - Находит число, которое встречается чаще всего \n2 - получение второго значения \n \n Выбери функцию для запуска: ")

    if choice == "1":
        user_input = input("Введите числа: ")
        nums = [int(x) for x in user_input.split()]
        
        result = most_frequent(nums)
        
        if result is None:
            print("Недостаточно уникальных чисел")
        else:
            print("Второе уникальное число:", result)    

    elif choice == "2":
        user_input = input("Введите числа через пробел: ")

        nums = [int(x) for x in user_input.split()]

        result = funk320QJK(nums)

        if result is None:
            print("Второго по величине элемента нет")
        else:
            print("Второй по величине элемент:", result)