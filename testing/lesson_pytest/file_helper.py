import os


class Session:
    def close(self):
        print('Closed sesion.')


class Api:

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = Session()

    def request(self, method, data):
        print('Executed', method)

    def close(self):
        print('Closing session')
        self.session.close()


class FileHelper:

    def __init__(self, api):
        self.api = api

    def remove_file(self, filepath):
        if os.path.isfile(filepath):
            print(f'Removing file {filepath!r}')
            os.unlink(filepath)

    def prepare_file(self, filepath):
        print(f'Preparing file {filepath!r} for upload')
        return bytes()

    def upload_file(self, filepath):
        data = self.prepare_file(filepath)
        self.api.request('POST', data)
