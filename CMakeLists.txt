cmake_minimum_required(VERSION 3.22)
project(emscripten-conan-repo-template)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
file(GLOB_RECURSE sources 
  ${PROJECT_SOURCE_DIR}/src/*.hh
  ${PROJECT_SOURCE_DIR}/src/*.cc
)

add_executable(${PROJECT_NAME} ${sources})
target_include_directories(${PROJECT_NAME} PRIVATE ${CONAN_INCLUDE_DIRS})
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 20)

target_link_libraries(${PROJECT_NAME} PRIVATE ${CONAN_LIBS})

if (${CMAKE_SYSTEM_NAME} MATCHES "Emscripten")
  set_target_properties(
      ${PROJECT_NAME}
      PROPERTIES 
          OUTPUT_NAME "${PROJECT_NAME}.wasm"
          SUFFIX ".js"
  )

  set_target_properties(${PROJECT_NAME} PROPERTIES LINK_FLAGS
    "-O3 \
    -o ${PROJECT_NAME}.js \
    -s WASM=1 \
    -s ENVIRONMENT=web \
    -s SINGLE_FILE=1 \
    -s EXPORT_ES6=1 \
    -s EXPORTED_RUNTIME_METHODS=['UTF8ToString'] \
    -s ASSERTIONS=1 \
    --bind"  
  )
    # -s USE_SDL=2 \
    # -s USE_SDL_IMAGE=2 \
    # -s SDL2_IMAGE_FORMATS='[\"png\"]' \
    # -s EXPORT_NAME=wasm \
    # --preload-file ../assets \

  file(COPY public/index.html DESTINATION ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})

else()
  set_target_properties(
      PROPERTIES 
          OUTPUT_NAME "${PROJECT_NAME}"
          SUFFIX ""
  )
endif()
