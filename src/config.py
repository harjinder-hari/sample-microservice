import os

TESTING = False
DEBUG = True
LOGFILE_PATH = os.environ.get("LOGFILE_PATH", "/tmp/error.log")
PURPOSE_OF_LIFE = os.environ.get("PURPOSE_OF_LIFE", "eat junk food :)")
SERVICE_PORT = os.environ.get("SERVICE_PORT", "5001")

