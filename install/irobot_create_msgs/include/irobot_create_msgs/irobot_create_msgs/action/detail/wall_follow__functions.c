// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from irobot_create_msgs:action/WallFollow.idl
// generated code does not contain a copyright notice
#include "irobot_create_msgs/action/detail/wall_follow__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `max_runtime`
#include "builtin_interfaces/msg/detail/duration__functions.h"

bool
irobot_create_msgs__action__WallFollow_Goal__init(irobot_create_msgs__action__WallFollow_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // follow_side
  // max_runtime
  if (!builtin_interfaces__msg__Duration__init(&msg->max_runtime)) {
    irobot_create_msgs__action__WallFollow_Goal__fini(msg);
    return false;
  }
  return true;
}

void
irobot_create_msgs__action__WallFollow_Goal__fini(irobot_create_msgs__action__WallFollow_Goal * msg)
{
  if (!msg) {
    return;
  }
  // follow_side
  // max_runtime
  builtin_interfaces__msg__Duration__fini(&msg->max_runtime);
}

bool
irobot_create_msgs__action__WallFollow_Goal__are_equal(const irobot_create_msgs__action__WallFollow_Goal * lhs, const irobot_create_msgs__action__WallFollow_Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // follow_side
  if (lhs->follow_side != rhs->follow_side) {
    return false;
  }
  // max_runtime
  if (!builtin_interfaces__msg__Duration__are_equal(
      &(lhs->max_runtime), &(rhs->max_runtime)))
  {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_Goal__copy(
  const irobot_create_msgs__action__WallFollow_Goal * input,
  irobot_create_msgs__action__WallFollow_Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // follow_side
  output->follow_side = input->follow_side;
  // max_runtime
  if (!builtin_interfaces__msg__Duration__copy(
      &(input->max_runtime), &(output->max_runtime)))
  {
    return false;
  }
  return true;
}

irobot_create_msgs__action__WallFollow_Goal *
irobot_create_msgs__action__WallFollow_Goal__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Goal * msg = (irobot_create_msgs__action__WallFollow_Goal *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_Goal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_Goal));
  bool success = irobot_create_msgs__action__WallFollow_Goal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_Goal__destroy(irobot_create_msgs__action__WallFollow_Goal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_Goal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_Goal__Sequence__init(irobot_create_msgs__action__WallFollow_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Goal * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_Goal *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_Goal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_Goal__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_Goal__Sequence__fini(irobot_create_msgs__action__WallFollow_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_Goal__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_Goal__Sequence *
irobot_create_msgs__action__WallFollow_Goal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Goal__Sequence * array = (irobot_create_msgs__action__WallFollow_Goal__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_Goal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_Goal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_Goal__Sequence__destroy(irobot_create_msgs__action__WallFollow_Goal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_Goal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_Goal__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_Goal__Sequence * lhs, const irobot_create_msgs__action__WallFollow_Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_Goal__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_Goal__Sequence * input,
  irobot_create_msgs__action__WallFollow_Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_Goal);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_Goal * data =
      (irobot_create_msgs__action__WallFollow_Goal *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_Goal__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_Goal__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `runtime`
// already included above
// #include "builtin_interfaces/msg/detail/duration__functions.h"

bool
irobot_create_msgs__action__WallFollow_Result__init(irobot_create_msgs__action__WallFollow_Result * msg)
{
  if (!msg) {
    return false;
  }
  // runtime
  if (!builtin_interfaces__msg__Duration__init(&msg->runtime)) {
    irobot_create_msgs__action__WallFollow_Result__fini(msg);
    return false;
  }
  return true;
}

void
irobot_create_msgs__action__WallFollow_Result__fini(irobot_create_msgs__action__WallFollow_Result * msg)
{
  if (!msg) {
    return;
  }
  // runtime
  builtin_interfaces__msg__Duration__fini(&msg->runtime);
}

bool
irobot_create_msgs__action__WallFollow_Result__are_equal(const irobot_create_msgs__action__WallFollow_Result * lhs, const irobot_create_msgs__action__WallFollow_Result * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // runtime
  if (!builtin_interfaces__msg__Duration__are_equal(
      &(lhs->runtime), &(rhs->runtime)))
  {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_Result__copy(
  const irobot_create_msgs__action__WallFollow_Result * input,
  irobot_create_msgs__action__WallFollow_Result * output)
{
  if (!input || !output) {
    return false;
  }
  // runtime
  if (!builtin_interfaces__msg__Duration__copy(
      &(input->runtime), &(output->runtime)))
  {
    return false;
  }
  return true;
}

irobot_create_msgs__action__WallFollow_Result *
irobot_create_msgs__action__WallFollow_Result__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Result * msg = (irobot_create_msgs__action__WallFollow_Result *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_Result), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_Result));
  bool success = irobot_create_msgs__action__WallFollow_Result__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_Result__destroy(irobot_create_msgs__action__WallFollow_Result * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_Result__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_Result__Sequence__init(irobot_create_msgs__action__WallFollow_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Result * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_Result *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_Result), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_Result__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_Result__Sequence__fini(irobot_create_msgs__action__WallFollow_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_Result__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_Result__Sequence *
irobot_create_msgs__action__WallFollow_Result__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Result__Sequence * array = (irobot_create_msgs__action__WallFollow_Result__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_Result__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_Result__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_Result__Sequence__destroy(irobot_create_msgs__action__WallFollow_Result__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_Result__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_Result__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_Result__Sequence * lhs, const irobot_create_msgs__action__WallFollow_Result__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_Result__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_Result__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_Result__Sequence * input,
  irobot_create_msgs__action__WallFollow_Result__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_Result);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_Result * data =
      (irobot_create_msgs__action__WallFollow_Result *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_Result__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_Result__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_Result__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
irobot_create_msgs__action__WallFollow_Feedback__init(irobot_create_msgs__action__WallFollow_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // engaged
  return true;
}

void
irobot_create_msgs__action__WallFollow_Feedback__fini(irobot_create_msgs__action__WallFollow_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // engaged
}

bool
irobot_create_msgs__action__WallFollow_Feedback__are_equal(const irobot_create_msgs__action__WallFollow_Feedback * lhs, const irobot_create_msgs__action__WallFollow_Feedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // engaged
  if (lhs->engaged != rhs->engaged) {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_Feedback__copy(
  const irobot_create_msgs__action__WallFollow_Feedback * input,
  irobot_create_msgs__action__WallFollow_Feedback * output)
{
  if (!input || !output) {
    return false;
  }
  // engaged
  output->engaged = input->engaged;
  return true;
}

irobot_create_msgs__action__WallFollow_Feedback *
irobot_create_msgs__action__WallFollow_Feedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Feedback * msg = (irobot_create_msgs__action__WallFollow_Feedback *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_Feedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_Feedback));
  bool success = irobot_create_msgs__action__WallFollow_Feedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_Feedback__destroy(irobot_create_msgs__action__WallFollow_Feedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_Feedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_Feedback__Sequence__init(irobot_create_msgs__action__WallFollow_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Feedback * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_Feedback *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_Feedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_Feedback__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_Feedback__Sequence__fini(irobot_create_msgs__action__WallFollow_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_Feedback__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_Feedback__Sequence *
irobot_create_msgs__action__WallFollow_Feedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_Feedback__Sequence * array = (irobot_create_msgs__action__WallFollow_Feedback__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_Feedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_Feedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_Feedback__Sequence__destroy(irobot_create_msgs__action__WallFollow_Feedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_Feedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_Feedback__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_Feedback__Sequence * lhs, const irobot_create_msgs__action__WallFollow_Feedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_Feedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_Feedback__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_Feedback__Sequence * input,
  irobot_create_msgs__action__WallFollow_Feedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_Feedback);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_Feedback * data =
      (irobot_create_msgs__action__WallFollow_Feedback *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_Feedback__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_Feedback__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_Feedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "irobot_create_msgs/action/detail/wall_follow__functions.h"

bool
irobot_create_msgs__action__WallFollow_SendGoal_Request__init(irobot_create_msgs__action__WallFollow_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    irobot_create_msgs__action__WallFollow_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!irobot_create_msgs__action__WallFollow_Goal__init(&msg->goal)) {
    irobot_create_msgs__action__WallFollow_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Request__fini(irobot_create_msgs__action__WallFollow_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  irobot_create_msgs__action__WallFollow_Goal__fini(&msg->goal);
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Request__are_equal(const irobot_create_msgs__action__WallFollow_SendGoal_Request * lhs, const irobot_create_msgs__action__WallFollow_SendGoal_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // goal
  if (!irobot_create_msgs__action__WallFollow_Goal__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Request__copy(
  const irobot_create_msgs__action__WallFollow_SendGoal_Request * input,
  irobot_create_msgs__action__WallFollow_SendGoal_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // goal
  if (!irobot_create_msgs__action__WallFollow_Goal__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

irobot_create_msgs__action__WallFollow_SendGoal_Request *
irobot_create_msgs__action__WallFollow_SendGoal_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_SendGoal_Request * msg = (irobot_create_msgs__action__WallFollow_SendGoal_Request *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Request));
  bool success = irobot_create_msgs__action__WallFollow_SendGoal_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Request__destroy(irobot_create_msgs__action__WallFollow_SendGoal_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_SendGoal_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__init(irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_SendGoal_Request * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_SendGoal_Request *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_SendGoal_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__fini(irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_SendGoal_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence *
irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * array = (irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__destroy(irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * lhs, const irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_SendGoal_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * input,
  irobot_create_msgs__action__WallFollow_SendGoal_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_SendGoal_Request * data =
      (irobot_create_msgs__action__WallFollow_SendGoal_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_SendGoal_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_SendGoal_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_SendGoal_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
irobot_create_msgs__action__WallFollow_SendGoal_Response__init(irobot_create_msgs__action__WallFollow_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    irobot_create_msgs__action__WallFollow_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Response__fini(irobot_create_msgs__action__WallFollow_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Response__are_equal(const irobot_create_msgs__action__WallFollow_SendGoal_Response * lhs, const irobot_create_msgs__action__WallFollow_SendGoal_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // accepted
  if (lhs->accepted != rhs->accepted) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Response__copy(
  const irobot_create_msgs__action__WallFollow_SendGoal_Response * input,
  irobot_create_msgs__action__WallFollow_SendGoal_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // accepted
  output->accepted = input->accepted;
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  return true;
}

irobot_create_msgs__action__WallFollow_SendGoal_Response *
irobot_create_msgs__action__WallFollow_SendGoal_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_SendGoal_Response * msg = (irobot_create_msgs__action__WallFollow_SendGoal_Response *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Response));
  bool success = irobot_create_msgs__action__WallFollow_SendGoal_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Response__destroy(irobot_create_msgs__action__WallFollow_SendGoal_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_SendGoal_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__init(irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_SendGoal_Response * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_SendGoal_Response *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_SendGoal_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__fini(irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_SendGoal_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence *
irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * array = (irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__destroy(irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * lhs, const irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_SendGoal_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * input,
  irobot_create_msgs__action__WallFollow_SendGoal_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_SendGoal_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_SendGoal_Response * data =
      (irobot_create_msgs__action__WallFollow_SendGoal_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_SendGoal_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_SendGoal_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_SendGoal_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
irobot_create_msgs__action__WallFollow_GetResult_Request__init(irobot_create_msgs__action__WallFollow_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    irobot_create_msgs__action__WallFollow_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Request__fini(irobot_create_msgs__action__WallFollow_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Request__are_equal(const irobot_create_msgs__action__WallFollow_GetResult_Request * lhs, const irobot_create_msgs__action__WallFollow_GetResult_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Request__copy(
  const irobot_create_msgs__action__WallFollow_GetResult_Request * input,
  irobot_create_msgs__action__WallFollow_GetResult_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  return true;
}

irobot_create_msgs__action__WallFollow_GetResult_Request *
irobot_create_msgs__action__WallFollow_GetResult_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_GetResult_Request * msg = (irobot_create_msgs__action__WallFollow_GetResult_Request *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_GetResult_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_GetResult_Request));
  bool success = irobot_create_msgs__action__WallFollow_GetResult_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Request__destroy(irobot_create_msgs__action__WallFollow_GetResult_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_GetResult_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__init(irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_GetResult_Request * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_GetResult_Request *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_GetResult_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_GetResult_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__fini(irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_GetResult_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence *
irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * array = (irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__destroy(irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * lhs, const irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_GetResult_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * input,
  irobot_create_msgs__action__WallFollow_GetResult_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_GetResult_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_GetResult_Request * data =
      (irobot_create_msgs__action__WallFollow_GetResult_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_GetResult_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_GetResult_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_GetResult_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `result`
// already included above
// #include "irobot_create_msgs/action/detail/wall_follow__functions.h"

bool
irobot_create_msgs__action__WallFollow_GetResult_Response__init(irobot_create_msgs__action__WallFollow_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!irobot_create_msgs__action__WallFollow_Result__init(&msg->result)) {
    irobot_create_msgs__action__WallFollow_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Response__fini(irobot_create_msgs__action__WallFollow_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  irobot_create_msgs__action__WallFollow_Result__fini(&msg->result);
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Response__are_equal(const irobot_create_msgs__action__WallFollow_GetResult_Response * lhs, const irobot_create_msgs__action__WallFollow_GetResult_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // result
  if (!irobot_create_msgs__action__WallFollow_Result__are_equal(
      &(lhs->result), &(rhs->result)))
  {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Response__copy(
  const irobot_create_msgs__action__WallFollow_GetResult_Response * input,
  irobot_create_msgs__action__WallFollow_GetResult_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  // result
  if (!irobot_create_msgs__action__WallFollow_Result__copy(
      &(input->result), &(output->result)))
  {
    return false;
  }
  return true;
}

irobot_create_msgs__action__WallFollow_GetResult_Response *
irobot_create_msgs__action__WallFollow_GetResult_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_GetResult_Response * msg = (irobot_create_msgs__action__WallFollow_GetResult_Response *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_GetResult_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_GetResult_Response));
  bool success = irobot_create_msgs__action__WallFollow_GetResult_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Response__destroy(irobot_create_msgs__action__WallFollow_GetResult_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_GetResult_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__init(irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_GetResult_Response * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_GetResult_Response *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_GetResult_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_GetResult_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__fini(irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_GetResult_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence *
irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * array = (irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__destroy(irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * lhs, const irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_GetResult_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * input,
  irobot_create_msgs__action__WallFollow_GetResult_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_GetResult_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_GetResult_Response * data =
      (irobot_create_msgs__action__WallFollow_GetResult_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_GetResult_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_GetResult_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_GetResult_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "irobot_create_msgs/action/detail/wall_follow__functions.h"

bool
irobot_create_msgs__action__WallFollow_FeedbackMessage__init(irobot_create_msgs__action__WallFollow_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    irobot_create_msgs__action__WallFollow_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!irobot_create_msgs__action__WallFollow_Feedback__init(&msg->feedback)) {
    irobot_create_msgs__action__WallFollow_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
irobot_create_msgs__action__WallFollow_FeedbackMessage__fini(irobot_create_msgs__action__WallFollow_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  irobot_create_msgs__action__WallFollow_Feedback__fini(&msg->feedback);
}

bool
irobot_create_msgs__action__WallFollow_FeedbackMessage__are_equal(const irobot_create_msgs__action__WallFollow_FeedbackMessage * lhs, const irobot_create_msgs__action__WallFollow_FeedbackMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // feedback
  if (!irobot_create_msgs__action__WallFollow_Feedback__are_equal(
      &(lhs->feedback), &(rhs->feedback)))
  {
    return false;
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_FeedbackMessage__copy(
  const irobot_create_msgs__action__WallFollow_FeedbackMessage * input,
  irobot_create_msgs__action__WallFollow_FeedbackMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // feedback
  if (!irobot_create_msgs__action__WallFollow_Feedback__copy(
      &(input->feedback), &(output->feedback)))
  {
    return false;
  }
  return true;
}

irobot_create_msgs__action__WallFollow_FeedbackMessage *
irobot_create_msgs__action__WallFollow_FeedbackMessage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_FeedbackMessage * msg = (irobot_create_msgs__action__WallFollow_FeedbackMessage *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_FeedbackMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(irobot_create_msgs__action__WallFollow_FeedbackMessage));
  bool success = irobot_create_msgs__action__WallFollow_FeedbackMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
irobot_create_msgs__action__WallFollow_FeedbackMessage__destroy(irobot_create_msgs__action__WallFollow_FeedbackMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    irobot_create_msgs__action__WallFollow_FeedbackMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__init(irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_FeedbackMessage * data = NULL;

  if (size) {
    data = (irobot_create_msgs__action__WallFollow_FeedbackMessage *)allocator.zero_allocate(size, sizeof(irobot_create_msgs__action__WallFollow_FeedbackMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = irobot_create_msgs__action__WallFollow_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        irobot_create_msgs__action__WallFollow_FeedbackMessage__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__fini(irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      irobot_create_msgs__action__WallFollow_FeedbackMessage__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence *
irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * array = (irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence *)allocator.allocate(sizeof(irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__destroy(irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__are_equal(const irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * lhs, const irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_FeedbackMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence__copy(
  const irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * input,
  irobot_create_msgs__action__WallFollow_FeedbackMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(irobot_create_msgs__action__WallFollow_FeedbackMessage);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    irobot_create_msgs__action__WallFollow_FeedbackMessage * data =
      (irobot_create_msgs__action__WallFollow_FeedbackMessage *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!irobot_create_msgs__action__WallFollow_FeedbackMessage__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          irobot_create_msgs__action__WallFollow_FeedbackMessage__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!irobot_create_msgs__action__WallFollow_FeedbackMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
