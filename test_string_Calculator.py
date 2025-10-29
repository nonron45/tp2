import pytest
from  String_Calculator import string_Calculator1
@pytest.mark.parametrize("n, expected_result",[("",""),("0",0),("1",1),("2",2),("3",3)])
def test_string_Calculator1_returns_empty(n:str, expected_result:int):
    result = string_Calculator1(n)
    assert result == expected_result


