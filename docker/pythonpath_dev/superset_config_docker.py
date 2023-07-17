#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#

# The allowed translation for you app
LANGUAGES = {
    "zh": {"flag": "cn", "name": "Chinese"},
    "en": {"flag": "us", "name": "English"}
}

# Your application default translation path
BABEL_DEFAULT_FOLDER = 'superset/translations'

#---------------------------以下为增加的内容 
# Setup default language
BABEL_DEFAULT_LOCALE = 'zh'

# PUBLIC_ROLE_LIKE = "Gamma"

HTTP_HEADERS = {}

TALISMAN_ENABLED = False
# TALISMAN_CONFIG = {}
# TALISMAN_DEV_CONFIG = {}

PREFERRED_DATABASES = [
    "PostgreSQL",
    "MySQL",
    "Oracle",
    "Microsoft SQL Server",
]

WTF_CSRF_ENABLED = False


SECRET_KEY="uy2EEQlygElrEijl4DXg0gE81QgR88KZ6j6nlAuhwq3BJiZ1PInPm0Qv"

''' 
DEFAULT_FEATURE_FLAGS: dict[str, bool] = {
    "ENABLE_EXPLORE_JSON_CSRF_PROTECTION": False,  # deprecated
    "DASHBOARD_CACHE": False,  # deprecated
    "DASHBOARD_NATIVE_FILTERS": True,  # deprecated
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,  # deprecated
    "DASHBOARD_FILTERS_EXPERIMENTAL": True,  # deprecated
    "DASHBOARD_VIRTUALIZATION": False,
    "GLOBAL_ASYNC_QUERIES": True,
    "DRILL_TO_DETAIL": True,
    "DRILL_BY": True,
    "HORIZONTAL_FILTER_BAR": True,   
    "SSH_TUNNELING": False
}

GLOBAL_ASYNC_QUERIES_REDIS_CONFIG = {
    "port": 6379,
    "host": "127.0.0.1",
    "password": "",
    "db": 8,
    "ssl": False,
}

GLOBAL_ASYNC_QUERIES_REDIS_STREAM_PREFIX = "async-events-"
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT = 1000
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT_FIREHOSE = 1000000
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_NAME = "async-token"
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_SECURE = False
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_SAMESITE = None  
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_DOMAIN = None
GLOBAL_ASYNC_QUERIES_JWT_SECRET = "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
GLOBAL_ASYNC_QUERIES_TRANSPORT = "ws"
'''
