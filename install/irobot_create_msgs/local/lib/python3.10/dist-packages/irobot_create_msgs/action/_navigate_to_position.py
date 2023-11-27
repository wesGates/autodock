# generated from rosidl_generator_py/resource/_idl.py.em
# with input from irobot_create_msgs:action/NavigateToPosition.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NavigateToPosition_Goal(type):
    """Metaclass of message 'NavigateToPosition_Goal'."""

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
                'irobot_create_msgs.action.NavigateToPosition_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__goal

            from geometry_msgs.msg import PoseStamped
            if PoseStamped.__class__._TYPE_SUPPORT is None:
                PoseStamped.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'MAX_TRANSLATION_SPEED__DEFAULT': 0.3,
            'MAX_ROTATION_SPEED__DEFAULT': 1.9,
        }

    @property
    def MAX_TRANSLATION_SPEED__DEFAULT(cls):
        """Return default value for message field 'max_translation_speed'."""
        return 0.3

    @property
    def MAX_ROTATION_SPEED__DEFAULT(cls):
        """Return default value for message field 'max_rotation_speed'."""
        return 1.9


class NavigateToPosition_Goal(metaclass=Metaclass_NavigateToPosition_Goal):
    """Message class 'NavigateToPosition_Goal'."""

    __slots__ = [
        '_goal_pose',
        '_achieve_goal_heading',
        '_max_translation_speed',
        '_max_rotation_speed',
    ]

    _fields_and_field_types = {
        'goal_pose': 'geometry_msgs/PoseStamped',
        'achieve_goal_heading': 'boolean',
        'max_translation_speed': 'float',
        'max_rotation_speed': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from geometry_msgs.msg import PoseStamped
        self.goal_pose = kwargs.get('goal_pose', PoseStamped())
        self.achieve_goal_heading = kwargs.get('achieve_goal_heading', bool())
        self.max_translation_speed = kwargs.get(
            'max_translation_speed', NavigateToPosition_Goal.MAX_TRANSLATION_SPEED__DEFAULT)
        self.max_rotation_speed = kwargs.get(
            'max_rotation_speed', NavigateToPosition_Goal.MAX_ROTATION_SPEED__DEFAULT)

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
        if self.goal_pose != other.goal_pose:
            return False
        if self.achieve_goal_heading != other.achieve_goal_heading:
            return False
        if self.max_translation_speed != other.max_translation_speed:
            return False
        if self.max_rotation_speed != other.max_rotation_speed:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_pose(self):
        """Message field 'goal_pose'."""
        return self._goal_pose

    @goal_pose.setter
    def goal_pose(self, value):
        if __debug__:
            from geometry_msgs.msg import PoseStamped
            assert \
                isinstance(value, PoseStamped), \
                "The 'goal_pose' field must be a sub message of type 'PoseStamped'"
        self._goal_pose = value

    @builtins.property
    def achieve_goal_heading(self):
        """Message field 'achieve_goal_heading'."""
        return self._achieve_goal_heading

    @achieve_goal_heading.setter
    def achieve_goal_heading(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'achieve_goal_heading' field must be of type 'bool'"
        self._achieve_goal_heading = value

    @builtins.property
    def max_translation_speed(self):
        """Message field 'max_translation_speed'."""
        return self._max_translation_speed

    @max_translation_speed.setter
    def max_translation_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'max_translation_speed' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'max_translation_speed' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._max_translation_speed = value

    @builtins.property
    def max_rotation_speed(self):
        """Message field 'max_rotation_speed'."""
        return self._max_rotation_speed

    @max_rotation_speed.setter
    def max_rotation_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'max_rotation_speed' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'max_rotation_speed' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._max_rotation_speed = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavigateToPosition_Result(type):
    """Metaclass of message 'NavigateToPosition_Result'."""

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
                'irobot_create_msgs.action.NavigateToPosition_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__result

            from geometry_msgs.msg import PoseStamped
            if PoseStamped.__class__._TYPE_SUPPORT is None:
                PoseStamped.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavigateToPosition_Result(metaclass=Metaclass_NavigateToPosition_Result):
    """Message class 'NavigateToPosition_Result'."""

    __slots__ = [
        '_pose',
    ]

    _fields_and_field_types = {
        'pose': 'geometry_msgs/PoseStamped',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from geometry_msgs.msg import PoseStamped
        self.pose = kwargs.get('pose', PoseStamped())

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
        if self.pose != other.pose:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pose(self):
        """Message field 'pose'."""
        return self._pose

    @pose.setter
    def pose(self, value):
        if __debug__:
            from geometry_msgs.msg import PoseStamped
            assert \
                isinstance(value, PoseStamped), \
                "The 'pose' field must be a sub message of type 'PoseStamped'"
        self._pose = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_NavigateToPosition_Feedback(type):
    """Metaclass of message 'NavigateToPosition_Feedback'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'ROTATING_TO_GOAL_POSITION': 1,
        'DRIVING_TO_GOAL_POSITION': 2,
        'ROTATING_TO_GOAL_ORIENTATION': 3,
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
                'irobot_create_msgs.action.NavigateToPosition_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__feedback

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'ROTATING_TO_GOAL_POSITION': cls.__constants['ROTATING_TO_GOAL_POSITION'],
            'DRIVING_TO_GOAL_POSITION': cls.__constants['DRIVING_TO_GOAL_POSITION'],
            'ROTATING_TO_GOAL_ORIENTATION': cls.__constants['ROTATING_TO_GOAL_ORIENTATION'],
        }

    @property
    def ROTATING_TO_GOAL_POSITION(self):
        """Message constant 'ROTATING_TO_GOAL_POSITION'."""
        return Metaclass_NavigateToPosition_Feedback.__constants['ROTATING_TO_GOAL_POSITION']

    @property
    def DRIVING_TO_GOAL_POSITION(self):
        """Message constant 'DRIVING_TO_GOAL_POSITION'."""
        return Metaclass_NavigateToPosition_Feedback.__constants['DRIVING_TO_GOAL_POSITION']

    @property
    def ROTATING_TO_GOAL_ORIENTATION(self):
        """Message constant 'ROTATING_TO_GOAL_ORIENTATION'."""
        return Metaclass_NavigateToPosition_Feedback.__constants['ROTATING_TO_GOAL_ORIENTATION']


class NavigateToPosition_Feedback(metaclass=Metaclass_NavigateToPosition_Feedback):
    """
    Message class 'NavigateToPosition_Feedback'.

    Constants:
      ROTATING_TO_GOAL_POSITION
      DRIVING_TO_GOAL_POSITION
      ROTATING_TO_GOAL_ORIENTATION
    """

    __slots__ = [
        '_navigate_state',
        '_remaining_angle_travel',
        '_remaining_travel_distance',
    ]

    _fields_and_field_types = {
        'navigate_state': 'int8',
        'remaining_angle_travel': 'float',
        'remaining_travel_distance': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.navigate_state = kwargs.get('navigate_state', int())
        self.remaining_angle_travel = kwargs.get('remaining_angle_travel', float())
        self.remaining_travel_distance = kwargs.get('remaining_travel_distance', float())

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
        if self.navigate_state != other.navigate_state:
            return False
        if self.remaining_angle_travel != other.remaining_angle_travel:
            return False
        if self.remaining_travel_distance != other.remaining_travel_distance:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def navigate_state(self):
        """Message field 'navigate_state'."""
        return self._navigate_state

    @navigate_state.setter
    def navigate_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'navigate_state' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'navigate_state' field must be an integer in [-128, 127]"
        self._navigate_state = value

    @builtins.property
    def remaining_angle_travel(self):
        """Message field 'remaining_angle_travel'."""
        return self._remaining_angle_travel

    @remaining_angle_travel.setter
    def remaining_angle_travel(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'remaining_angle_travel' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'remaining_angle_travel' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._remaining_angle_travel = value

    @builtins.property
    def remaining_travel_distance(self):
        """Message field 'remaining_travel_distance'."""
        return self._remaining_travel_distance

    @remaining_travel_distance.setter
    def remaining_travel_distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'remaining_travel_distance' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'remaining_travel_distance' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._remaining_travel_distance = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavigateToPosition_SendGoal_Request(type):
    """Metaclass of message 'NavigateToPosition_SendGoal_Request'."""

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
                'irobot_create_msgs.action.NavigateToPosition_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__send_goal__request

            from irobot_create_msgs.action import NavigateToPosition
            if NavigateToPosition.Goal.__class__._TYPE_SUPPORT is None:
                NavigateToPosition.Goal.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavigateToPosition_SendGoal_Request(metaclass=Metaclass_NavigateToPosition_SendGoal_Request):
    """Message class 'NavigateToPosition_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'irobot_create_msgs/NavigateToPosition_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'action'], 'NavigateToPosition_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Goal
        self.goal = kwargs.get('goal', NavigateToPosition_Goal())

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
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Goal
            assert \
                isinstance(value, NavigateToPosition_Goal), \
                "The 'goal' field must be a sub message of type 'NavigateToPosition_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavigateToPosition_SendGoal_Response(type):
    """Metaclass of message 'NavigateToPosition_SendGoal_Response'."""

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
                'irobot_create_msgs.action.NavigateToPosition_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__send_goal__response

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavigateToPosition_SendGoal_Response(metaclass=Metaclass_NavigateToPosition_SendGoal_Response):
    """Message class 'NavigateToPosition_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
    ]

    _fields_and_field_types = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accepted = kwargs.get('accepted', bool())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

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
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self):
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


class Metaclass_NavigateToPosition_SendGoal(type):
    """Metaclass of service 'NavigateToPosition_SendGoal'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('irobot_create_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'irobot_create_msgs.action.NavigateToPosition_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__navigate_to_position__send_goal

            from irobot_create_msgs.action import _navigate_to_position
            if _navigate_to_position.Metaclass_NavigateToPosition_SendGoal_Request._TYPE_SUPPORT is None:
                _navigate_to_position.Metaclass_NavigateToPosition_SendGoal_Request.__import_type_support__()
            if _navigate_to_position.Metaclass_NavigateToPosition_SendGoal_Response._TYPE_SUPPORT is None:
                _navigate_to_position.Metaclass_NavigateToPosition_SendGoal_Response.__import_type_support__()


class NavigateToPosition_SendGoal(metaclass=Metaclass_NavigateToPosition_SendGoal):
    from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_SendGoal_Request as Request
    from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavigateToPosition_GetResult_Request(type):
    """Metaclass of message 'NavigateToPosition_GetResult_Request'."""

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
                'irobot_create_msgs.action.NavigateToPosition_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavigateToPosition_GetResult_Request(metaclass=Metaclass_NavigateToPosition_GetResult_Request):
    """Message class 'NavigateToPosition_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())

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
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavigateToPosition_GetResult_Response(type):
    """Metaclass of message 'NavigateToPosition_GetResult_Response'."""

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
                'irobot_create_msgs.action.NavigateToPosition_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__get_result__response

            from irobot_create_msgs.action import NavigateToPosition
            if NavigateToPosition.Result.__class__._TYPE_SUPPORT is None:
                NavigateToPosition.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavigateToPosition_GetResult_Response(metaclass=Metaclass_NavigateToPosition_GetResult_Response):
    """Message class 'NavigateToPosition_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'irobot_create_msgs/NavigateToPosition_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'action'], 'NavigateToPosition_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Result
        self.result = kwargs.get('result', NavigateToPosition_Result())

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
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Result
            assert \
                isinstance(value, NavigateToPosition_Result), \
                "The 'result' field must be a sub message of type 'NavigateToPosition_Result'"
        self._result = value


class Metaclass_NavigateToPosition_GetResult(type):
    """Metaclass of service 'NavigateToPosition_GetResult'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('irobot_create_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'irobot_create_msgs.action.NavigateToPosition_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__navigate_to_position__get_result

            from irobot_create_msgs.action import _navigate_to_position
            if _navigate_to_position.Metaclass_NavigateToPosition_GetResult_Request._TYPE_SUPPORT is None:
                _navigate_to_position.Metaclass_NavigateToPosition_GetResult_Request.__import_type_support__()
            if _navigate_to_position.Metaclass_NavigateToPosition_GetResult_Response._TYPE_SUPPORT is None:
                _navigate_to_position.Metaclass_NavigateToPosition_GetResult_Response.__import_type_support__()


class NavigateToPosition_GetResult(metaclass=Metaclass_NavigateToPosition_GetResult):
    from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_GetResult_Request as Request
    from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavigateToPosition_FeedbackMessage(type):
    """Metaclass of message 'NavigateToPosition_FeedbackMessage'."""

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
                'irobot_create_msgs.action.NavigateToPosition_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__navigate_to_position__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__navigate_to_position__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__navigate_to_position__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__navigate_to_position__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__navigate_to_position__feedback_message

            from irobot_create_msgs.action import NavigateToPosition
            if NavigateToPosition.Feedback.__class__._TYPE_SUPPORT is None:
                NavigateToPosition.Feedback.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavigateToPosition_FeedbackMessage(metaclass=Metaclass_NavigateToPosition_FeedbackMessage):
    """Message class 'NavigateToPosition_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'irobot_create_msgs/NavigateToPosition_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'action'], 'NavigateToPosition_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Feedback
        self.feedback = kwargs.get('feedback', NavigateToPosition_Feedback())

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
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self):
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        if __debug__:
            from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Feedback
            assert \
                isinstance(value, NavigateToPosition_Feedback), \
                "The 'feedback' field must be a sub message of type 'NavigateToPosition_Feedback'"
        self._feedback = value


class Metaclass_NavigateToPosition(type):
    """Metaclass of action 'NavigateToPosition'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('irobot_create_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'irobot_create_msgs.action.NavigateToPosition')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__navigate_to_position

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from irobot_create_msgs.action import _navigate_to_position
            if _navigate_to_position.Metaclass_NavigateToPosition_SendGoal._TYPE_SUPPORT is None:
                _navigate_to_position.Metaclass_NavigateToPosition_SendGoal.__import_type_support__()
            if _navigate_to_position.Metaclass_NavigateToPosition_GetResult._TYPE_SUPPORT is None:
                _navigate_to_position.Metaclass_NavigateToPosition_GetResult.__import_type_support__()
            if _navigate_to_position.Metaclass_NavigateToPosition_FeedbackMessage._TYPE_SUPPORT is None:
                _navigate_to_position.Metaclass_NavigateToPosition_FeedbackMessage.__import_type_support__()


class NavigateToPosition(metaclass=Metaclass_NavigateToPosition):

    # The goal message defined in the action definition.
    from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Goal as Goal
    # The result message defined in the action definition.
    from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Result as Result
    # The feedback message defined in the action definition.
    from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from irobot_create_msgs.action._navigate_to_position import NavigateToPosition_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
