def func_calc() -> None:
    a = int(input('Введите первый коэффицент'))
    b = int(input('Введите второй коэффицент'))
    c = int(input('Введите третий коэффицент'))
    dis = b**2 - 4 * a * c
    if dis > 0:
        print  ("Уравнение имеет 2 корня")
        ans1 = (-b + (dis**0.5)) / (2 * a)
        ans2 = (-b - (dis**0.5)) / (2 * a)
        print(f'Первый корень = {int(ans1)}; Второй корень = {int(ans2)}')
    elif dis == 0:
        print('Уравнение имеет 1 корень')
        ans1 =  (-b) / (2 * a)
        print(f'Корень = {ans1}')
    else:
        print('Уравнение не имеет корней')



def main():
    func_calc()



if __name__ == "__main__":
    main()

