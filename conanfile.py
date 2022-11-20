from conans import ConanFile, CMake

class Emscripten(ConanFile):  
  requires = [
    "rapidjson/cci.20211112",
  ]
  name = "emscripten-conan-repo-template"
  version = "1.0.0"
  generators = "cmake"
  default_options = {
    "openssl:shared": False,
    "sdl_image:with_libtiff": False,
    # "rapidjson:shared": False
  }
  settings = {"os": ["Emscripten", "Linux", "Windows"]} 
  # install_folder = "build"
  # build_policy = "missing"

  def imports(self):
    self.copy("*.html", dst="bin", src="bin")
    self.copy("*.js", dst="bin", src="bin")
    self.copy("*.wasm", dst="bin", src="bin")

  def build(self):
    cmake = CMake(self)
    cmake.configure()
    cmake.build()
