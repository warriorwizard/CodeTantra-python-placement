from string import ascii_uppercase
from collections import OrderedDict
a={(i,chr(i)) for i in range(65,91)}
b={(chr(i),i) for i in range(65,91)}
print(sorted(a))
print(sorted(b))