// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from irobot_create_msgs:msg/IrIntensity.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "irobot_create_msgs/msg/detail/ir_intensity__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace irobot_create_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void IrIntensity_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) irobot_create_msgs::msg::IrIntensity(_init);
}

void IrIntensity_fini_function(void * message_memory)
{
  auto typed_message = static_cast<irobot_create_msgs::msg::IrIntensity *>(message_memory);
  typed_message->~IrIntensity();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember IrIntensity_message_member_array[2] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(irobot_create_msgs::msg::IrIntensity, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "value",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(irobot_create_msgs::msg::IrIntensity, value),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers IrIntensity_message_members = {
  "irobot_create_msgs::msg",  // message namespace
  "IrIntensity",  // message name
  2,  // number of fields
  sizeof(irobot_create_msgs::msg::IrIntensity),
  IrIntensity_message_member_array,  // message members
  IrIntensity_init_function,  // function to initialize message memory (memory has to be allocated)
  IrIntensity_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t IrIntensity_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &IrIntensity_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace irobot_create_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::msg::IrIntensity>()
{
  return &::irobot_create_msgs::msg::rosidl_typesupport_introspection_cpp::IrIntensity_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, msg, IrIntensity)() {
  return &::irobot_create_msgs::msg::rosidl_typesupport_introspection_cpp::IrIntensity_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
