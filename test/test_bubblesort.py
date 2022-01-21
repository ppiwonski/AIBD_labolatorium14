import pytest
from bubblesort import bubble

#przypadki testowe
testdata=[([1,5,2,5,3,8],[1,2,3,5,5,8]),
            ([1,1,1,1],[1,1,1,1]),
            ([5,6,-2,-3],[-3,-2,5,6])]
testdata1=[[]]
testdata2=[[1,5,2,5,3,'a']]

#sprawdzenie poprawności wyników
@pytest.mark.parametrize('sample,expected_output', testdata)
def test_bubble(sample,expected_output):
    assert bubble(sample) == expected_output

#sprawdzenie pustej listy
@pytest.mark.parametrize('sample', testdata1)
def test_bubble1(sample):
    got=bubble(sample)
    expected_output=[]
    assert got == expected_output

#sprawdzenie typów danych
@pytest.mark.parametrize('sample', testdata2)
def test_bubble2(sample):
    got=bubble(sample)
    expected_output=None
    assert got == expected_output