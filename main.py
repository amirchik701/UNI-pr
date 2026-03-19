from proekt640Tursunov import most_frequent

if __name__== "__main__":
    choice  = input("1 - Находит число, которое встречается чаще всего \n \n Выбери функцию для запуска: ")

    if choice == "1":
        user_input = input("Введите числа: ")
        nums = [int(x) for x in user_input.split()]
        
        result = most_frequent(nums)
        
        if result is None:
            print("Недостаточно уникальных чисел")
        else:
            print("Второе уникальное число:", result)