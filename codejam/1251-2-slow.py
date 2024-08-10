from itertools import permutations

MAX_NUM = 10 ** 9

def find_min_max_time(N, D):
    cities = list(range(1, N))  # 도시 2번부터 N번까지
    min_time = MAX_NUM
    max_time = 0
    
    # 도시 순열
    for city_perm in permutations(cities):
        # 교통수단 순열
        for trans_perm in permutations(range(N)):
            is_possible = True
            # 도시 1에서 출발하여 city_perm 순으로 방문하고 다시 1로 돌아오는 경우의 시간 계산
            time = 0
            curr_city = 0  # 항상 1번 도시에서 시작
            for i in range(N-1):
                next_city = city_perm[i]
                transport = trans_perm[i]
                # 교통수단이 없는 경우
                if D[transport][curr_city][next_city] == 0:
                    is_possible = False
                    break
                time += D[transport][curr_city][next_city]
                curr_city = next_city
            if not is_possible:
                continue
            # 마지막 도시에서 1번 도시로 돌아오는 시간
            if D[trans_perm[-1]][curr_city][0] == 0: # 교통수단이 없는 경우
                continue 
            time += D[trans_perm[-1]][curr_city][0]
            
            # 최소 및 최대 시간 갱신
            min_time = min(min_time, time)
            max_time = max(max_time, time)
    
    return min_time, max_time

t = int(input())
for _ in range(t):
    n = int(input())
    d = []
    for _ in range(n):
        transport_times = []
        for _ in range(n):
            transport_times.append(list(map(int, input().split())))
        d.append(transport_times)

    min_time, max_time = find_min_max_time(n, d)
    if min_time == MAX_NUM:
        min_time = 0
    print(min_time, max_time)