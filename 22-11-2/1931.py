n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

sortedMeetings = sorted(meetings, key=lambda x: [x[1], x[0]])

realMeetings = [sortedMeetings[0]]
for s, e in sortedMeetings[1:]:
    rs, re = realMeetings[-1]
    if s >= re:
        realMeetings.append([s, e])

print(len(realMeetings))