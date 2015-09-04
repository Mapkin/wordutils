from wordutils.utils import split_num

def test_split():
    assert split_num(1234, 2) == [12, 34]
    assert split_num(123, 2) == [1, 23]
    assert split_num(123, 4) == [123]
    assert split_num(1234567, 4) == [123, 4567]
