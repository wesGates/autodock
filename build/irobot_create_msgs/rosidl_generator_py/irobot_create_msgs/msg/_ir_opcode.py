# generated from rosidl_generator_py/resource/_idl.py.em
# with input from irobot_create_msgs:msg/IrOpcode.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_IrOpcode(type):
    """Metaclass of message 'IrOpcode'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'CODE_IR_FORCE_FIELD': 161,
        'CODE_IR_VIRTUAL_WALL': 162,
        'CODE_IR_BUOY_GREEN': 164,
        'CODE_IR_BUOY_RED': 168,
        'CODE_IR_BUOY_BOTH': 172,
        'CODE_IR_EVAC_GREEN_FIELD': 244,
        'CODE_IR_EVAC_RED_FIELD': 248,
        'CODE_IR_EVAC_BOTH_FIELD': 252,
        'SENSOR_OMNI': 0,
        'SENSOR_DIRECTIONAL_FRONT': 1,
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
                'irobot_create_msgs.msg.IrOpcode')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ir_opcode
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ir_opcode
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ir_opcode
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ir_opcode
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ir_opcode

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'CODE_IR_FORCE_FIELD': cls.__constants['CODE_IR_FORCE_FIELD'],
            'CODE_IR_VIRTUAL_WALL': cls.__constants['CODE_IR_VIRTUAL_WALL'],
            'CODE_IR_BUOY_GREEN': cls.__constants['CODE_IR_BUOY_GREEN'],
            'CODE_IR_BUOY_RED': cls.__constants['CODE_IR_BUOY_RED'],
            'CODE_IR_BUOY_BOTH': cls.__constants['CODE_IR_BUOY_BOTH'],
            'CODE_IR_EVAC_GREEN_FIELD': cls.__constants['CODE_IR_EVAC_GREEN_FIELD'],
            'CODE_IR_EVAC_RED_FIELD': cls.__constants['CODE_IR_EVAC_RED_FIELD'],
            'CODE_IR_EVAC_BOTH_FIELD': cls.__constants['CODE_IR_EVAC_BOTH_FIELD'],
            'SENSOR_OMNI': cls.__constants['SENSOR_OMNI'],
            'SENSOR_DIRECTIONAL_FRONT': cls.__constants['SENSOR_DIRECTIONAL_FRONT'],
        }

    @property
    def CODE_IR_FORCE_FIELD(self):
        """Message constant 'CODE_IR_FORCE_FIELD'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_FORCE_FIELD']

    @property
    def CODE_IR_VIRTUAL_WALL(self):
        """Message constant 'CODE_IR_VIRTUAL_WALL'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_VIRTUAL_WALL']

    @property
    def CODE_IR_BUOY_GREEN(self):
        """Message constant 'CODE_IR_BUOY_GREEN'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_BUOY_GREEN']

    @property
    def CODE_IR_BUOY_RED(self):
        """Message constant 'CODE_IR_BUOY_RED'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_BUOY_RED']

    @property
    def CODE_IR_BUOY_BOTH(self):
        """Message constant 'CODE_IR_BUOY_BOTH'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_BUOY_BOTH']

    @property
    def CODE_IR_EVAC_GREEN_FIELD(self):
        """Message constant 'CODE_IR_EVAC_GREEN_FIELD'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_EVAC_GREEN_FIELD']

    @property
    def CODE_IR_EVAC_RED_FIELD(self):
        """Message constant 'CODE_IR_EVAC_RED_FIELD'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_EVAC_RED_FIELD']

    @property
    def CODE_IR_EVAC_BOTH_FIELD(self):
        """Message constant 'CODE_IR_EVAC_BOTH_FIELD'."""
        return Metaclass_IrOpcode.__constants['CODE_IR_EVAC_BOTH_FIELD']

    @property
    def SENSOR_OMNI(self):
        """Message constant 'SENSOR_OMNI'."""
        return Metaclass_IrOpcode.__constants['SENSOR_OMNI']

    @property
    def SENSOR_DIRECTIONAL_FRONT(self):
        """Message constant 'SENSOR_DIRECTIONAL_FRONT'."""
        return Metaclass_IrOpcode.__constants['SENSOR_DIRECTIONAL_FRONT']


class IrOpcode(metaclass=Metaclass_IrOpcode):
    """
    Message class 'IrOpcode'.

    Constants:
      CODE_IR_FORCE_FIELD
      CODE_IR_VIRTUAL_WALL
      CODE_IR_BUOY_GREEN
      CODE_IR_BUOY_RED
      CODE_IR_BUOY_BOTH
      CODE_IR_EVAC_GREEN_FIELD
      CODE_IR_EVAC_RED_FIELD
      CODE_IR_EVAC_BOTH_FIELD
      SENSOR_OMNI
      SENSOR_DIRECTIONAL_FRONT
    """

    __slots__ = [
        '_header',
        '_opcode',
        '_sensor',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'opcode': 'uint8',
        'sensor': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.opcode = kwargs.get('opcode', int())
        self.sensor = kwargs.get('sensor', int())

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
        if self.opcode != other.opcode:
            return False
        if self.sensor != other.sensor:
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
    def opcode(self):
        """Message field 'opcode'."""
        return self._opcode

    @opcode.setter
    def opcode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'opcode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'opcode' field must be an unsigned integer in [0, 255]"
        self._opcode = value

    @builtins.property
    def sensor(self):
        """Message field 'sensor'."""
        return self._sensor

    @sensor.setter
    def sensor(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'sensor' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'sensor' field must be an unsigned integer in [0, 255]"
        self._sensor = value
