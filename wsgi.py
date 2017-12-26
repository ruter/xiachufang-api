from gevent import monkey
monkey.patch_all()

from app import api
from gunicorn.app.base import Application


class ApiApplication(Application):
    def load_config(self):
        self.load_config_from_module_name_or_filename('config/gunicorn.py')

    def load(self):
        return api.server.app


if __name__ == '__main__':
    ApiApplication().run()
