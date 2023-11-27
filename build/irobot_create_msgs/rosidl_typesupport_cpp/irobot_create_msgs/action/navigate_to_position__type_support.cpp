// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from irobot_create_msgs:action/NavigateToPosition.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_Goal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_Goal_type_support_ids_t;

static const _NavigateToPosition_Goal_type_support_ids_t _NavigateToPosition_Goal_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_Goal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_Goal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_Goal_type_support_symbol_names_t _NavigateToPosition_Goal_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_Goal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_Goal)),
  }
};

typedef struct _NavigateToPosition_Goal_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_Goal_type_support_data_t;

static _NavigateToPosition_Goal_type_support_data_t _NavigateToPosition_Goal_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_Goal_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_Goal_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_Goal_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_Goal_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_Goal_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_Goal_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_Goal>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_Goal_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_Goal)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_Goal>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_Result_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_Result_type_support_ids_t;

static const _NavigateToPosition_Result_type_support_ids_t _NavigateToPosition_Result_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_Result_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_Result_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_Result_type_support_symbol_names_t _NavigateToPosition_Result_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_Result)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_Result)),
  }
};

typedef struct _NavigateToPosition_Result_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_Result_type_support_data_t;

static _NavigateToPosition_Result_type_support_data_t _NavigateToPosition_Result_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_Result_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_Result_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_Result_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_Result_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_Result_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_Result_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_Result>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_Result_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_Result)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_Result>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_Feedback_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_Feedback_type_support_ids_t;

static const _NavigateToPosition_Feedback_type_support_ids_t _NavigateToPosition_Feedback_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_Feedback_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_Feedback_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_Feedback_type_support_symbol_names_t _NavigateToPosition_Feedback_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_Feedback)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_Feedback)),
  }
};

typedef struct _NavigateToPosition_Feedback_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_Feedback_type_support_data_t;

static _NavigateToPosition_Feedback_type_support_data_t _NavigateToPosition_Feedback_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_Feedback_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_Feedback_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_Feedback_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_Feedback_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_Feedback_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_Feedback_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_Feedback>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_Feedback_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_Feedback)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_Feedback>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_SendGoal_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_SendGoal_Request_type_support_ids_t;

static const _NavigateToPosition_SendGoal_Request_type_support_ids_t _NavigateToPosition_SendGoal_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_SendGoal_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_SendGoal_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_SendGoal_Request_type_support_symbol_names_t _NavigateToPosition_SendGoal_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal_Request)),
  }
};

typedef struct _NavigateToPosition_SendGoal_Request_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_SendGoal_Request_type_support_data_t;

static _NavigateToPosition_SendGoal_Request_type_support_data_t _NavigateToPosition_SendGoal_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_SendGoal_Request_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_SendGoal_Request_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_SendGoal_Request_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_SendGoal_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_SendGoal_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_SendGoal_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_SendGoal_Request>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_SendGoal_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal_Request)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_SendGoal_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_SendGoal_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_SendGoal_Response_type_support_ids_t;

static const _NavigateToPosition_SendGoal_Response_type_support_ids_t _NavigateToPosition_SendGoal_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_SendGoal_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_SendGoal_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_SendGoal_Response_type_support_symbol_names_t _NavigateToPosition_SendGoal_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal_Response)),
  }
};

typedef struct _NavigateToPosition_SendGoal_Response_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_SendGoal_Response_type_support_data_t;

static _NavigateToPosition_SendGoal_Response_type_support_data_t _NavigateToPosition_SendGoal_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_SendGoal_Response_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_SendGoal_Response_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_SendGoal_Response_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_SendGoal_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_SendGoal_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_SendGoal_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_SendGoal_Response>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_SendGoal_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal_Response)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_SendGoal_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_SendGoal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_SendGoal_type_support_ids_t;

static const _NavigateToPosition_SendGoal_type_support_ids_t _NavigateToPosition_SendGoal_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_SendGoal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_SendGoal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_SendGoal_type_support_symbol_names_t _NavigateToPosition_SendGoal_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_SendGoal)),
  }
};

typedef struct _NavigateToPosition_SendGoal_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_SendGoal_type_support_data_t;

static _NavigateToPosition_SendGoal_type_support_data_t _NavigateToPosition_SendGoal_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_SendGoal_service_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_SendGoal_service_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_SendGoal_service_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_SendGoal_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t NavigateToPosition_SendGoal_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_SendGoal_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<irobot_create_msgs::action::NavigateToPosition_SendGoal>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_SendGoal_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_GetResult_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_GetResult_Request_type_support_ids_t;

static const _NavigateToPosition_GetResult_Request_type_support_ids_t _NavigateToPosition_GetResult_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_GetResult_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_GetResult_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_GetResult_Request_type_support_symbol_names_t _NavigateToPosition_GetResult_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult_Request)),
  }
};

typedef struct _NavigateToPosition_GetResult_Request_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_GetResult_Request_type_support_data_t;

