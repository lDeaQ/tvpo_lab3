import pytest
from mortgage import MortgageCalculator

@pytest.fixture
def calculator():
    return MortgageCalculator()

def test_zero_interest_rate(calculator):
    payment = calculator.calculate_monthly_payment(1_200_000, 0, 10)
    assert payment == 10_000  # 1.2 млн / 120 месяцев

def test_negative_loan_amount(calculator):
    with pytest.raises(ValueError, match="Сумма кредита должна быть положительной"):
        calculator.calculate_monthly_payment(-1_000_000, 8.5, 10)

def test_negative_rate(calculator):
    with pytest.raises(ValueError, match="Процентная ставка не может быть отрицательной"):
        calculator.calculate_monthly_payment(1_000_000, -5, 10)

def test_invalid_years(calculator):
    with pytest.raises(ValueError, match="Срок кредита должен быть больше нуля"):
        calculator.calculate_monthly_payment(1_000_000, 8.5, 0)

def test_total_payout(calculator):
    payment = 50_000
    total = calculator.total_payout(payment, 5)
    assert total == 3_000_000  # 50к * 12 * 5

def test_overpayment(calculator):
    over = calculator.overpayment(1_000_000, 20_000, 5)
    assert over == 200_000  # 20к*60 = 1.2 млн → переплата 200к

'''
6
7
8
9
dasdasdas
'''