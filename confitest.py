import params as params
import pytest


@pytest.fixture()
def setup(request):
    print("I will be executing first ")
    yield
    print(" i will be executed last ")


@pytest.fixture(scope = "class")
def dataLoad():
    print(" user profile data is being created")
    return ["sai","yadav","saiyadav.com"]

@pytest.fixture(params=[("chrome", "sai","yadav"),("Firefox", "Sai"),("IE","Yadav")])
def crossBrowser(request):
    return request.param
print('@pytest.fixture(params=[("chrome", "sai","yadav"),("Firefox", "Sai"),("IE","Yadav")])')
print(params)