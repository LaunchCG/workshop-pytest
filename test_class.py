import pytest

class TestClass:
    
    @pytest.mark.one
    def test_one(self):
        x = "this"
        assert "h" in x
    
    @pytest.mark.two
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")