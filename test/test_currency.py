from currency import calculate_savings, calculate_currency, calculate_daily_goal


def test_calculate_savings():
    assert calculate_savings(5000, 3000) == 2000


def test_calculate_currency():
    assert calculate_currency(100, 4) == 25


def test_calculate_daily_goal():
    assert calculate_daily_goal(1000, 10) == 100