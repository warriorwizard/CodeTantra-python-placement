import statistics
n=int(input('Enter size of list: '))
b=[int(input('Enter integer value: ')) for x in range(n)]
print('Mean of list:',statistics.mean(b))
print('Median of list:',statistics.median(b))
print('Mode of list:',statistics.mode(b))
print('Standard deviation of list:',statistics.stdev(b))
print('Variance of list:',statistics.variance(b))