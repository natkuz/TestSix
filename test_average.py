import pytest
from average import find_average, comparison_average_lists

@pytest.mark.parametrize("a, expected", [
    ([10, 20, 30, 40, 50], 30.0),
    ([], 0),
    ([5], 5.0)
])
def test_find_average(a, expected):
    assert find_average(a) == expected

def test_find_average_typeerror():
    with pytest.raises(TypeError):
        find_average("Not a list")

@pytest.mark.parametrize("a, b, expected", [
    ([10, 20, 30, 40, 50], [1, 2, 3, 4, 5], "Первый список имеет большее среднее значение"),
    ([1, 2, 3, 4, 5], [10, 20, 30, 40, 50], "Второй список имеет большее среднее значение"),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Средние значения равны")
])
def test_comparison(a, b, expected):
    assert comparison_average_lists(a, b) == expected