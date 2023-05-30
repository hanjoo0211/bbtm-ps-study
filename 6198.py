n = int(input())
benchmark = 0
buildings = []
for _ in range(n):
    height = int(input())
    while buildings:
        building = buildings.pop()
        if building > height:
            buildings.append(building)
            break
    benchmark += len(buildings)
    buildings.append(height)
print(benchmark)