# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cometbft/types/v1beta1/block.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'cometbft/types/v1beta1/block.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cometbft.types.v1beta1 import types_pb2 as cometbft_dot_types_dot_v1beta1_dot_types__pb2
from cometbft.types.v1beta1 import evidence_pb2 as cometbft_dot_types_dot_v1beta1_dot_evidence__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cometbft/types/v1beta1/block.proto\x12\x16\x63ometbft.types.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\"cometbft/types/v1beta1/types.proto\x1a%cometbft/types/v1beta1/evidence.proto\"\x86\x02\n\x05\x42lock\x12<\n\x06header\x18\x01 \x01(\x0b\x32\x1e.cometbft.types.v1beta1.HeaderB\x04\xc8\xde\x1f\x00R\x06header\x12\x36\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.cometbft.types.v1beta1.DataB\x04\xc8\xde\x1f\x00R\x04\x64\x61ta\x12\x46\n\x08\x65vidence\x18\x03 \x01(\x0b\x32$.cometbft.types.v1beta1.EvidenceListB\x04\xc8\xde\x1f\x00R\x08\x65vidence\x12?\n\x0blast_commit\x18\x04 \x01(\x0b\x32\x1e.cometbft.types.v1beta1.CommitR\nlastCommitB9Z7github.com/cometbft/cometbft/api/cometbft/types/v1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.types.v1beta1.block_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cometbft/cometbft/api/cometbft/types/v1beta1'
  _globals['_BLOCK'].fields_by_name['header']._loaded_options = None
  _globals['_BLOCK'].fields_by_name['header']._serialized_options = b'\310\336\037\000'
  _globals['_BLOCK'].fields_by_name['data']._loaded_options = None
  _globals['_BLOCK'].fields_by_name['data']._serialized_options = b'\310\336\037\000'
  _globals['_BLOCK'].fields_by_name['evidence']._loaded_options = None
  _globals['_BLOCK'].fields_by_name['evidence']._serialized_options = b'\310\336\037\000'
  _globals['_BLOCK']._serialized_start=160
  _globals['_BLOCK']._serialized_end=422
# @@protoc_insertion_point(module_scope)
