#!/usr/bin/env python
#
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

"""
Verify that $CPPDEFINES does not contain 'canceled' macro
"""

import TestSCons

test = TestSCons.TestSCons()

test.write('SConstruct', """\
env = Environment()
env.MergeFlags("-DSTILLHERE")
print(env["CPPDEFINES"])
env.MergeFlags("-USTILLHERE")
print(env["CPPDEFINES"])
env.MergeFlags("-DCANCELED -UCANCELED")
print(env["CPPDEFINES"])
env.MergeFlags("-DCANCELED -U CANCELED")
print(env["CPPDEFINES"])
""")

expect = test.wrap_stdout(build_str="scons: `.' is up to date.\n",
                          read_str="""\
['STILLHERE']
['STILLHERE']
['STILLHERE']
['STILLHERE']
""")

test.run(arguments=".", stdout=expect)

test.pass_test()

