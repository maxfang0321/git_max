mList = [i for i in range(0,60,5) if i % 5 == 0]
hList = [i for i in range(2,24)]

a = [i for i in range(1,1+1440)]

pre = '012005'
i = 1
for h in hList:
    for m in mList:
        index =''.join([pre,'{:>04d}'.format(i)])
        s_tm = ':'.join(['{:>02d}'.format(h),'{:>02d}'.format(m)])
        e_tm = ':'.join(['{:>02d}'.format(h+2),'{:>02d}'.format(m)])
        print(index,s_tm,e_tm)
        i+=1

'''
fout= open(r'D:\a.txt',mode='w')

step = 5
time_range = 120
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

'''
