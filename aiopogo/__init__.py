from .exceptions import PleaseInstallProtobufVersion3

__title__ = 'aiopogo'
__version__ = '1.6.0'
__author__ = 'David Christenson'
__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2017 David Christenson <https://github.com/Noctem>'

protobuf_version = 0
try:
    from google import protobuf
    protobuf_version = protobuf.__version__
except ImportError:
    raise PleaseInstallProtobufVersion3('Protobuf not found, install it.')

if int(protobuf_version[:1]) < 3:
    raise PleaseInstallProtobufVersion3('Protobuf 3 needed, you have {}'.format(protobuf_version))

from functools import partial

try:
    from ujson import dumps as _dumps, loads as json_loads
    json_dumps = partial(_dumps, escape_forward_slashes=False)
except ImportError:
    from json import dumps as _dumps, loads as json_loads
    from .utilities import JSONByteEncoder
    json_dumps = partial(_dumps, cls=JSONByteEncoder)

from .pgoapi import PGoApi
from .rpc_api import RpcApi
from .hash_server import HashServer

def close_sessions():
    RpcApi.sessions.close()
    HashServer.close_session()

def activate_hash_server(hash_token, conn_limit=300):
    HashServer.set_token(hash_token)
    HashServer.activate_session(conn_limit)
