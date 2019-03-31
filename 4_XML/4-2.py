import sys
import io
import urllib.request as req
from bs4 import BeautifuSoup
import os.path
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
