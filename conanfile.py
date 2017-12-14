from conans import ConanFile, CMake, tools


class ExtraCMakeModulesConan(ConanFile):
    name = "extra-cmake-modules"
    version = "5.41.0"
    license = "BSD 3-Clause"
    url = "https://api.kde.org/frameworks/extra-cmake-modules/html/index.html"
    settings = "compiler", "build_type", "arch"
    description = "Extra CMake modules"
    generators = "cmake"

    def source(self):
        shortened_version = self.version.rpartition('.')[0]
        download_url = "https://download.kde.org/stable/frameworks/%s/%s-%s.tar.xz" % (shortened_version, self.name, self.version)
        tools.download(download_url, "source.tar.xz")
        self.run("cmake -E tar xf source.tar.xz")

    def build(self):
        cmake = CMake(self)

        cmake.definitions['CMAKE_INSTALL_PREFIX'] = self.package_folder
        cmake.definitions['BUILD_HTML_DOCS'] = 0
        cmake.definitions['BUILD_QTHELP_DOCS'] = 0
        cmake.definitions['BUILD_TESTING'] = 0

        cmake.configure(source_dir="%s/%s-%s" % (self.source_folder, self.name, self.version))
        cmake.build()
        cmake.install()
