import pytest

@pytest.mark.usefixtures("setup")
#@pytest.fixture()
class TestExample:

#    def setup():
#        print("I will be executing first ")
#        yield
 #       print("i will be executing last")
    def test_fixtureDemo0(self):
        print(" i will be execute steps in fixturedemo method ")

    def test_fixtureDemo1(self):
        print(" i will be execute steps in fixturedemo method ")

    def test_fixtureDemo2(self):
        print(" i will be execute steps in fixturedemo method ")

    def test_fixtureDemo3(self):
        print(" i will be execute steps in fixturedemo method ")