static _NavigateToPosition_GetResult_Request_type_support_data_t _NavigateToPosition_GetResult_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_GetResult_Request_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_GetResult_Request_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_GetResult_Request_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_GetResult_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_GetResult_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_GetResult_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_GetResult_Request>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_GetResult_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult_Request)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_GetResult_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_GetResult_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_GetResult_Response_type_support_ids_t;

static const _NavigateToPosition_GetResult_Response_type_support_ids_t _NavigateToPosition_GetResult_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_GetResult_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_GetResult_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_GetResult_Response_type_support_symbol_names_t _NavigateToPosition_GetResult_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult_Response)),
  }
};

typedef struct _NavigateToPosition_GetResult_Response_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_GetResult_Response_type_support_data_t;

static _NavigateToPosition_GetResult_Response_type_support_data_t _NavigateToPosition_GetResult_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_GetResult_Response_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_GetResult_Response_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_GetResult_Response_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_GetResult_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_GetResult_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_GetResult_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_GetResult_Response>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_GetResult_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult_Response)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_GetResult_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_GetResult_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_GetResult_type_support_ids_t;

static const _NavigateToPosition_GetResult_type_support_ids_t _NavigateToPosition_GetResult_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_GetResult_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_GetResult_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_GetResult_type_support_symbol_names_t _NavigateToPosition_GetResult_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_GetResult)),
  }
};

typedef struct _NavigateToPosition_GetResult_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_GetResult_type_support_data_t;

static _NavigateToPosition_GetResult_type_support_data_t _NavigateToPosition_GetResult_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_GetResult_service_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_GetResult_service_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_GetResult_service_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_GetResult_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t NavigateToPosition_GetResult_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_GetResult_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<irobot_create_msgs::action::NavigateToPosition_GetResult>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_GetResult_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _NavigateToPosition_FeedbackMessage_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NavigateToPosition_FeedbackMessage_type_support_ids_t;

static const _NavigateToPosition_FeedbackMessage_type_support_ids_t _NavigateToPosition_FeedbackMessage_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NavigateToPosition_FeedbackMessage_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NavigateToPosition_FeedbackMessage_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NavigateToPosition_FeedbackMessage_type_support_symbol_names_t _NavigateToPosition_FeedbackMessage_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, irobot_create_msgs, action, NavigateToPosition_FeedbackMessage)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, irobot_create_msgs, action, NavigateToPosition_FeedbackMessage)),
  }
};

typedef struct _NavigateToPosition_FeedbackMessage_type_support_data_t
{
  void * data[2];
} _NavigateToPosition_FeedbackMessage_type_support_data_t;

static _NavigateToPosition_FeedbackMessage_type_support_data_t _NavigateToPosition_FeedbackMessage_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NavigateToPosition_FeedbackMessage_message_typesupport_map = {
  2,
  "irobot_create_msgs",
  &_NavigateToPosition_FeedbackMessage_message_typesupport_ids.typesupport_identifier[0],
  &_NavigateToPosition_FeedbackMessage_message_typesupport_symbol_names.symbol_name[0],
  &_NavigateToPosition_FeedbackMessage_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NavigateToPosition_FeedbackMessage_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NavigateToPosition_FeedbackMessage_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_FeedbackMessage>()
{
  return &::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_FeedbackMessage_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, irobot_create_msgs, action, NavigateToPosition_FeedbackMessage)() {
  return get_message_type_support_handle<irobot_create_msgs::action::NavigateToPosition_FeedbackMessage>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

#include "action_msgs/msg/goal_status_array.hpp"
#include "action_msgs/srv/cancel_goal.hpp"
// already included above
// #include "irobot_create_msgs/action/detail/navigate_to_position__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_typesupport_cpp/action_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"

namespace irobot_create_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

static rosidl_action_type_support_t NavigateToPosition_action_type_support_handle = {
  NULL, NULL, NULL, NULL, NULL};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace irobot_create_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_action_type_support_t *
get_action_type_support_handle<irobot_create_msgs::action::NavigateToPosition>()
{
  using ::irobot_create_msgs::action::rosidl_typesupport_cpp::NavigateToPosition_action_type_support_handle;
  // Thread-safe by always writing the same values to the static struct
  NavigateToPosition_action_type_support_handle.goal_service_type_support = get_service_type_support_handle<::irobot_create_msgs::action::NavigateToPosition::Impl::SendGoalService>();
  NavigateToPosition_action_type_support_handle.result_service_type_support = get_service_type_support_handle<::irobot_create_msgs::action::NavigateToPosition::Impl::GetResultService>();
  NavigateToPosition_action_type_support_handle.cancel_service_type_support = get_service_type_support_handle<::irobot_create_msgs::action::NavigateToPosition::Impl::CancelGoalService>();
  NavigateToPosition_action_type_support_handle.feedback_message_type_support = get_message_type_support_handle<::irobot_create_msgs::action::NavigateToPosition::Impl::FeedbackMessage>();
  NavigateToPosition_action_type_support_handle.status_message_type_support = get_message_type_support_handle<::irobot_create_msgs::action::NavigateToPosition::Impl::GoalStatusMessage>();
  return &NavigateToPosition_action_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp
