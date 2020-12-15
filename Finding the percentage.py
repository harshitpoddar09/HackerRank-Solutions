if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        if i==query_name:
            j=student_marks[i]
    sum=0
    for k in j:
        sum=sum+k
        avg=sum/3
    print("{:.2f}".format(avg))