# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
#
# =============================================================================
#              _   _ _____ _____ ____ ___       _             __
#  _ __  _   _| | | |_   _|_   _|  _ \_ _|_ __ | |_ ___ _ __ / _| __ _  ___ ___
# | '_ \| | | | |_| | | |   | | | |_) | || '_ \| __/ _ \ '__| |_ / _` |/ __/ _ \
# | |_) | |_| |  _  | | |   | | |  __/| || | | | ||  __/ |  |  _| (_| | (_|  __/
# | .__/ \__, |_| |_| |_|   |_| |_|  |___|_| |_|\__\___|_|  |_|  \__,_|\___\___|
# |_|    |___/
#
# =============================================================================
# Authors:						Patrick Lehmann
#
# Python package:	    An interface for HTTP Requests and Responses.
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2019 Patrick Lehmann - Bötzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
#
from typing import Dict


class Response():
	_headers :          Dict =  None
	_contentKind :      str =   None
	_contentEncoding :  str =   None
	_contentType :      str =   None
	_content =                  None


class JSONResponse(Response):


	def __init__(self):
		super().__init__()
