#!/usr/bin/env python3
import subprocess
import sys

# Install requests first
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', '-q'])

# Now run the blog generator
import os
os.chdir('/root/.openclaw/workspace/Nub-1-Blog')
exec(open('solar-blog-generator.py').read(), {'__name__': '__main__', '--auto': None})
