from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from os import getcwd, mkdir
from shutil import copy2

class Emscripten(ConanFile):  
    name = "emscripten-conan-repo-template"
    version = "1.0.0"
    package_type = "application"
    build_policy = "missing"
    settings = "os", "arch", "compiler", "build_type"

    exports = "CMakeLists.txt",

    # build_folder = "build"
    # package_folder = "p"

    # source_folder = "."
    # package_folder = "lib"
    # generators_folder = "build"
    # generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("spdlog/1.12.0")
        self.test_requires("gtest/1.8.1")
    
    # def imports(self):
    #     self.copy("*.html", dst="bin", src="bin")
    #     self.copy("*.js", dst="bin", src="bin")
    #     self.copy("*.wasm", dst="bin", src="bin")
    
    # def test(self):
    #     print("Do this later, it requires knowing how to package code")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [self.name]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        self._after_build()

    def _after_build(self):
        release_dir = getcwd()
        base_folder = self.folders._base_source
        match self.settings.os:
            case "Emscripten":
                print("Creating bin for Emscripten…")
                mkdir("bin")
                public_dir = f"{base_folder}/public"
                copy2(f"{release_dir}/{self.name}.js", f"{release_dir}/bin/wasm.js")
                copy2(f"{public_dir}/index.html", f"{release_dir}/bin/index.html")
            case "Linux":
                print("Creating bin for Linux…")
                mkdir("bin")
                copy2(f"{release_dir}/{self.name}", f"{release_dir}/bin/bin")

            case _:
                print("Unknown os")
