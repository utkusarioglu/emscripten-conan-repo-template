
install() {
  target_profile=$1
  build_type=$2

  build_type=${build_type:-'Release'}
  required_params='target_profile'
  
  for required_param in $required_params; do
    if [ -z "${!required_param}" ]; then
      echo "Error: ${required_param} needs to be set."
      exit 1
    fi
  done

  conan install . \
    -b 'missing' \
    -pr:b $(pwd)/profiles/build.profile \
    -pr:h $(pwd)/profiles/$target_profile.profile \
    --settings="build_type=$build_type" \
    --lockfile-out conan.lock \
    --lockfile conan.lock \
    --lockfile-partial
}

build() {
  target_profile=$1
  build_type=$2

  build_type=${build_type:-'Release'}
  required_params='target_profile'
  
  for required_param in $required_params; do
    if [ -z "${!required_param}" ]; then
      echo "Error: ${required_param} needs to be set."
      exit 1
    fi
  done

  conan build . \
    -pr:b $(pwd)/profiles/build.profile \
    -pr:h $(pwd)/profiles/$target_profile.profile \
    --settings="build_type=$build_type" \
    --lockfile-out conan.lock \
    --lockfile conan.lock
}

create() {
  target_profile=$1
  
  if [ -z "$target_profile" ]; then
    echo "Error: Target profile needs to be the first param"
    exit 1
  fi

  conan create . \
    -pr:b $(pwd)/profiles/build.profile \
    -pr:h $(pwd)/profiles/$target_profile.profile \
    --lockfile-out conan.lock \
    --lockfile conan.lock
}


clean() {
  build_type=$1

  if [ -z "$build_type" ]; then
    echo "Error: build type param is required"
    exit 1
  fi

  rm -rf "build/$build_type"
}

test() {
  target_profile=$1
  
  if [ -z "$target_profile" ]; then
    echo "Error: Target profile needs to be the first param"
    exit 1
  fi

  conan test \
    -pr:b $(pwd)/profiles/host.profile \
    -pr:h $(pwd)/profiles/$target_profile.profile \
    test_package \
    emscripten-conan-repo-template/1.0.0
}
