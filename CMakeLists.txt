cmake_minimum_required(VERSION 3.22)
project(emscripten-conan-repo-template)

find_package(spdlog REQUIRED)

add_executable(${PROJECT_NAME} src/main.cc)

target_link_libraries(${PROJECT_NAME} spdlog::spdlog)
