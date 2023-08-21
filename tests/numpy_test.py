import pytest
import numpy as np
from testbook import testbook


@pytest.fixture(scope="module")
def tb():
    with testbook("./python-exercises.ipynb", execute=True) as tb:
        yield tb

def test_exercise1(tb):
    get_full_names = tb.ref("get_full_names")
    first_names = np.array(["Bob", "Jane", "Mallory"])
    last_names = np.array(["Smith", "Jones", "Williams"])
    try:
        assert np.array_equal(get_full_names(first_names, last_names), np.array(['Bob Smith' 'Jane Jones' 'Mallory Williams']))
    except AssertionError as e:
        print(e)