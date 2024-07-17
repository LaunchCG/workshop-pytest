import pytest
import logging

logger = logging.getLogger()


def add_one(x):
    return x + 1


@pytest.mark.parametrize('addend', [1, 3, 5])
def test_add_one_with_one_param(addend):
    expected_sum = addend
    expected_sum += 1
    assert add_one(addend) == expected_sum


@pytest.mark.parametrize('numbers', [
    [1, 2],
    [3, 4],
    [5, 6],
])
def test_add_one_with_param_list(number_list):
    addend, expected_sum = number_list
    assert add_one(addend) == expected_sum


@pytest.mark.parametrize('addend, expected_sum', [
    (1, 2),
    (3, 4),
    (5, 6),
])
def test_add_one_with_tuple(addend, expected_sum):
    assert add_one(addend) == expected_sum


addend_list = [1, 3, 5]


@pytest.mark.parametrize('addend', addend_list)
def test_add_one_var_param(addend):
    expected_sum = addend
    expected_sum += 1
    assert add_one(addend) == expected_sum


def increment_by_one(x):
    x += 1
    return x


@pytest.mark.parametrize('addend', [1, 3, 5])
@pytest.mark.parametrize('expected_sum', [2, 4, 6])
def test_add_one_two_params(addend, expected_sum):
    if increment_by_one(addend) == expected_sum:
        assert add_one(addend) == expected_sum
    else:
        pytest.skip("Skipping, as addend was not 1 less than expected sum")


def multiply_by_two(x):
    return x * 2


@pytest.mark.parametrize('func_product', [
    multiply_by_two(1),
    multiply_by_two(2),
])
@pytest.mark.parametrize('func_sum', [
    add_one(1),
    add_one(3),
])
def test_add_one_with_decrement_func(func_sum, func_product):
    if func_product - func_sum == 0:
        assert func_sum == func_product
    else:
        pytest.skip("Skipping, as product needs to be of value 2")


@pytest.fixture(params=addend_list)
def addend(request):
    return request.param


def test_add_one_with_fixture_one_param(addend):
    expected_sum = addend
    expected_sum += 1
    assert add_one(addend) == expected_sum


@pytest.fixture(params=[[1, 2], [3, 4], [5, 6]])
def number_list(request):
    return request.param


def test_add_one_with_pytest_fixture_list(number_list):
    addend, expected_sum = number_list
    assert add_one(addend) == expected_sum










