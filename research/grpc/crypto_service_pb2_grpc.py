# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import crypto_service_pb2 as crypto__service__pb2


class GExchangeStub(object):
    """Service definition for GExchange
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_price = channel.unary_unary(
                '/GExchange/get_price',
                request_serializer=crypto__service__pb2.cryptocurrency.SerializeToString,
                response_deserializer=crypto__service__pb2.market_price.FromString,
                )
        self.get_maxprice = channel.unary_unary(
                '/GExchange/get_maxprice',
                request_serializer=crypto__service__pb2.market_price.SerializeToString,
                response_deserializer=crypto__service__pb2.final_price.FromString,
                )


class GExchangeServicer(object):
    """Service definition for GExchange
    """

    def get_price(self, request, context):
        """get_price method definition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_maxprice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GExchangeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_price': grpc.unary_unary_rpc_method_handler(
                    servicer.get_price,
                    request_deserializer=crypto__service__pb2.cryptocurrency.FromString,
                    response_serializer=crypto__service__pb2.market_price.SerializeToString,
            ),
            'get_maxprice': grpc.unary_unary_rpc_method_handler(
                    servicer.get_maxprice,
                    request_deserializer=crypto__service__pb2.market_price.FromString,
                    response_serializer=crypto__service__pb2.final_price.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GExchange', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GExchange(object):
    """Service definition for GExchange
    """

    @staticmethod
    def get_price(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GExchange/get_price',
            crypto__service__pb2.cryptocurrency.SerializeToString,
            crypto__service__pb2.market_price.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_maxprice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GExchange/get_maxprice',
            crypto__service__pb2.market_price.SerializeToString,
            crypto__service__pb2.final_price.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
