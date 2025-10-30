class MortgageCalculator:
    def calculate_monthly_payment(self, loan_amount, annual_rate, years):
        if loan_amount <= 0:
            raise ValueError("Сумма кредита должна быть положительной")
        if annual_rate < 0:
            raise ValueError("Процентная ставка не может быть отрицательной")
        if years <= 0:
            raise ValueError("Срок кредита должен быть больше нуля")

        monthly_rate = annual_rate / 100 / 12  # месячная ставка в долях
        total_months = years * 12

        # Аннуитетная формула
        if monthly_rate == 0:
            return loan_amount / total_months

        monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate)**total_months) / \
                          ((1 + monthly_rate)**total_months - 1)

        return round(monthly_payment, 2)

    def total_payout(self, monthly_payment, years):
        return round(monthly_payment * years * 12, 2)

    def overpayment(self, loan_amount, monthly_payment, years):
        return self.total_payout(monthly_payment, years) - loan_amount
