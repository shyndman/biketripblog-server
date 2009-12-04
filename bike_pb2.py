# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_POINT = descriptor.Descriptor(
  name='Point',
  full_name='ca.scotthyndman.bike.data.Point',
  filename='bike.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='ca.scotthyndman.bike.data.Point.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='latitude', full_name='ca.scotthyndman.bike.data.Point.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='longitude', full_name='ca.scotthyndman.bike.data.Point.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='altitude', full_name='ca.scotthyndman.bike.data.Point.altitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bearing', full_name='ca.scotthyndman.bike.data.Point.bearing', index=4,
      number=5, type=2, cpp_type=6, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='temperature', full_name='ca.scotthyndman.bike.data.Point.temperature', index=5,
      number=6, type=2, cpp_type=6, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeStamp', full_name='ca.scotthyndman.bike.data.Point.timeStamp', index=6,
      number=7, type=3, cpp_type=2, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_PHOTO = descriptor.Descriptor(
  name='Photo',
  full_name='ca.scotthyndman.bike.data.Photo',
  filename='bike.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='ca.scotthyndman.bike.data.Photo.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='ca.scotthyndman.bike.data.Photo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contents', full_name='ca.scotthyndman.bike.data.Photo.contents', index=2,
      number=3, type=12, cpp_type=9, label=1,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_UPLOADPACKAGE = descriptor.Descriptor(
  name='UploadPackage',
  full_name='ca.scotthyndman.bike.data.UploadPackage',
  filename='bike.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='points', full_name='ca.scotthyndman.bike.data.UploadPackage.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='photos', full_name='ca.scotthyndman.bike.data.UploadPackage.photos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_UPLOADPACKAGE.fields_by_name['points'].message_type = _POINT
_UPLOADPACKAGE.fields_by_name['photos'].message_type = _PHOTO

class Point(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POINT

class Photo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PHOTO

class UploadPackage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPLOADPACKAGE

