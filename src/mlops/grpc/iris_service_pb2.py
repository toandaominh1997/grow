# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12iris_service.proto\"l\n\niris_param\x12\x0f\n\x02sl\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x0f\n\x02sw\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x0f\n\x02pl\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x0f\n\x02pw\x18\x04 \x01(\x02H\x03\x88\x01\x01\x42\x05\n\x03_slB\x05\n\x03_swB\x05\n\x03_plB\x05\n\x03_pw\"+\n\x0biris_output\x12\x12\n\x05value\x18\x01 \x01(\x02H\x00\x88\x01\x01\x42\x08\n\x06_value2:\n\tIrisModel\x12-\n\x0epredict_output\x12\x0b.iris_param\x1a\x0c.iris_output\"\x00\x62\x06proto3')



_IRIS_PARAM = DESCRIPTOR.message_types_by_name['iris_param']
_IRIS_OUTPUT = DESCRIPTOR.message_types_by_name['iris_output']
iris_param = _reflection.GeneratedProtocolMessageType('iris_param', (_message.Message,), {
  'DESCRIPTOR' : _IRIS_PARAM,
  '__module__' : 'iris_service_pb2'
  # @@protoc_insertion_point(class_scope:iris_param)
  })
_sym_db.RegisterMessage(iris_param)

iris_output = _reflection.GeneratedProtocolMessageType('iris_output', (_message.Message,), {
  'DESCRIPTOR' : _IRIS_OUTPUT,
  '__module__' : 'iris_service_pb2'
  # @@protoc_insertion_point(class_scope:iris_output)
  })
_sym_db.RegisterMessage(iris_output)

_IRISMODEL = DESCRIPTOR.services_by_name['IrisModel']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IRIS_PARAM._serialized_start=22
  _IRIS_PARAM._serialized_end=130
  _IRIS_OUTPUT._serialized_start=132
  _IRIS_OUTPUT._serialized_end=175
  _IRISMODEL._serialized_start=177
  _IRISMODEL._serialized_end=235
# @@protoc_insertion_point(module_scope)
