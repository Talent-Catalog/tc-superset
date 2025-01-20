# Overrides standard configuration
# - https://github.com/apache/superset/blob/master/superset/config.py
#
# These overridden values are based on sample
# https://github.com/apache/superset/blob/master/docker/pythonpath_dev/superset_config.py

# SECRET_KEY - always has to be overridden with a randomly generated unique
# string for this instance of Superset

SECRET_KEY = "NQU3OL6QGiyHVm8pEjMPDKSmIYqNE89tB3Bm41Cj8wZ36WP3fifiVRaM"

APP_NAME = "Talent Catalog Portal"
BRAND_NAME = "Talent Catalog"
APP_ICON = "/static/assets/images/tc-logo.png"

import logging
import os

from celery.schedules import crontab
from flask_caching.backends.filesystemcache import FileSystemCache

logger = logging.getLogger()

DATABASE_DIALECT = "postgresql"
DATABASE_USER = "tctalent"
DATABASE_PASSWORD = "tctalent"
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = "5432"
DATABASE_DB = "supersetdb"

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = (
  f"{DATABASE_DIALECT}://"
  f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
  f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
)

RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

# REDIS_HOST = os.getenv("REDIS_HOST", "redis")
# REDIS_PORT = os.getenv("REDIS_PORT", "6379")
# REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
# REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")
#
# CACHE_CONFIG = {
#   "CACHE_TYPE": "RedisCache",
#   "CACHE_DEFAULT_TIMEOUT": 300,
#   "CACHE_KEY_PREFIX": "superset_",
#   "CACHE_REDIS_HOST": REDIS_HOST,
#   "CACHE_REDIS_PORT": REDIS_PORT,
#   "CACHE_REDIS_DB": REDIS_RESULTS_DB,
# }
# DATA_CACHE_CONFIG = CACHE_CONFIG
#
#
# class CeleryConfig:
#   broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
#   imports = (
#     "superset.sql_lab",
#     "superset.tasks.scheduler",
#     "superset.tasks.thumbnails",
#     "superset.tasks.cache",
#   )
#   result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
#   worker_prefetch_multiplier = 1
#   task_acks_late = False
#   beat_schedule = {
#     "reports.scheduler": {
#       "task": "reports.scheduler",
#       "schedule": crontab(minute="*", hour="*"),
#     },
#     "reports.prune_log": {
#       "task": "reports.prune_log",
#       "schedule": crontab(minute=10, hour=0),
#     },
#   }
#
#
# CELERY_CONFIG = CeleryConfig

# FEATURE_FLAGS = {"ALERT_REPORTS": True}
# ALERT_REPORTS_NOTIFICATION_DRY_RUN = True
# WEBDRIVER_BASEURL = "http://superset:8088/"  # When using docker compose baseurl should be http://superset_app:8088/  # noqa: E501
# # The base URL for the email report hyperlinks.
# WEBDRIVER_BASEURL_USER_FRIENDLY = WEBDRIVER_BASEURL
# SQLLAB_CTAS_NO_LIMIT = True

#
# Optionally import superset_config_docker.py (which will have been included on
# the PYTHONPATH) in order to allow for local settings to be overridden
#
# try:
#   import superset_config_docker
#   from superset_config_docker import *  # noqa
#
#   logger.info(
#     f"Loaded your Docker configuration at " f"[{superset_config_docker.__file__}]"
#   )
# except ImportError:
#   logger.info("Using default Docker config...")
