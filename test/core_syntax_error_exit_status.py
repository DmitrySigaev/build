#!/usr/bin/python

# Copyright (C) Mateusz Loskot 2020.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

# Test that Jam syntax error results in non-zero exit status

import BoostBuild

# Create a temporary working directory.
t = BoostBuild.Tester()

# Create the needed files.
t.write("jamroot.jam", """
exe hello : hello.cpp

""")

t.run_build_system(status=1)

t.cleanup()
