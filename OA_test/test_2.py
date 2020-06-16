import pytest
class TestClass(object):
    def test_01(self):
        x = ["aaa","bbb"]
        print(111)
        assert "aaa" in x
    @pytest.mark.beta
    def test_02(self):
        x = "hello"
        assert hasattr(x, 'hello world')
    def test_03(self):
        assert 1 == 1