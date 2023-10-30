import Lab2

def test_find_min_max():
    list_input = [5, 66, 30, 50]
    correct_result = [5, 66]

    actual_result = Lab2.find_min_max(list_input)

    assert (actual_result == correct_result)


def test_calc_average():
    list_input = [5, 66, 30, 50]
    correct_result = 37.75

    actual_result = Lab2.calc_average(list_input)

    assert (actual_result == correct_result)


def test_calc_median_temperature():
    list_input = [5, 66, 30, 50]
    correct_result = 40

    actual_result = Lab2.calc_median_temperature(list_input)

    assert (actual_result == correct_result)
