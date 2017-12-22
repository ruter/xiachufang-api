import os
import multiprocessing


LOG_PATH = os.path.join(os.getcwd(), 'log/')

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

bind = '127.0.0.1:5000'
graceful_timeout = 30
preload_app = True
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2

loglevel = 'info'
accesslog = os.path.join(LOG_PATH, 'gunicorn_access.log') #访问日志文件
errorlog = os.path.join(LOG_PATH, 'gunicorn_error.log')   #错误日志文件
