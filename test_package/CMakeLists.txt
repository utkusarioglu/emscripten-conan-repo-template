cmake_minimum_required(VERSION 3.22)
project(PackageTest CXX)

find_package(emscripten-conan-repo-template CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example emscripten-conan-repo-template::emscripten-conan-repo-template)
