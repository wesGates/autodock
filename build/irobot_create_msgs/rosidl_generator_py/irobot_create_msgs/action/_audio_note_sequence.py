# generated from rosidl_generator_py/resource/_idl.py.em
# with input from irobot_create_msgs:action/AudioNoteSequence.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AudioNoteSequence_Goal(type):
    """Metaclass of message 'AudioNoteSequence_Goal'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'INFINITE': -1,
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
                'irobot_create_msgs.action.AudioNoteSequence_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__goal

            from irobot_create_msgs.msg import AudioNoteVector
            if AudioNoteVector.__class__._TYPE_SUPPORT is None:
                AudioNoteVector.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'INFINITE': cls.__constants['INFINITE'],
            'ITERATIONS__DEFAULT': 1,
        }

    @property
    def INFINITE(self):
        """Message constant 'INFINITE'."""
        return Metaclass_AudioNoteSequence_Goal.__constants['INFINITE']

    @property
    def ITERATIONS__DEFAULT(cls):
        """Return default value for message field 'iterations'."""
        return 1


class AudioNoteSequence_Goal(metaclass=Metaclass_AudioNoteSequence_Goal):
    """
    Message class 'AudioNoteSequence_Goal'.

    Constants:
      INFINITE
    """

    __slots__ = [
        '_iterations',
        '_note_sequence',
    ]

    _fields_and_field_types = {
        'iterations': 'int32',
        'note_sequence': 'irobot_create_msgs/AudioNoteVector',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'msg'], 'AudioNoteVector'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.iterations = kwargs.get(
            'iterations', AudioNoteSequence_Goal.ITERATIONS__DEFAULT)
        from irobot_create_msgs.msg import AudioNoteVector
        self.note_sequence = kwargs.get('note_sequence', AudioNoteVector())

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
        if self.iterations != other.iterations:
            return False
        if self.note_sequence != other.note_sequence:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def iterations(self):
        """Message field 'iterations'."""
        return self._iterations

    @iterations.setter
    def iterations(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'iterations' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'iterations' field must be an integer in [-2147483648, 2147483647]"
        self._iterations = value

    @builtins.property
    def note_sequence(self):
        """Message field 'note_sequence'."""
        return self._note_sequence

    @note_sequence.setter
    def note_sequence(self, value):
        if __debug__:
            from irobot_create_msgs.msg import AudioNoteVector
            assert \
                isinstance(value, AudioNoteVector), \
                "The 'note_sequence' field must be a sub message of type 'AudioNoteVector'"
        self._note_sequence = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AudioNoteSequence_Result(type):
    """Metaclass of message 'AudioNoteSequence_Result'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__result

            from builtin_interfaces.msg import Duration
            if Duration.__class__._TYPE_SUPPORT is None:
                Duration.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AudioNoteSequence_Result(metaclass=Metaclass_AudioNoteSequence_Result):
    """Message class 'AudioNoteSequence_Result'."""

    __slots__ = [
        '_complete',
        '_iterations_played',
        '_runtime',
    ]

    _fields_and_field_types = {
        'complete': 'boolean',
        'iterations_played': 'int32',
        'runtime': 'builtin_interfaces/Duration',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.complete = kwargs.get('complete', bool())
        self.iterations_played = kwargs.get('iterations_played', int())
        from builtin_interfaces.msg import Duration
        self.runtime = kwargs.get('runtime', Duration())

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
        if self.complete != other.complete:
            return False
        if self.iterations_played != other.iterations_played:
            return False
        if self.runtime != other.runtime:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def complete(self):
        """Message field 'complete'."""
        return self._complete

    @complete.setter
    def complete(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'complete' field must be of type 'bool'"
        self._complete = value

    @builtins.property
    def iterations_played(self):
        """Message field 'iterations_played'."""
        return self._iterations_played

    @iterations_played.setter
    def iterations_played(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'iterations_played' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'iterations_played' field must be an integer in [-2147483648, 2147483647]"
        self._iterations_played = value

    @builtins.property
    def runtime(self):
        """Message field 'runtime'."""
        return self._runtime

    @runtime.setter
    def runtime(self, value):
        if __debug__:
            from builtin_interfaces.msg import Duration
            assert \
                isinstance(value, Duration), \
                "The 'runtime' field must be a sub message of type 'Duration'"
        self._runtime = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AudioNoteSequence_Feedback(type):
    """Metaclass of message 'AudioNoteSequence_Feedback'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__feedback

            from builtin_interfaces.msg import Duration
            if Duration.__class__._TYPE_SUPPORT is None:
                Duration.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AudioNoteSequence_Feedback(metaclass=Metaclass_AudioNoteSequence_Feedback):
    """Message class 'AudioNoteSequence_Feedback'."""

    __slots__ = [
        '_iterations_played',
        '_current_runtime',
    ]

    _fields_and_field_types = {
        'iterations_played': 'int32',
        'current_runtime': 'builtin_interfaces/Duration',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.iterations_played = kwargs.get('iterations_played', int())
        from builtin_interfaces.msg import Duration
        self.current_runtime = kwargs.get('current_runtime', Duration())

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
        if self.iterations_played != other.iterations_played:
            return False
        if self.current_runtime != other.current_runtime:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def iterations_played(self):
        """Message field 'iterations_played'."""
        return self._iterations_played

    @iterations_played.setter
    def iterations_played(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'iterations_played' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'iterations_played' field must be an integer in [-2147483648, 2147483647]"
        self._iterations_played = value

    @builtins.property
    def current_runtime(self):
        """Message field 'current_runtime'."""
        return self._current_runtime

    @current_runtime.setter
    def current_runtime(self, value):
        if __debug__:
            from builtin_interfaces.msg import Duration
            assert \
                isinstance(value, Duration), \
                "The 'current_runtime' field must be a sub message of type 'Duration'"
        self._current_runtime = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AudioNoteSequence_SendGoal_Request(type):
    """Metaclass of message 'AudioNoteSequence_SendGoal_Request'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__send_goal__request

            from irobot_create_msgs.action import AudioNoteSequence
            if AudioNoteSequence.Goal.__class__._TYPE_SUPPORT is None:
                AudioNoteSequence.Goal.__class__.__import_type_support__()

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


class AudioNoteSequence_SendGoal_Request(metaclass=Metaclass_AudioNoteSequence_SendGoal_Request):
    """Message class 'AudioNoteSequence_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'irobot_create_msgs/AudioNoteSequence_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'action'], 'AudioNoteSequence_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Goal
        self.goal = kwargs.get('goal', AudioNoteSequence_Goal())

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
            from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Goal
            assert \
                isinstance(value, AudioNoteSequence_Goal), \
                "The 'goal' field must be a sub message of type 'AudioNoteSequence_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AudioNoteSequence_SendGoal_Response(type):
    """Metaclass of message 'AudioNoteSequence_SendGoal_Response'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__send_goal__response

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


class AudioNoteSequence_SendGoal_Response(metaclass=Metaclass_AudioNoteSequence_SendGoal_Response):
    """Message class 'AudioNoteSequence_SendGoal_Response'."""

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


class Metaclass_AudioNoteSequence_SendGoal(type):
    """Metaclass of service 'AudioNoteSequence_SendGoal'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__audio_note_sequence__send_goal

            from irobot_create_msgs.action import _audio_note_sequence
            if _audio_note_sequence.Metaclass_AudioNoteSequence_SendGoal_Request._TYPE_SUPPORT is None:
                _audio_note_sequence.Metaclass_AudioNoteSequence_SendGoal_Request.__import_type_support__()
            if _audio_note_sequence.Metaclass_AudioNoteSequence_SendGoal_Response._TYPE_SUPPORT is None:
                _audio_note_sequence.Metaclass_AudioNoteSequence_SendGoal_Response.__import_type_support__()


class AudioNoteSequence_SendGoal(metaclass=Metaclass_AudioNoteSequence_SendGoal):
    from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_SendGoal_Request as Request
    from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AudioNoteSequence_GetResult_Request(type):
    """Metaclass of message 'AudioNoteSequence_GetResult_Request'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__get_result__request

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


class AudioNoteSequence_GetResult_Request(metaclass=Metaclass_AudioNoteSequence_GetResult_Request):
    """Message class 'AudioNoteSequence_GetResult_Request'."""

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


class Metaclass_AudioNoteSequence_GetResult_Response(type):
    """Metaclass of message 'AudioNoteSequence_GetResult_Response'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__get_result__response

            from irobot_create_msgs.action import AudioNoteSequence
            if AudioNoteSequence.Result.__class__._TYPE_SUPPORT is None:
                AudioNoteSequence.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AudioNoteSequence_GetResult_Response(metaclass=Metaclass_AudioNoteSequence_GetResult_Response):
    """Message class 'AudioNoteSequence_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'irobot_create_msgs/AudioNoteSequence_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'action'], 'AudioNoteSequence_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Result
        self.result = kwargs.get('result', AudioNoteSequence_Result())

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
            from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Result
            assert \
                isinstance(value, AudioNoteSequence_Result), \
                "The 'result' field must be a sub message of type 'AudioNoteSequence_Result'"
        self._result = value


class Metaclass_AudioNoteSequence_GetResult(type):
    """Metaclass of service 'AudioNoteSequence_GetResult'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__audio_note_sequence__get_result

            from irobot_create_msgs.action import _audio_note_sequence
            if _audio_note_sequence.Metaclass_AudioNoteSequence_GetResult_Request._TYPE_SUPPORT is None:
                _audio_note_sequence.Metaclass_AudioNoteSequence_GetResult_Request.__import_type_support__()
            if _audio_note_sequence.Metaclass_AudioNoteSequence_GetResult_Response._TYPE_SUPPORT is None:
                _audio_note_sequence.Metaclass_AudioNoteSequence_GetResult_Response.__import_type_support__()


class AudioNoteSequence_GetResult(metaclass=Metaclass_AudioNoteSequence_GetResult):
    from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_GetResult_Request as Request
    from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AudioNoteSequence_FeedbackMessage(type):
    """Metaclass of message 'AudioNoteSequence_FeedbackMessage'."""

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
                'irobot_create_msgs.action.AudioNoteSequence_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__audio_note_sequence__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__audio_note_sequence__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__audio_note_sequence__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__audio_note_sequence__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__audio_note_sequence__feedback_message

            from irobot_create_msgs.action import AudioNoteSequence
            if AudioNoteSequence.Feedback.__class__._TYPE_SUPPORT is None:
                AudioNoteSequence.Feedback.__class__.__import_type_support__()

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


class AudioNoteSequence_FeedbackMessage(metaclass=Metaclass_AudioNoteSequence_FeedbackMessage):
    """Message class 'AudioNoteSequence_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'irobot_create_msgs/AudioNoteSequence_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['irobot_create_msgs', 'action'], 'AudioNoteSequence_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Feedback
        self.feedback = kwargs.get('feedback', AudioNoteSequence_Feedback())

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
            from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Feedback
            assert \
                isinstance(value, AudioNoteSequence_Feedback), \
                "The 'feedback' field must be a sub message of type 'AudioNoteSequence_Feedback'"
        self._feedback = value


class Metaclass_AudioNoteSequence(type):
    """Metaclass of action 'AudioNoteSequence'."""

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
                'irobot_create_msgs.action.AudioNoteSequence')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__audio_note_sequence

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from irobot_create_msgs.action import _audio_note_sequence
            if _audio_note_sequence.Metaclass_AudioNoteSequence_SendGoal._TYPE_SUPPORT is None:
                _audio_note_sequence.Metaclass_AudioNoteSequence_SendGoal.__import_type_support__()
            if _audio_note_sequence.Metaclass_AudioNoteSequence_GetResult._TYPE_SUPPORT is None:
                _audio_note_sequence.Metaclass_AudioNoteSequence_GetResult.__import_type_support__()
            if _audio_note_sequence.Metaclass_AudioNoteSequence_FeedbackMessage._TYPE_SUPPORT is None:
                _audio_note_sequence.Metaclass_AudioNoteSequence_FeedbackMessage.__import_type_support__()


class AudioNoteSequence(metaclass=Metaclass_AudioNoteSequence):

    # The goal message defined in the action definition.
    from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Goal as Goal
    # The result message defined in the action definition.
    from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Result as Result
    # The feedback message defined in the action definition.
    from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from irobot_create_msgs.action._audio_note_sequence import AudioNoteSequence_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
