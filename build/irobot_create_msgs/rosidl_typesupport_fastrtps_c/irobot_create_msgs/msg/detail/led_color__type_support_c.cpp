// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from irobot_create_msgs:msg/LedColor.idl
// generated code does not contain a copyright notice
#include "irobot_create_msgs/msg/detail/led_color__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "irobot_create_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "irobot_create_msgs/msg/detail/led_color__struct.h"
#include "irobot_create_msgs/msg/detail/led_color__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _LedColor__ros_msg_type = irobot_create_msgs__msg__LedColor;

static bool _LedColor__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _LedColor__ros_msg_type * ros_message = static_cast<const _LedColor__ros_msg_type *>(untyped_ros_message);
  // Field name: red
  {
    cdr << ros_message->red;
  }

  // Field name: green
  {
    cdr << ros_message->green;
  }

  // Field name: blue
  {
    cdr << ros_message->blue;
  }

  return true;
}

static bool _LedColor__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _LedColor__ros_msg_type * ros_message = static_cast<_LedColor__ros_msg_type *>(untyped_ros_message);
  // Field name: red
  {
    cdr >> ros_message->red;
  }

  // Field name: green
  {
    cdr >> ros_message->green;
  }

  // Field name: blue
  {
    cdr >> ros_message->blue;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_irobot_create_msgs
size_t get_serialized_size_irobot_create_msgs__msg__LedColor(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _LedColor__ros_msg_type * ros_message = static_cast<const _LedColor__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name red
  {
    size_t item_size = sizeof(ros_message->red);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name green
  {
    size_t item_size = sizeof(ros_message->green);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name blue
  {
    size_t item_size = sizeof(ros_message->blue);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _LedColor__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_irobot_create_msgs__msg__LedColor(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_irobot_create_msgs
size_t max_serialized_size_irobot_create_msgs__msg__LedColor(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: red
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: green
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: blue
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _LedColor__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_irobot_create_msgs__msg__LedColor(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_LedColor = {
  "irobot_create_msgs::msg",
  "LedColor",
  _LedColor__cdr_serialize,
  _LedColor__cdr_deserialize,
  _LedColor__get_serialized_size,
  _LedColor__max_serialized_size
};

static rosidl_message_type_support_t _LedColor__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_LedColor,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, irobot_create_msgs, msg, LedColor)() {
  return &_LedColor__type_support;
}

#if defined(__cplusplus)
}
#endif
