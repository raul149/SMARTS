# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="agent.proto",
    package="agent",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0b\x61gent.proto\x12\x05\x61gent"\x14\n\x05Input\x12\x0b\n\x03msg\x18\x01 \x01(\t"\x15\n\x06Output\x12\x0b\n\x03msg\x18\x01 \x01(\t"\x18\n\x06Status\x12\x0e\n\x06result\x18\x01 \x01(\t"\t\n\x07Machine"9\n\nConnection\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.agent.Status\x12\x0c\n\x04port\x18\x02 \x01(\x05" \n\rSpecification\x12\x0f\n\x07payload\x18\x01 \x01(\x0c"\x1e\n\x0bObservation\x12\x0f\n\x07payload\x18\x01 \x01(\x0c"G\n\x06\x41\x63tion\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.agent.Status\x12\x13\n\x06\x61\x63tion\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\t\n\x07_action2\xc8\x01\n\x05\x41gent\x12/\n\x0eTestConnection\x12\x0c.agent.Input\x1a\r.agent.Output"\x00\x12\x32\n\x0bSpawnWorker\x12\x0e.agent.Machine\x1a\x11.agent.Connection"\x00\x12.\n\x05\x42uild\x12\x14.agent.Specification\x1a\r.agent.Status"\x00\x12*\n\x03\x41\x63t\x12\x12.agent.Observation\x1a\r.agent.Action"\x00\x62\x06proto3',
)


_INPUT = _descriptor.Descriptor(
    name="Input",
    full_name="agent.Input",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="agent.Input.msg",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=22,
    serialized_end=42,
)


_OUTPUT = _descriptor.Descriptor(
    name="Output",
    full_name="agent.Output",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="agent.Output.msg",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=44,
    serialized_end=65,
)


_STATUS = _descriptor.Descriptor(
    name="Status",
    full_name="agent.Status",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="result",
            full_name="agent.Status.result",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=67,
    serialized_end=91,
)


_MACHINE = _descriptor.Descriptor(
    name="Machine",
    full_name="agent.Machine",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=93,
    serialized_end=102,
)


_CONNECTION = _descriptor.Descriptor(
    name="Connection",
    full_name="agent.Connection",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="status",
            full_name="agent.Connection.status",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="port",
            full_name="agent.Connection.port",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=104,
    serialized_end=161,
)


_SPECIFICATION = _descriptor.Descriptor(
    name="Specification",
    full_name="agent.Specification",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="agent.Specification.payload",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=163,
    serialized_end=195,
)


_OBSERVATION = _descriptor.Descriptor(
    name="Observation",
    full_name="agent.Observation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="agent.Observation.payload",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=197,
    serialized_end=227,
)


_ACTION = _descriptor.Descriptor(
    name="Action",
    full_name="agent.Action",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="status",
            full_name="agent.Action.status",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="action",
            full_name="agent.Action.action",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_action",
            full_name="agent.Action._action",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=229,
    serialized_end=300,
)

_CONNECTION.fields_by_name["status"].message_type = _STATUS
_ACTION.fields_by_name["status"].message_type = _STATUS
_ACTION.oneofs_by_name["_action"].fields.append(_ACTION.fields_by_name["action"])
_ACTION.fields_by_name["action"].containing_oneof = _ACTION.oneofs_by_name["_action"]
DESCRIPTOR.message_types_by_name["Input"] = _INPUT
DESCRIPTOR.message_types_by_name["Output"] = _OUTPUT
DESCRIPTOR.message_types_by_name["Status"] = _STATUS
DESCRIPTOR.message_types_by_name["Machine"] = _MACHINE
DESCRIPTOR.message_types_by_name["Connection"] = _CONNECTION
DESCRIPTOR.message_types_by_name["Specification"] = _SPECIFICATION
DESCRIPTOR.message_types_by_name["Observation"] = _OBSERVATION
DESCRIPTOR.message_types_by_name["Action"] = _ACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Input = _reflection.GeneratedProtocolMessageType(
    "Input",
    (_message.Message,),
    {
        "DESCRIPTOR": _INPUT,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Input)
    },
)
_sym_db.RegisterMessage(Input)

Output = _reflection.GeneratedProtocolMessageType(
    "Output",
    (_message.Message,),
    {
        "DESCRIPTOR": _OUTPUT,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Output)
    },
)
_sym_db.RegisterMessage(Output)

Status = _reflection.GeneratedProtocolMessageType(
    "Status",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATUS,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Status)
    },
)
_sym_db.RegisterMessage(Status)

Machine = _reflection.GeneratedProtocolMessageType(
    "Machine",
    (_message.Message,),
    {
        "DESCRIPTOR": _MACHINE,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Machine)
    },
)
_sym_db.RegisterMessage(Machine)

Connection = _reflection.GeneratedProtocolMessageType(
    "Connection",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONNECTION,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Connection)
    },
)
_sym_db.RegisterMessage(Connection)

Specification = _reflection.GeneratedProtocolMessageType(
    "Specification",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPECIFICATION,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Specification)
    },
)
_sym_db.RegisterMessage(Specification)

Observation = _reflection.GeneratedProtocolMessageType(
    "Observation",
    (_message.Message,),
    {
        "DESCRIPTOR": _OBSERVATION,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Observation)
    },
)
_sym_db.RegisterMessage(Observation)

Action = _reflection.GeneratedProtocolMessageType(
    "Action",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTION,
        "__module__": "agent_pb2"
        # @@protoc_insertion_point(class_scope:agent.Action)
    },
)
_sym_db.RegisterMessage(Action)


_AGENT = _descriptor.ServiceDescriptor(
    name="Agent",
    full_name="agent.Agent",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=303,
    serialized_end=503,
    methods=[
        _descriptor.MethodDescriptor(
            name="TestConnection",
            full_name="agent.Agent.TestConnection",
            index=0,
            containing_service=None,
            input_type=_INPUT,
            output_type=_OUTPUT,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SpawnWorker",
            full_name="agent.Agent.SpawnWorker",
            index=1,
            containing_service=None,
            input_type=_MACHINE,
            output_type=_CONNECTION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Build",
            full_name="agent.Agent.Build",
            index=2,
            containing_service=None,
            input_type=_SPECIFICATION,
            output_type=_STATUS,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Act",
            full_name="agent.Agent.Act",
            index=3,
            containing_service=None,
            input_type=_OBSERVATION,
            output_type=_ACTION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_AGENT)

DESCRIPTOR.services_by_name["Agent"] = _AGENT

# @@protoc_insertion_point(module_scope)