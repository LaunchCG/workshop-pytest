import pytest

class TestClass:
    @pytest.mark.parametrize('num1,num2', [(5, 5), (10, 30), (0, 0), (5, 20)])
    def test_calculation(self, num1, num2):
        assert num1 == num2