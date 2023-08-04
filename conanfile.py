from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class Emscripten(ConanFile):  
    name = "emscripten-conan-repo-template"
    version = "1.0.0"
    package_type = "application"
    build_policy = "missing"
    settings = "os", "arch", "compiler", "build_type"

    build_folder = "build"

    # source_folder = "."
    # package_folder = "lib"
    # generators_folder = "build"
    # generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        self.folders.build = "b"
        self.folders.generators = "generators"

    def requirements(self):
        self.requires("spdlog/1.12.0")
    
    def test_requirements(self):
        self.test_requires("gtest/1.8.1")

    # def imports(self):
    #     self.copy("*.html", dst="bin", src="bin")
    #     self.copy("*.js", dst="bin", src="bin")
    #     self.copy("*.wasm", dst="bin", src="bin")

    def deploy(conanfile, output_folder, **kwargs):
        print(f"output folder: {output_folder}")
    

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
