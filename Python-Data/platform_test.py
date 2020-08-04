
import platform

# x = platform.system()
# print(x)
# AttributeError: module 'platform' has no attribute 'system'

print('\nuname =\n', platform.uname())

print('\nversion =\n', platform.version())

print('\nsystem =\n', platform.system())

"""

uname =
 uname_result(system='Darwin', node='xgqfrms-mbp.local', release='19.5.0', version='Darwin Kernel Version 19.5.0: Tue May 26 20:41:44 PDT 2020; root:xnu-6153.121.2~2/RELEASE_X86_64', machine='x86_64', processor='i386')

version =
 Darwin Kernel Version 19.5.0: Tue May 26 20:41:44 PDT 2020; root:xnu-6153.121.2~2/RELEASE_X86_64

system =
 Darwin

"""

"""
# module name conflict bug

# print(platform)
# <module 'platform' from '/Users/xgqfrms-mbp/Documents/GitHub/Python/Python-Data/platform.py'>

# <module 'platform' from '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/platform.py'>

"""
