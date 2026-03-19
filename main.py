from proekt640Tursunov import most_frequent
from funk320Jahongir import funk320QJK
from Maksimfunk import funkMaksim  # Импорт функции из файла Maksimfunk.py

if __name__ == "__main__":
    choice = input(
        "1 - Находит число, которое встречается чаще всего\n"
        "2 - получение второго значения\n"
        "3 - сумма двух чисел\n\n"
        "Выбери функцию для запуска: "
    )

    if choice == "1":
        user_input = input("Введите числа: ")
        nums = [int(x) for x in user_input.split()]
        
        result = most_frequent(nums)
        
        if result is None:
            print("Недостаточно уникальных чисел")
        else:
            print("Самое частое число:", result)

    elif choice == "2":
        user_input = input("Введите числа через пробел: ")
        nums = [int(x) for x in user_input.split()]

        result = funk320QJK(nums)

        if result is None:
            print("Второго по величине элемента нет")
        else:
            print("Второй по величине элемент:", result)

    elif choice == "3":
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))

        result = funkMaksim(x, y)
        print("Сумма:", result)