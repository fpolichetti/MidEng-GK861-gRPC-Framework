# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DataWarehouse.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x44\x61taWarehouse.proto\",\n\x10WarehouseRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x61uth\x18\x02 \x01(\x05\"\xb2\x01\n\x0bProductData\x12\x11\n\tproductID\x18\x01 \x01(\x05\x12\x13\n\x0bproductName\x18\x02 \x01(\t\x12\x17\n\x0fproductCategory\x18\x03 \x01(\t\x12\x14\n\x0cproductPrice\x18\x04 \x01(\x01\x12\x14\n\x0cproductStock\x18\x05 \x01(\x05\x12\x19\n\x11productExpiryDate\x18\x06 \x01(\x05\x12\x1b\n\x13productAvailability\x18\x07 \x01(\x08\"\xd5\x01\n\x11WarehouseResponse\x12\x13\n\x0bwarehouseID\x18\x01 \x01(\x05\x12\x15\n\rwarehouseName\x18\x02 \x01(\t\x12\x19\n\x11warehouseLocation\x18\x03 \x01(\t\x12\x18\n\x10warehouseStorage\x18\x04 \x01(\x05\x12\x1d\n\x15warehouseParkingSlots\x18\x05 \x01(\x05\x12\x1d\n\x15warehouseAvailability\x18\x06 \x01(\x08\x12!\n\x0bproductData\x18\x07 \x03(\x0b\x32\x0c.ProductData2N\n\x14\x44\x61taWarehouseService\x12\x36\n\x0bwarehousing\x12\x11.WarehouseRequest\x1a\x12.WarehouseResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DataWarehouse_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_WAREHOUSEREQUEST']._serialized_start=23
  _globals['_WAREHOUSEREQUEST']._serialized_end=67
  _globals['_PRODUCTDATA']._serialized_start=70
  _globals['_PRODUCTDATA']._serialized_end=248
  _globals['_WAREHOUSERESPONSE']._serialized_start=251
  _globals['_WAREHOUSERESPONSE']._serialized_end=464
  _globals['_DATAWAREHOUSESERVICE']._serialized_start=466
  _globals['_DATAWAREHOUSESERVICE']._serialized_end=544
# @@protoc_insertion_point(module_scope)
