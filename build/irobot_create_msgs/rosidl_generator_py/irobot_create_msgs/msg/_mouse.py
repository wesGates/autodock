# generated from rosidl_generator_py/resource/_idl.py.em
# with input from irobot_create_msgs:msg/Mouse.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Mouse(type):
    """Metaclass of message 'Mouse'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('irobot_create_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'irobot_create_msgs.msg.Mouse')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mouse
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mouse
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mouse
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mouse
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mouse

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mouse(metaclass=Metaclass_Mouse):
    """Message class 'Mouse'."""

    __slots__ = [
        '_header',
        '_integrated_x',
        '_integrated_y',
        '_frame_id',
        '_last_squal',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'integrated_x': 'float',
        'integrated_y': 'float',
        'frame_id': 'uint32',
        'last_squal': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.integrated_x = kwargs.get('integrated_x', float())
        self.integrated_y = kwargs.get('integrated_y', float())
        self.frame_id = kwargs.get('frame_id', int())
        self.last_squal = kwargs.get('last_squal', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.integrated_x != other.integrated_x:
            return False
        if self.integrated_y != other.integrated_y:
            return False
        if self.frame_id != other.frame_id:
            return False
        if self.last_squal != other.last_squal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def integrated_x(self):
        """Message field 'integrated_x'."""
        return self._integrated_x

    @integrated_x.setter
    def integrated_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'integrated_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'integrated_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._integrated_x = value

    @builtins.property
    def integrated_y(self):
        """Message field 'integrated_y'."""
        return self._integrated_y

    @integrated_y.setter
    def integrated_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'integrated_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'integrated_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._integrated_y = value

    @builtins.property
    def frame_id(self):
        """Message field 'frame_id'."""
        return self._frame_id

    @frame_id.setter
    def frame_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'frame_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'frame_id' field must be an unsigned integer in [0, 4294967295]"
        self._frame_id = value

    @builtins.property
    def last_squal(self):
        """Message field 'last_squal'."""
        return self._last_squal

    @last_squal.setter
    def last_squal(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'last_squal' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'last_squal' field must be an unsigned integer in [0, 255]"
        self._last_squal = value
