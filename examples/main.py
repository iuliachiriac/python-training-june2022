# import pymodule  # import module
#
# print(pymodule.X, pymodule.get_long_strings('aa', 'aaaa', n=3))


# import pymodule as mod  # import module as alias
#
# print(mod.X, mod.get_long_strings('aa', 'aaaa', n=3))


# from pymodule import get_long_strings  # import specific names from module
#
# print(get_long_strings('aa', 'aaaa', n=3))


import sys  # import from standard library
from pprint import pprint  # import from standard library

import ipdb  # import from 3rd party packages (unused)

from pymodule import X as pym_X  # import specific names under alias from module
from pypackage import other_module
# import pypackage

print(pym_X, other_module.name)
pprint(sys.path)

