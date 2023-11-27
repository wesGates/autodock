# generated from rosidl_generator_py/resource/_idl.py.em
# with input from irobot_create_msgs:msg/Button.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Button(type):
    """Metaclass of message 'Button'."""

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
                'irobot_create_msgs.msg.Button')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__button
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__button
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__button
            cls._TYPE_SUPPORT = module.type_support_msg__msg__button
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__button

            from builtin_interfaces.msg import Duration
            if Duration.__class__._TYPE_SUPPORT is None:
                Duration.__class__.__import_type_support__()

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

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


class Button(metaclass=Metaclass_Button):
    """Message class 'Button'."""

    __slots__ = [
        '_header',
        '_is_pressed',
        '_last_start_pressed_time',
        '_last_pressed_duration',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'is_pressed': 'boolean',
        'last_start_pressed_time': 'builtin_interfaces/Time',
        'last_pressed_duration': 'builtin_interfaces/Duration',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.is_pressed = kwargs.get('is_pressed', bool())
        from builtin_interfaces.msg import Time
        self.last_start_pressed_time = kwargs.get('last_start_pressed_time', Time())
        from builtin_interfaces.msg import Duration
        self.last_pressed_duration = kwargs.get('last_pressed_duration', Duration())

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
        if self.is_pressed != other.is_pressed:
            return False
        if self.last_start_pressed_time != other.last_start_pressed_time:
            return False
        if self.last_pressed_duration != other.last_pressed_duration:
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
    def is_pressed(self):
        """Message field 'is_pressed'."""
        return self._is_pressed

    @is_pressed.setter
    def is_pressed(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_pressed' field must be of type 'bool'"
        self._is_pressed = value

    @builtins.property
    def last_start_pressed_time(self):
        """Message field 'last_start_pressed_time'."""
        return self._last_start_pressed_time

    @last_start_pressed_time.setter
    def last_start_pressed_time(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'last_start_pressed_time' field must be a sub message of type 'Time'"
        self._last_start_pressed_time = value

    @builtins.property
    def last_pressed_duration(self):
        """Message field 'last_pressed_duration'."""
        return self._last_pressed_duration

    @last_pressed_duration.setter
    def last_pressed_duration(self, value):
        if __debug__:
            from builtin_interfaces.msg import Duration
            assert \
                isinstance(value, Duration), \
                "The 'last_pressed_duration' field must be a sub message of type 'Duration'"
        self._last_pressed_duration = value
