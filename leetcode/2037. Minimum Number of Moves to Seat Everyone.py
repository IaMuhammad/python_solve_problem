def minMovesToSeat(seats, students):
    print(seats)
    s = 0
    i = 0
    print(seats)
    for k in seats:
        s += abs(k - students[i])
        i += 1
    return s
s1 = [12,59,24]
s2 = [15,52,64]
print(minMovesToSeat(s1,s2))