import pytest
import yaml
def inc(x):
    return int(x) + 1
class TestDemo1():
    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open('D:\\Users\\W9011218\\PycharmProjects\\pythonProject1\\venv\\test.yaml')))
    def test_answer(self,a,b):
        print(a+b)
def test_answer1(self):
    assert inc(4) == 5
@pytest.fixture()
def login():
    u = 'addad'
    p = 'dada'
    return  (u+p)
class TestDemo2():
    def test_a(self,login):
        print('a{}'.format(login))

    def test_b(self):
        print('b')

    def test_c(self):
        print('c')
if __name__ == '__main__':
    pytest.main(['test_a.py::TestDemo1','-v'])

