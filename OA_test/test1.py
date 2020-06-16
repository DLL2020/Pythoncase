import pytest
class TestClass(object):
    def test_01(self):
        x = ["aaa","bbb"]
        print(111)
        assert "aaa" in x

    def test_02(self):
        x = "hello"
        assert x in 'hello world'

    @pytest.mark.A
    def test_03(self):
        assert 1 == 1






























