# Enter your code here. Read input from STDIN. Print output to STDOUT
actual=list(map(int, input().split()))
expected=list(map(int, input().split()))
actual_date=actual[0]
actual_month=actual[1]
actual_year=actual[2]
expected_date=expected[0]
expected_month=expected[1]
expected_year=expected[2]
if actual_year<expected_year:
    print('0')
elif actual_year==expected_year:
    if actual_month<expected_month:
        print('0')
    elif actual_month==expected_month:
        if actual_date<=expected_date:
            print('0')
        else:
            fine=(actual_date-expected_date)*15
            print(fine)
    else:
        fine=(actual_month-expected_month)*500
        print(fine)
else:
    print('10000')   