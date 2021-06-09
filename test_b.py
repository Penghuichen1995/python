import pytest
import yaml

class TestDemo1():
    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open('D:\\Users\\W9011218\\PycharmProjects\\pythonProject1\\venv\\test.yaml')))
    def test_answer(self,a,b):
            print(a+b)