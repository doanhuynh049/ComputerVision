import random
from colorama import init, Fore

def guess_number():
    init()
    number = random.randint(1, 100)
    attempts = 0

    print(Fore.YELLOW + "Chào mừng bạn đến với trò chơi đoán số!")
    print("Tôi đã chọn một số từ 1 đến 100. Hãy cố gắng đoán xem đó là số nào.")

    while True:
        guess = int(input(Fore.CYAN + "Nhập số dự đoán của bạn: "))
        attempts += 1

        if guess < number:
            print(Fore.RED + "Số bạn đoán nhỏ hơn số tôi đã chọn. Hãy thử lại!")
        elif guess > number:
            print(Fore.RED + "Số bạn đoán lớn hơn số tôi đã chọn. Hãy thử lại!")
        else:
            print(Fore.GREEN + "Chúc mừng! Bạn đã đoán đúng số sau", attempts, "lần đoán.")
            break

guess_number()
