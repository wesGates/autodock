# generated from rosidl_generator_py/resource/_idl.py.em
# with input from irobot_create_msgs:msg/WheelStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_WheelStatus(type):
    """Metaclass of message 'WheelStatus'."""

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
                'irobot_create_msgs.msg.WheelStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__wheel_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__wheel_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__wheel_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__wheel_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__wheel_status

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


class WheelStatus(metaclass=Metaclass_WheelStatus):
    """Message class 'WheelStatus'."""

    __slots__ = [
        '_header',
        '_current_ma_left',
        '_current_ma_right',
        '_pwm_left',
        '_pwm_right',
        '_wheels_enabled',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'current_ma_left': 'int16',
        'current_ma_right': 'int16',
        'pwm_left': 'int16',
        'pwm_right': 'int16',
        'wheels_enabled': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.current_ma_left = kwargs.get('current_ma_left', int())
        self.current_ma_right = kwargs.get('current_ma_right', int())
        self.pwm_left = kwargs.get('pwm_left', int())
        self.pwm_right = kwargs.get('pwm_right', int())
        self.wheels_enabled = kwargs.get('wheels_enabled', bool())

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
        if self.current_ma_left != other.current_ma_left:
            return False
        if self.current_ma_right != other.current_ma_right:
            return False
        if self.pwm_left != other.pwm_left:
            return False
        if self.pwm_right != other.pwm_right:
            return False
        if self.wheels_enabled != other.wheels_enabled:
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
    def current_ma_left(self):
        """Message field 'current_ma_left'."""
        return self._current_ma_left

    @current_ma_left.setter
    def current_ma_left(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'current_ma_left' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'current_ma_left' field must be an integer in [-32768, 32767]"
        self._current_ma_left = value

    @builtins.property
    def current_ma_right(self):
        """Message field 'current_ma_right'."""
        return self._current_ma_right

    @current_ma_right.setter
    def current_ma_right(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'current_ma_right' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'current_ma_right' field must be an integer in [-32768, 32767]"
        self._current_ma_right = value

    @builtins.property
    def pwm_left(self):
        """Message field 'pwm_left'."""
        return self._pwm_left

    @pwm_left.setter
    def pwm_left(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'pwm_left' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'pwm_left' field must be an integer in [-32768, 32767]"
        self._pwm_left = value

    @builtins.property
    def pwm_right(self):
        """Message field 'pwm_right'."""
        return self._pwm_right

    @pwm_right.setter
    def pwm_right(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'pwm_right' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'pwm_right' field must be an integer in [-32768, 32767]"
        self._pwm_right = value

    @builtins.property
    def wheels_enabled(self):
        """Message field 'wheels_enabled'."""
        return self._wheels_enabled

    @wheels_enabled.setter
    def wheels_enabled(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'wheels_enabled' field must be of type 'bool'"
        self._wheels_enabled = value
