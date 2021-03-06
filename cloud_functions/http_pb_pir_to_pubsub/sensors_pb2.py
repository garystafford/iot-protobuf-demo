# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensors.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensors.proto',
  package='sensors',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rsensors.proto\x12\x07sensors\"\\\n\tSensorDHT\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\x12\x1e\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x10.sensors.DataDHT\"0\n\x07\x44\x61taDHT\x12\x13\n\x0btemperature\x18\x01 \x01(\x01\x12\x10\n\x08humidity\x18\x02 \x01(\x01\"\\\n\tSensorPIR\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\x12\x1e\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x10.sensors.DataPIR\"\x19\n\x07\x44\x61taPIR\x12\x0e\n\x06motion\x18\x01 \x01(\x08\"`\n\x0bSensorLight\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\x12 \n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x12.sensors.DataLight\"\x1a\n\tDataLight\x12\r\n\x05light\x18\x01 \x01(\x08\x62\x06proto3')
)




_SENSORDHT = _descriptor.Descriptor(
  name='SensorDHT',
  full_name='sensors.SensorDHT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='sensors.SensorDHT.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sensors.SensorDHT.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensors.SensorDHT.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sensors.SensorDHT.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=118,
)


_DATADHT = _descriptor.Descriptor(
  name='DataDHT',
  full_name='sensors.DataDHT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperature', full_name='sensors.DataDHT.temperature', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='sensors.DataDHT.humidity', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=168,
)


_SENSORPIR = _descriptor.Descriptor(
  name='SensorPIR',
  full_name='sensors.SensorPIR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='sensors.SensorPIR.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sensors.SensorPIR.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensors.SensorPIR.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sensors.SensorPIR.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=262,
)


_DATAPIR = _descriptor.Descriptor(
  name='DataPIR',
  full_name='sensors.DataPIR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='motion', full_name='sensors.DataPIR.motion', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=289,
)


_SENSORLIGHT = _descriptor.Descriptor(
  name='SensorLight',
  full_name='sensors.SensorLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='sensors.SensorLight.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sensors.SensorLight.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensors.SensorLight.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sensors.SensorLight.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=387,
)


_DATALIGHT = _descriptor.Descriptor(
  name='DataLight',
  full_name='sensors.DataLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='light', full_name='sensors.DataLight.light', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=415,
)

_SENSORDHT.fields_by_name['data'].message_type = _DATADHT
_SENSORPIR.fields_by_name['data'].message_type = _DATAPIR
_SENSORLIGHT.fields_by_name['data'].message_type = _DATALIGHT
DESCRIPTOR.message_types_by_name['SensorDHT'] = _SENSORDHT
DESCRIPTOR.message_types_by_name['DataDHT'] = _DATADHT
DESCRIPTOR.message_types_by_name['SensorPIR'] = _SENSORPIR
DESCRIPTOR.message_types_by_name['DataPIR'] = _DATAPIR
DESCRIPTOR.message_types_by_name['SensorLight'] = _SENSORLIGHT
DESCRIPTOR.message_types_by_name['DataLight'] = _DATALIGHT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorDHT = _reflection.GeneratedProtocolMessageType('SensorDHT', (_message.Message,), dict(
  DESCRIPTOR = _SENSORDHT,
  __module__ = 'sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensors.SensorDHT)
  ))
_sym_db.RegisterMessage(SensorDHT)

DataDHT = _reflection.GeneratedProtocolMessageType('DataDHT', (_message.Message,), dict(
  DESCRIPTOR = _DATADHT,
  __module__ = 'sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensors.DataDHT)
  ))
_sym_db.RegisterMessage(DataDHT)

SensorPIR = _reflection.GeneratedProtocolMessageType('SensorPIR', (_message.Message,), dict(
  DESCRIPTOR = _SENSORPIR,
  __module__ = 'sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensors.SensorPIR)
  ))
_sym_db.RegisterMessage(SensorPIR)

DataPIR = _reflection.GeneratedProtocolMessageType('DataPIR', (_message.Message,), dict(
  DESCRIPTOR = _DATAPIR,
  __module__ = 'sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensors.DataPIR)
  ))
_sym_db.RegisterMessage(DataPIR)

SensorLight = _reflection.GeneratedProtocolMessageType('SensorLight', (_message.Message,), dict(
  DESCRIPTOR = _SENSORLIGHT,
  __module__ = 'sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensors.SensorLight)
  ))
_sym_db.RegisterMessage(SensorLight)

DataLight = _reflection.GeneratedProtocolMessageType('DataLight', (_message.Message,), dict(
  DESCRIPTOR = _DATALIGHT,
  __module__ = 'sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensors.DataLight)
  ))
_sym_db.RegisterMessage(DataLight)


# @@protoc_insertion_point(module_scope)
