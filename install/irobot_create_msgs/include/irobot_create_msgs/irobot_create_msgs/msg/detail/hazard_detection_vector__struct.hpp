// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from irobot_create_msgs:msg/HazardDetectionVector.idl
// generated code does not contain a copyright notice

#ifndef IROBOT_CREATE_MSGS__MSG__DETAIL__HAZARD_DETECTION_VECTOR__STRUCT_HPP_
#define IROBOT_CREATE_MSGS__MSG__DETAIL__HAZARD_DETECTION_VECTOR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'detections'
#include "irobot_create_msgs/msg/detail/hazard_detection__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__irobot_create_msgs__msg__HazardDetectionVector __attribute__((deprecated))
#else
# define DEPRECATED__irobot_create_msgs__msg__HazardDetectionVector __declspec(deprecated)
#endif

namespace irobot_create_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HazardDetectionVector_
{
  using Type = HazardDetectionVector_<ContainerAllocator>;

  explicit HazardDetectionVector_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    (void)_init;
  }

  explicit HazardDetectionVector_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _detections_type =
    std::vector<irobot_create_msgs::msg::HazardDetection_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<irobot_create_msgs::msg::HazardDetection_<ContainerAllocator>>>;
  _detections_type detections;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__detections(
    const std::vector<irobot_create_msgs::msg::HazardDetection_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<irobot_create_msgs::msg::HazardDetection_<ContainerAllocator>>> & _arg)
  {
    this->detections = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator> *;
  using ConstRawPtr =
    const irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__irobot_create_msgs__msg__HazardDetectionVector
    std::shared_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__irobot_create_msgs__msg__HazardDetectionVector
    std::shared_ptr<irobot_create_msgs::msg::HazardDetectionVector_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HazardDetectionVector_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->detections != other.detections) {
      return false;
    }
    return true;
  }
  bool operator!=(const HazardDetectionVector_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HazardDetectionVector_

// alias to use template instance with default allocator
using HazardDetectionVector =
  irobot_create_msgs::msg::HazardDetectionVector_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace irobot_create_msgs

#endif  // IROBOT_CREATE_MSGS__MSG__DETAIL__HAZARD_DETECTION_VECTOR__STRUCT_HPP_
