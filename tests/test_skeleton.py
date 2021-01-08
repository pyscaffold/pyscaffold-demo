import pytest

from demo_project.skeleton import fib

__author__ = "John Doe"
__copyright__ = "John Doe"
__license__ = "MIT"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
