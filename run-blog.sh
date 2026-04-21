#!/bin/bash
cd /root/.openclaw/workspace/Nub-1-Blog
pip3 install requests -q 2>/dev/null
python3 solar-blog-generator.py --auto
