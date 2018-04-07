cmake_minimum_required(VERSION 3.8)
project(A1)

set(CMAKE_CXX_STANDARD 11)

# Do not modify these flags other than changing -ggdb to -O2 and back.
set(CMAKE_CXX_FLAGS "-ggdb -std=c++11 -Wall -Wctor-dtor-privacy -Wuninitialized -Winit-self -Wlogical-op -Wredundant-decls -Wshadow -Werror -Wno-unused -Wno-sign-compare -Wno-reorder -Wno-unused-variable")

add_library(a1-obj OBJECT a1.cpp)
add_library(main-obj OBJECT main.cpp)
add_executable(a1 $<TARGET_OBJECTS:a1-obj> $<TARGET_OBJECTS:main-obj>)