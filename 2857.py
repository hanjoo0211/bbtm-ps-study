fbi_agent = []
for i in range(1, 6):
    agent = input()
    if "FBI" in agent:
        fbi_agent.append(i)
print(*fbi_agent) if fbi_agent else print("HE GOT AWAY!")
