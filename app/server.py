import logging
import os
import re
import time
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("rasp")
RASP_ENABLED = os.getenv("RASP_ENABLED", "1") == "1"
