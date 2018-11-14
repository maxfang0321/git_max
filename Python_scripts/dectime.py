a = [i for i in range(1,1+1440)]

fout= open(r'D:\a.txt',mode='w')

step = 5
time_range = 30
i = 1

start = 0
end = start+time_range

while end <= 1440:
    for j in a[start:start+time_range]:
        index = ''.join(['0001','{:>04d}'.format(j)])
        dectime_index = ''.join(['{:>04d}'.format(time_range),'{:>02d}'.format(step),'{:>04d}'.format(i)])
        fout.write(','.join([index,dectime_index]))
        fout.write("\n")
    start+=step
    end+=step
    i+=1
    
fout.close()
