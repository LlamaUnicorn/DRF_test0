import pytest


class TestStringMethods:
    """Tests String Methods"""
    def test_upper(self):
        assert "foo".upper() == "FOO"

    def test_isupper(self):
        assert "FOO".isupper() is True, "Foo is not upper!"
        assert "Foo".isupper() is False

    def test_split(self):
        s = "hello world"
        assert s.split() == ['hello', 'world']
        with pytest.raises(TypeError):
            s.split(2)
