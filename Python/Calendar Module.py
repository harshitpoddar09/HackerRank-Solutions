# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date=list(map(int, input().split()))
day_num=calendar.weekday(date[2],date[0],date[1])
if day_num==0:
    print('MONDAY')
elif day_num==1:
    print('TUESDAY')
elif day_num==2:
    print('WEDNESDAY')
elif day_num==3:
    print('THURSDAY')
elif day_num==4:
    print('FRIDAY')
elif day_num==5:
    print('SATURDAY')
elif day_num==6:
    print('SUNDAY')
