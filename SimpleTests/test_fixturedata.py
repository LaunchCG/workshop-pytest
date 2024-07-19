import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_extractDataLoad(self, dataLoad):
        print(dataLoad)
