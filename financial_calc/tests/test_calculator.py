from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax
def test_simple_interest():
   success , value = calculate_simple_interest(1000, 5, 3)
   assert success and value == 150.0
   success, value = calculate_simple_interest(2500, 7.5, 2)
   assert success and value == 375.0
   success, value = calculate_simple_interest(0, 5, 3)
   assert success and value == 0.0
   success, value = calculate_simple_interest(-1000, 5, 3)
   assert not success

def test_compound_interest():
    success, value = calculate_compound_interest(1000, 5, 3, 1)
    assert success and round(value, 2) == 1157.63
    success, value = calculate_compound_interest(1000, 5, 3, 12)
    assert success and round(value, 2) == 1161.47
    success, value = calculate_compound_interest(0, 5, 3)
    assert success and value == 0.0
    success, value = calculate_compound_interest(-1000, 5, 3)
    assert not success

def test_tax():
    success, value = calculate_tax(50000, 13)
    assert success and value == 6500.0
    success, value = calculate_tax(10000, 5.5)
    assert success and value == 550.0
    success, value = calculate_tax(0, 13)
    assert success and value == 0.0
    success, value = calculate_tax(10000, -5)
    assert not success