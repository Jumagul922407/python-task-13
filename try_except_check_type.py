# try_except_check_type.py

def check_input():
    value = input("Сан жазыңыз: ")

    try:
        number = int(value)
        print(f"{number} - бул сан.")
    except ValueError:
        print("Бул сан эмес!")

check_input()
