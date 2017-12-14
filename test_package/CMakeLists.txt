project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(ECM REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH})
include(ECMGenerateHeaders)

add_library(MyLib INTERFACE)
target_include_directories(MyLib INTERFACE "${CMAKE_CURRENT_SOURCE_DIR}" "${CMAKE_CURRENT_BINARY_DIR}")
ecm_generate_headers(
    MyLib_FORWARDING_HEADERS
    HEADER_NAMES MLFoo
    REQUIRED_HEADERS MyLib_HEADERS
)

add_executable(example example.cpp)
target_link_libraries(example MyLib)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
