from mortgage import MortgageCalculator

def main():
    calc = MortgageCalculator()
    print("Калькулятор ипотеки")
    while True:
        print("\n1. Рассчитать ипотеку")
        print("2. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                amount = float(input("Введите сумму кредита (₽): "))
                rate = float(input("Годовая процентная ставка (%): "))
                years = int(input("Срок кредита (лет): "))

                payment = calc.calculate_monthly_payment(amount, rate, years)
                total = calc.total_payout(payment, years)
                overpay = calc.overpayment(amount, payment, years)

                print("\nРезультаты:")
                print(f"Ежемесячный платёж: {payment:,.2f} ₽")
                print(f"Общая выплата: {total:,.2f} ₽")
                print(f"Переплата: {overpay:,.2f} ₽")

            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")

        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

'''
1
2
3
4
5
6



'''