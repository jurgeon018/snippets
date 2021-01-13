import unittest
from unittest import mock

import os
import tempfile

from main import rm


class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "w") as f:
            f.write("Delete me!")

    # def test_rm(self):
    #     rm(self.tmpfilepath)
    #     self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

    @mock.patch('main.os')
    def test_rm1(self, mock_os):
        rm("any path")
        mock_os.remove.assert_called_with("any path")

    @mock.patch('main.rm')
    def test_rm2(self, mock_rm):
        mock_rm("any path")
        mock_rm.assert_called_with("any path")

    @mock.patch('main.os.path')
    @mock.patch('main.os')
    def test_rm3(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False
        
        rm("any path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        rm("any path")
        
        mock_os.remove.assert_called_with("any path")
