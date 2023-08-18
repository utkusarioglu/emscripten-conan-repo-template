from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from os import getcwd, makedirs, chmod
from stat import S_IRWXG, S_IRWXU, S_IROTH, S_IXOTH 
from shutil import copy2

class Emscripten(ConanFile):  
    name = "emscripten-conan-repo-template"
    version = "1.0.0"
    package_type = "application"
    build_policy = "missing"
    settings = "os", "arch", "compiler", "build_type"

    exports = "CMakeLists.txt",

    # def configure(self):
    #     self.options["spdlog"].shared = True

    def layout(self):
        # cmake_layout(self)
        build_type = str(self.settings.build_type).lower()
        os = str(self.settings.os).lower()

        self.folders.source = "."
        self.folders.build = f"build/{os}/{build_type}"
        self.folders.generators = f"build/{os}/{build_type}/generators"
        self.cpp.source.includeDirs = ["include"]
        self.cpp.build.libdirs = "."
        self.cpp.build.bindirs = "."


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
        os = self.settings.os

        match os:
            case "Emscripten":
                print("Creating bin for Emscripten…")
                makedirs("bin", exist_ok=True)
                public_dir = f"{base_folder}/public"
                copy2(f"{release_dir}/{self.name}.js", f"{release_dir}/bin/wasm.js")
                copy2(f"{public_dir}/index.html", f"{release_dir}/bin/index.html")
            case "Linux":
                print("Creating bin for Linux…")
                makedirs("bin", exist_ok=True)
                source = f"{release_dir}/{self.name}"
                target = f"{release_dir}/bin/{self.name}"
                copy2(source, target)
                chmod(target, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH)

            case _:
                print("Unknown os")
