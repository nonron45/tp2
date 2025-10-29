from unittest import result

import pytest
from  String_Calculator import string_Calculator1

def test_string_Calculator1_returns_empty():
    result = string_Calculator1("")
    assert result == 0


