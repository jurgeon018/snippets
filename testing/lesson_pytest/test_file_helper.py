import os
from file_helper import FileHelper, Api
import pytest
from unittest import mock


# moved to conftest.py
# @pytest.fixture
# def temp_file(tmp_path):
#     f = tmp_path / 'filename.txt'
#     f.write_text('CONTENT')
#     return f


@pytest.fixture
def api():
    api = Api('api_key_secret')
    yield api
    api.session.close()


@pytest.fixture
def fh(api):
    fh = FileHelper(api=api)
    return fh


class TestFileHelper:

    def test_init(self):
        api = object()
        fh = FileHelper(api)
        assert fh.api == api

    def test_remove_file(self, fh, temp_file):
        api = object()
        fh = FileHelper(api)
        fh.remove_file(temp_file)
        assert os.path.exists(temp_file) is False

    # @mock.patch.object(FileHelper, 'prepare_file')
    @mock.patch.object(FileHelper, 'prepare_file', autospec=True)
    def test_file_upload(self, mocked_prepare_file):
        '''
        При autospec=True функция будет замокана,
        но будет вываливаливаться ошибка если будет передано
        неправильное количество параметров.
        '''
        fake_api = mock.MagicMock()
        # expected_data = object()
        # mocked_prepare_file.return_value = expected_data
        fake_filepath = 'fdsasdf'
        fh = FileHelper(fake_api)
        fh.upload_file(fake_filepath)
        # fake_api.request.assert_called()
        # fake_api.request.assert_called_once()
        fake_api.request.assert_called_once_with(
            'POST',
            mocked_prepare_file.return_value,
        )
        mocked_prepare_file.assert_called_once_with(
            fh,
            fake_filepath,
        )

    @mock.patch('file_helper.os')
    def test_uses_unlink_for_remove(self, mocked_fh_os, fh):
        filepath = 'sdfas'
        mocked_fh_os.path.isfile.return_value = True
        fh.remove_file(filepath)
        mocked_fh_os.unlink_assert_called_once_with(
            filepath
        )
