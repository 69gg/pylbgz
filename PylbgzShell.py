import os
import re

while True:
    cwd = os.getcwd()
    content = input(f"PylbgzShell{cwd} $ ")
    compress = re.match('^compress (.*)$', content)
    if compress:
