#!/usr/bin/env python3
#
# An example hgweb CGI script, edit as necessary
# See also https://mercurial-scm.org/wiki/PublishingRepositories

# Path to repo or hgweb config to serve (see 'hg help hgweb')
import os
config = os.environ.get("HGWEB_CONFIG", "/path/to/repo/or/config").encode('utf-8')

# Uncomment and adjust if Mercurial is not installed system-wide
# (consult "installed modules" path from 'hg debuginstall'):
# import sys; sys.path.insert(0, "/path/to/python/lib")

# Uncomment to send python tracebacks to the browser if an error occurs:
# import cgitb; cgitb.enable()

from mercurial import demandimport

demandimport.enable()
from mercurial.hgweb import hgweb, wsgicgi

application = hgweb(config)
wsgicgi.launch(application)
