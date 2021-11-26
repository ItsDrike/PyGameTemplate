#!/bin/sh

ALLOWED_LICENSES="GPL v3\
;GNU Library or Lesser General Public License (LGPL)\
;MIT License\
;BSD License\
;BSD 3-Clause\
;Apache Software License\
;Public Domain\
;ISC License (ISCL)\
;Mozilla Public License 2.0 (MPL 2.0)\
;Python Software Foundation License"

pip-licenses --allow-only "$ALLOWED_LICENSES"
