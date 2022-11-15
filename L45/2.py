my_set = {(u,t,s) for s in range(1,30) for t in range(s,30+1)  for u in range(1,30+1) if s**2+t**2==u**2 }
print(sorted((my_set)))