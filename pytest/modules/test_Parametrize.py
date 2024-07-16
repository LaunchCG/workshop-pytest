import pytest


class TestParametrize:
    @pytest.mark.parametrize("num1,num2", [(1, 1), (2, 2), (3, 5), (7, 9), (8, 8)])
    def test_parametrize(self, num1, num2):
        assert num1 == num2
