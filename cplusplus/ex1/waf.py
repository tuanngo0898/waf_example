#!/usr/bin/python

from __future__ import print_function
import subprocess
import os.path as p
import sys

d = p.dirname(p.realpath(__file__))
waf_light = p.join(d, '..', '..', 'modules', 'waf', 'waf-light') # Path to waf-light ../../modules/waf/waf-light

python = sys.executable

try:
    subprocess.check_call([python, waf_light] + sys.argv[1:])
except subprocess.CalledProcessError as e:
    if e.returncode != 2 or p.isfile(waf_light):
        sys.exit(1)

    print('Missing waf submodule. Trying to get it')

    try:
        subprocess.check_call(['git', 'submodule', 'update', '--init',
                               'modules/waf'])
    except subprocess.CalledProcessError:
        print('Could not update submodule', file=sys.stderr)
        sys.exit(1)

    print('Submodules OK, try running again')
