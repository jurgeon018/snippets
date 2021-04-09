import pytest
import sys


@pytest.mark.skip(reason='skipped test example')
def test_skip():
    pass


@pytest.mark.skipif(sys.version_info > (3, 5), reason='required version')
def test_skip_id():
    pass


@pytest.mark.xfail(reason='wrond comprison', strict=True)
def test_fail_comparison():
    assert 1 == 0


@pytest.mark.xfail(raises=(AssertionError, TimeoutError))
def test_fail_exception():
    raise AssertionError
