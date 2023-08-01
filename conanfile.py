from conan import ConanFile
from conan.tools.cmake import CMake

class Emscripten(ConanFile):  
    requires = [
        "gtest/1.8.1"
        # "rapidjson/cci.20211112",
    ]
    name = "emscripten-conan-repo-template"
    version = "1.0.0"
    build_folder = "build"
    source_folder = "src"
    recipe_folder = "dependencies"
    # generators = "cmake"
#     default_options = {
#         "openssl/*:shared": False,
#         "sdl_image/*:with_libtiff": False,
# # "rapidjson:shared": False
#     }
#   settings = {"os": ["Emscripten", "Linux", "Windows"]} 
  # install_folder = "build"
  # build_policy = "missing"
    # def validate(self):
    #     if self.settings.os is "Macos":
    #         raise ConanInvalidConfiguration("Macos not defined")

    def imports(self):
        self.copy("*.html", dst="bin", src="bin")
        self.copy("*.js", dst="bin", src="bin")
        self.copy("*.wasm", dst="bin", src="bin")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
