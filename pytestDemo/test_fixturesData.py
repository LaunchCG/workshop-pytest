import pytest

from pytestDemo.BaseDemo import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])

        # print(dataLoad)
        # print(dataLoad[1])

