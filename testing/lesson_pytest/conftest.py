import pytest


@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('CONTENT')
    return f
