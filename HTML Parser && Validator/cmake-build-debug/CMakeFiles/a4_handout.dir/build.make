# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Users/austinmccarson/Desktop/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Users/austinmccarson/Desktop/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/austinmccarson/Downloads/a4-handout

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/austinmccarson/Downloads/a4-handout/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/a4_handout.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/a4_handout.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/a4_handout.dir/flags.make

CMakeFiles/a4_handout.dir/a4.cpp.o: CMakeFiles/a4_handout.dir/flags.make
CMakeFiles/a4_handout.dir/a4.cpp.o: ../a4.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/austinmccarson/Downloads/a4-handout/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/a4_handout.dir/a4.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/a4_handout.dir/a4.cpp.o -c /Users/austinmccarson/Downloads/a4-handout/a4.cpp

CMakeFiles/a4_handout.dir/a4.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/a4_handout.dir/a4.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/austinmccarson/Downloads/a4-handout/a4.cpp > CMakeFiles/a4_handout.dir/a4.cpp.i

CMakeFiles/a4_handout.dir/a4.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/a4_handout.dir/a4.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/austinmccarson/Downloads/a4-handout/a4.cpp -o CMakeFiles/a4_handout.dir/a4.cpp.s

CMakeFiles/a4_handout.dir/a4.cpp.o.requires:

.PHONY : CMakeFiles/a4_handout.dir/a4.cpp.o.requires

CMakeFiles/a4_handout.dir/a4.cpp.o.provides: CMakeFiles/a4_handout.dir/a4.cpp.o.requires
	$(MAKE) -f CMakeFiles/a4_handout.dir/build.make CMakeFiles/a4_handout.dir/a4.cpp.o.provides.build
.PHONY : CMakeFiles/a4_handout.dir/a4.cpp.o.provides

CMakeFiles/a4_handout.dir/a4.cpp.o.provides.build: CMakeFiles/a4_handout.dir/a4.cpp.o


CMakeFiles/a4_handout.dir/main.cpp.o: CMakeFiles/a4_handout.dir/flags.make
CMakeFiles/a4_handout.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/austinmccarson/Downloads/a4-handout/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/a4_handout.dir/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/a4_handout.dir/main.cpp.o -c /Users/austinmccarson/Downloads/a4-handout/main.cpp

CMakeFiles/a4_handout.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/a4_handout.dir/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/austinmccarson/Downloads/a4-handout/main.cpp > CMakeFiles/a4_handout.dir/main.cpp.i

CMakeFiles/a4_handout.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/a4_handout.dir/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/austinmccarson/Downloads/a4-handout/main.cpp -o CMakeFiles/a4_handout.dir/main.cpp.s

CMakeFiles/a4_handout.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/a4_handout.dir/main.cpp.o.requires

CMakeFiles/a4_handout.dir/main.cpp.o.provides: CMakeFiles/a4_handout.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/a4_handout.dir/build.make CMakeFiles/a4_handout.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/a4_handout.dir/main.cpp.o.provides

CMakeFiles/a4_handout.dir/main.cpp.o.provides.build: CMakeFiles/a4_handout.dir/main.cpp.o


# Object files for target a4_handout
a4_handout_OBJECTS = \
"CMakeFiles/a4_handout.dir/a4.cpp.o" \
"CMakeFiles/a4_handout.dir/main.cpp.o"

# External object files for target a4_handout
a4_handout_EXTERNAL_OBJECTS =

a4_handout: CMakeFiles/a4_handout.dir/a4.cpp.o
a4_handout: CMakeFiles/a4_handout.dir/main.cpp.o
a4_handout: CMakeFiles/a4_handout.dir/build.make
a4_handout: CMakeFiles/a4_handout.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/austinmccarson/Downloads/a4-handout/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable a4_handout"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/a4_handout.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/a4_handout.dir/build: a4_handout

.PHONY : CMakeFiles/a4_handout.dir/build

CMakeFiles/a4_handout.dir/requires: CMakeFiles/a4_handout.dir/a4.cpp.o.requires
CMakeFiles/a4_handout.dir/requires: CMakeFiles/a4_handout.dir/main.cpp.o.requires

.PHONY : CMakeFiles/a4_handout.dir/requires

CMakeFiles/a4_handout.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/a4_handout.dir/cmake_clean.cmake
.PHONY : CMakeFiles/a4_handout.dir/clean

CMakeFiles/a4_handout.dir/depend:
	cd /Users/austinmccarson/Downloads/a4-handout/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/austinmccarson/Downloads/a4-handout /Users/austinmccarson/Downloads/a4-handout /Users/austinmccarson/Downloads/a4-handout/cmake-build-debug /Users/austinmccarson/Downloads/a4-handout/cmake-build-debug /Users/austinmccarson/Downloads/a4-handout/cmake-build-debug/CMakeFiles/a4_handout.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/a4_handout.dir/depend
