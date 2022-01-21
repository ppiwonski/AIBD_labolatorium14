import pytest
from bubblesort import bubble

testdata=[([1,5,2,5,3,8],[1,2,3,5,5,8]),
            ([1,1,1,1],[1,1,1,1]),
            ([5,6,-2,-3],[-3,-2,5,6])]
testdata1=[[]]
testdata2=[[1,5,2,5,3,'a']]
@pytest.mark.parametrize('sample,expected_output', testdata)

#sprawdzenie poprawności wyników
def test_bubble(sample,expected_output):
    assert bubble(sample) == expected_output


@pytest.mark.parametrize('sample', testdata1)
#sprawdzenie czy lista jest pusta
def test_bubble1(sample):
    got=bubble(sample)
    expected_output=[]
    assert got == expected_output


@pytest.mark.parametrize('sample', testdata2)
#sprawdzenie typów danych
def test_bubble2(sample):
    got=bubble(sample)
    expected_output=None
    assert got == expected_output