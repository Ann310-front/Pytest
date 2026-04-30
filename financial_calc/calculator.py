def calculate_simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        return (False, 'Ошибка: Аргументы должны быть неотрицательными')
    result1 = principal * rate * time / 100
    return (True, result1)

def calculate_compound_interest(principal, rate, time, n=1):
    if principal < 0 or rate < 0 or time < 0:
        return (False, 'Ошибка: Аргументы должны быть неотрицательными')
    if not isinstance(n, int) or n <= 0:
        return (False, "Ошибка: n должно быть целым положительным числом")
    result2 = principal * (1 + rate/(100*n))**(n*time)
    return (True, result2)

def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 100:
        return (False, "Ошибка: tax_rate должна быть между 0 и 100")
    result3 = amount * tax_rate / 100
    return (True, result3)
  



