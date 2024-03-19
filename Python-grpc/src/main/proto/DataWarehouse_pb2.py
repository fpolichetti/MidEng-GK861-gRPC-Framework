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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x44\x61taWarehouse.proto\x12\rdatawarehouse\",\n\x10WarehouseRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x61uth\x18\x02 \x01(\x05\"\xe3\x01\n\x11WarehouseResponse\x12\x13\n\x0bwarehouseID\x18\x01 \x01(\x05\x12\x15\n\rwarehouseName\x18\x02 \x01(\t\x12\x19\n\x11warehouseLocation\x18\x03 \x01(\t\x12\x18\n\x10warehouseStorage\x18\x04 \x01(\x05\x12\x1d\n\x15warehouseParkingSlots\x18\x05 \x01(\x05\x12\x1d\n\x15warehouseAvailability\x18\x06 \x01(\x08\x12/\n\x0bproductData\x18\x07 \x03(\x0b\x32\x1a.datawarehouse.ProductData\"\xb2\x01\n\x0bProductData\x12\x11\n\tproductID\x18\x01 \x01(\x05\x12\x13\n\x0bproductName\x18\x02 \x01(\t\x12\x17\n\x0fproductCategory\x18\x03 \x01(\t\x12\x14\n\x0cproductPrice\x18\x04 \x01(\x01\x12\x14\n\x0cproductStock\x18\x05 \x01(\x05\x12\x19\n\x11productExpiryDate\x18\x06 \x01(\t\x12\x1b\n\x13productAvailability\x18\x07 \x01(\x08\"\x1f\n\x0bPingRequest\x12\x10\n\x08\x63lientID\x18\x01 \x01(\t\"\x1f\n\x0cPingResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xad\x01\n\x14\x44\x61taWarehouseService\x12R\n\x0bwarehousing\x12\x1f.datawarehouse.WarehouseRequest\x1a .datawarehouse.WarehouseResponse\"\x00\x12\x41\n\x04ping\x12\x1a.datawarehouse.PingRequest\x1a\x1b.datawarehouse.PingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DataWarehouse_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_WAREHOUSEREQUEST']._serialized_start=38
  _globals['_WAREHOUSEREQUEST']._serialized_end=82
  _globals['_WAREHOUSERESPONSE']._serialized_start=85
  _globals['_WAREHOUSERESPONSE']._serialized_end=312
  _globals['_PRODUCTDATA']._serialized_start=315
  _globals['_PRODUCTDATA']._serialized_end=493
  _globals['_PINGREQUEST']._serialized_start=495
  _globals['_PINGREQUEST']._serialized_end=526
  _globals['_PINGRESPONSE']._serialized_start=528
  _globals['_PINGRESPONSE']._serialized_end=559
  _globals['_DATAWAREHOUSESERVICE']._serialized_start=562
  _globals['_DATAWAREHOUSESERVICE']._serialized_end=735
# @@protoc_insertion_point(module_scope)
