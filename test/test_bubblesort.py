import pytest
from bubblesort import bubble

testdata=[[1,5,2,5,3,8]]
testdata1=[[]]
@pytest.mark.parametrize('sample', testdata)

def test_bubble(sample):
    got=bubble(sample)
    expected_output=[1,2,3,5,5,8]
    assert got == expected_output


@pytest.mark.parametrize('sample', testdata1)

def test_bubble1(sample):
    got=bubble(sample)
    expected_output=[]
    assert got == expected_output