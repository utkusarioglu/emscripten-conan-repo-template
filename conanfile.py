from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class Emscripten(ConanFile):  
    requires = [
        "spdlog/1.12.0",
    ]
    test_requires = [
        "gtest/1.8.1"
    ]
    name = "emscripten-conan-repo-template"
    version = "1.0.0"
    build_policy = "missing"
    # build_folder = "build"

    source_folder = "src"
    package_folder = "lib"
    generators_folder = "build"
    # generators = "CMakeDeps", "CMakeToolchain"

    # def imports(self):
    #     self.copy("*.html", dst="bin", src="bin")
    #     self.copy("*.js", dst="bin", src="bin")
    #     self.copy("*.wasm", dst="bin", src="bin")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
