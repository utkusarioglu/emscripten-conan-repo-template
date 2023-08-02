cmake_minimum_required(VERSION 3.22)
project(emscripten-conan-repo-template)

add_executable(${PROJECT_NAME} src/main.cc)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
