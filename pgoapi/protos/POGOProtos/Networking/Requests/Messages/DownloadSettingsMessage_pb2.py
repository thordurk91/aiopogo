# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/DownloadSettingsMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/DownloadSettingsMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\nEPOGOProtos/Networking/Requests/Messages/DownloadSettingsMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"\'\n\x17\x44ownloadSettingsMessage\x12\x0c\n\x04hash\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DOWNLOADSETTINGSMESSAGE = _descriptor.Descriptor(
  name='DownloadSettingsMessage',
  full_name='POGOProtos.Networking.Requests.Messages.DownloadSettingsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='POGOProtos.Networking.Requests.Messages.DownloadSettingsMessage.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['DownloadSettingsMessage'] = _DOWNLOADSETTINGSMESSAGE

DownloadSettingsMessage = _reflection.GeneratedProtocolMessageType('DownloadSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADSETTINGSMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.DownloadSettingsMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.DownloadSettingsMessage)
  ))
_sym_db.RegisterMessage(DownloadSettingsMessage)


# @@protoc_insertion_point(module_scope)