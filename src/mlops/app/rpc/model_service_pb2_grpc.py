# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import model_service_pb2 as model__service__pb2


class IrisModelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.predict_output = channel.unary_unary(
                '/IrisModel/predict_output',
                request_serializer=model__service__pb2.iris_param.SerializeToString,
                response_deserializer=model__service__pb2.iris_output.FromString,
                )


class IrisModelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def predict_output(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IrisModelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'predict_output': grpc.unary_unary_rpc_method_handler(
                    servicer.predict_output,
                    request_deserializer=model__service__pb2.iris_param.FromString,
                    response_serializer=model__service__pb2.iris_output.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'IrisModel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IrisModel(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def predict_output(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IrisModel/predict_output',
            model__service__pb2.iris_param.SerializeToString,
            model__service__pb2.iris_output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
