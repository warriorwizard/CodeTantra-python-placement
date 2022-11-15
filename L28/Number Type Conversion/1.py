# Type Conversion Example
a = '0111110'
i=int(a,2)
d=type(i)
print(f"converting to int: {i} ,data type: {d}")
f=float(i)
d=type(f)
print(f"converting to float: {f} ,data type: {d}")
c=complex(i)
d=type(c)
print(f"converting to complex: {c} ,data type: {d}")