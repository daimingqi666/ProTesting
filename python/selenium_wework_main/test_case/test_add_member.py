from time import sleep

from python.selenium_wework_main.page.add_member import AddMember
from python.selenium_wework_main.page.main import Main
import pytest


class TestAddMember:
    def setup(self):
        self.main = Main()
    def test_addmember(self):
        add_member = self.main.goto_add_member().add_member()
       # add_member.add_member()
        sleep(2)
        assert 'abcesdffff' in AddMember(self.main._driver).get_member()



if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_add_member.py'])