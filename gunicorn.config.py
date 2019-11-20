"""Gunicorn configuration."""

bind = '0.0.0.0:5000'
workers = 2
threads = 4
worker_class = 'gthread'
accesslog = '-'