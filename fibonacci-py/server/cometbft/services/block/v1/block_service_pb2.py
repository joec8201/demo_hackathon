# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cometbft/services/block/v1/block_service.proto
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
    'cometbft/services/block/v1/block_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cometbft.services.block.v1 import block_pb2 as cometbft_dot_services_dot_block_dot_v1_dot_block__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.cometbft/services/block/v1/block_service.proto\x12\x1a\x63ometbft.services.block.v1\x1a&cometbft/services/block/v1/block.proto2\xfc\x01\n\x0c\x42lockService\x12n\n\x0bGetByHeight\x12..cometbft.services.block.v1.GetByHeightRequest\x1a/.cometbft.services.block.v1.GetByHeightResponse\x12|\n\x0fGetLatestHeight\x12\x32.cometbft.services.block.v1.GetLatestHeightRequest\x1a\x33.cometbft.services.block.v1.GetLatestHeightResponse0\x01\x42=Z;github.com/cometbft/cometbft/api/cometbft/services/block/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.services.block.v1.block_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/cometbft/cometbft/api/cometbft/services/block/v1'
  _globals['_BLOCKSERVICE']._serialized_start=119
  _globals['_BLOCKSERVICE']._serialized_end=371
# @@protoc_insertion_point(module_scope)
