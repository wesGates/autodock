# generated from rosidl_generator_py/resource/_idl.py.em
# with input from irobot_create_msgs:msg/InterfaceButtons.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InterfaceButtons(type):
    """Metaclass of message 'InterfaceButtons'."""

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
                'irobot_create_msgs.msg.InterfaceButtons')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__interface_buttons
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__interface_buttons
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__interface_buttons
            cls._TYPE_SUPPORT = module.type_support_msg__msg__interface_buttons
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__interface_buttons

            from irobot_create_msgs.msg import Button
            if Button.__class__._TYPE_SUPPORT is None:
                Button.__class__.__import_type_support__()

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


class InterfaceButtons(metaclass=Metaclass_InterfaceButtons):
    """Message class 'InterfaceButtons'."""

    __slots__ = [
        '_header',
        '_button_1',
        '_button_power',
        '_button_2',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'button_1': 'irobot_create_msgs/Button',
        'button_power': 'irobot_create_msgs/Button',
        'button_2': 'irobot_create_msgs/Button',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'msg'], 'Button'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'msg'], 'Button'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'msg'], 'Button'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        from irobot_create_msgs.msg import Button
        self.button_1 = kwargs.get('button_1', Button())
        from irobot_create_msgs.msg import Button
        self.button_power = kwargs.get('button_power', Button())
        from irobot_create_msgs.msg import Button
        self.button_2 = kwargs.get('button_2', Button())

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
        if self.button_1 != other.button_1:
            return False
        if self.button_power != other.button_power:
            return False
        if self.button_2 != other.button_2:
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
    def button_1(self):
        """Message field 'button_1'."""
        return self._button_1

    @button_1.setter
    def button_1(self, value):
        if __debug__:
            from irobot_create_msgs.msg import Button
            assert \
                isinstance(value, Button), \
                "The 'button_1' field must be a sub message of type 'Button'"
        self._button_1 = value

    @builtins.property
    def button_power(self):
        """Message field 'button_power'."""
        return self._button_power

    @button_power.setter
    def button_power(self, value):
        if __debug__:
            from irobot_create_msgs.msg import Button
            assert \
                isinstance(value, Button), \
                "The 'button_power' field must be a sub message of type 'Button'"
        self._button_power = value

    @builtins.property
    def button_2(self):
        """Message field 'button_2'."""
        return self._button_2

    @button_2.setter
    def button_2(self, value):
        if __debug__:
            from irobot_create_msgs.msg import Button
            assert \
                isinstance(value, Button), \
                "The 'button_2' field must be a sub message of type 'Button'"
        self._button_2 = value
