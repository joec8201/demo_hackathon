# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cometbft/statesync/v1/types.proto
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
    'cometbft/statesync/v1/types.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cometbft/statesync/v1/types.proto\x12\x15\x63ometbft.statesync.v1\"\xde\x02\n\x07Message\x12V\n\x11snapshots_request\x18\x01 \x01(\x0b\x32\'.cometbft.statesync.v1.SnapshotsRequestH\x00R\x10snapshotsRequest\x12Y\n\x12snapshots_response\x18\x02 \x01(\x0b\x32(.cometbft.statesync.v1.SnapshotsResponseH\x00R\x11snapshotsResponse\x12J\n\rchunk_request\x18\x03 \x01(\x0b\x32#.cometbft.statesync.v1.ChunkRequestH\x00R\x0c\x63hunkRequest\x12M\n\x0e\x63hunk_response\x18\x04 \x01(\x0b\x32$.cometbft.statesync.v1.ChunkResponseH\x00R\rchunkResponseB\x05\n\x03sum\"\x12\n\x10SnapshotsRequest\"\x8b\x01\n\x11SnapshotsResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x16\n\x06\x66ormat\x18\x02 \x01(\rR\x06\x66ormat\x12\x16\n\x06\x63hunks\x18\x03 \x01(\rR\x06\x63hunks\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash\x12\x1a\n\x08metadata\x18\x05 \x01(\x0cR\x08metadata\"T\n\x0c\x43hunkRequest\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x16\n\x06\x66ormat\x18\x02 \x01(\rR\x06\x66ormat\x12\x14\n\x05index\x18\x03 \x01(\rR\x05index\"\x85\x01\n\rChunkResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x16\n\x06\x66ormat\x18\x02 \x01(\rR\x06\x66ormat\x12\x14\n\x05index\x18\x03 \x01(\rR\x05index\x12\x14\n\x05\x63hunk\x18\x04 \x01(\x0cR\x05\x63hunk\x12\x18\n\x07missing\x18\x05 \x01(\x08R\x07missingB8Z6github.com/cometbft/cometbft/api/cometbft/statesync/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.statesync.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/cometbft/cometbft/api/cometbft/statesync/v1'
  _globals['_MESSAGE']._serialized_start=61
  _globals['_MESSAGE']._serialized_end=411
  _globals['_SNAPSHOTSREQUEST']._serialized_start=413
  _globals['_SNAPSHOTSREQUEST']._serialized_end=431
  _globals['_SNAPSHOTSRESPONSE']._serialized_start=434
  _globals['_SNAPSHOTSRESPONSE']._serialized_end=573
  _globals['_CHUNKREQUEST']._serialized_start=575
  _globals['_CHUNKREQUEST']._serialized_end=659
  _globals['_CHUNKRESPONSE']._serialized_start=662
  _globals['_CHUNKRESPONSE']._serialized_end=795
# @@protoc_insertion_point(module_scope)
