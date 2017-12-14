# Extra CMake modules
[ ![Download](https://api.bintray.com/packages/mmha/conan/extra-cmake-modules%3Ammha/images/download.svg) ](https://bintray.com/mmha/conan/extra-cmake-modules%3Ammha/_latestVersion)

[Conan.io](https://conan.io) package for [extra-cmake-modules](https://api.kde.org/frameworks/extra-cmake-modules/html/index.html) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/mmha/conan/extra-cmake-modules).

## For Users: Use this package

### Basic setup

    $ conan install extra-cmake-modules/5.41.0@mmha/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    extra-cmake-modules/5.41.0@mmha/testing

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## License
[BSD 3-Clause](LICENSE)
