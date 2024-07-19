import pytest


class TestClass:
    @pytest.mark.fifth
    def test_anime1(self):
        print("Running Anime 1")

    @pytest.mark.fourth
    def test_anime2(self):
        print("Running Anime 2")

    @pytest.mark.third
    def test_anime3(self):
        print("Running Anime 3")

    @pytest.mark.second
    def test_anime4(self):
        print("Running Anime 4")

    @pytest.mark.first
    def test_anime5(self):
        print("Running Anime 5")
