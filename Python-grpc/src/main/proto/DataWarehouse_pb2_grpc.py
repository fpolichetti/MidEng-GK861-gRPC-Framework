# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import DataWarehouse_pb2 as DataWarehouse__pb2


class DataWarehouseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.warehousing = channel.unary_unary(
                '/datawarehouse.DataWarehouseService/warehousing',
                request_serializer=DataWarehouse__pb2.WarehouseRequest.SerializeToString,
                response_deserializer=DataWarehouse__pb2.WarehouseResponse.FromString,
                )
        self.ping = channel.unary_unary(
                '/datawarehouse.DataWarehouseService/ping',
                request_serializer=DataWarehouse__pb2.PingRequest.SerializeToString,
                response_deserializer=DataWarehouse__pb2.PingResponse.FromString,
                )


class DataWarehouseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def warehousing(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataWarehouseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'warehousing': grpc.unary_unary_rpc_method_handler(
                    servicer.warehousing,
                    request_deserializer=DataWarehouse__pb2.WarehouseRequest.FromString,
                    response_serializer=DataWarehouse__pb2.WarehouseResponse.SerializeToString,
            ),
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=DataWarehouse__pb2.PingRequest.FromString,
                    response_serializer=DataWarehouse__pb2.PingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'datawarehouse.DataWarehouseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataWarehouseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def warehousing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datawarehouse.DataWarehouseService/warehousing',
            DataWarehouse__pb2.WarehouseRequest.SerializeToString,
            DataWarehouse__pb2.WarehouseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datawarehouse.DataWarehouseService/ping',
            DataWarehouse__pb2.PingRequest.SerializeToString,
            DataWarehouse__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
