nh, nm, ns = map(int, input().split(":"))
sh, sm, ss = map(int, input().split(":"))
nt = nh * 3600 + nm * 60 + ns
st = sh * 3600 + sm * 60 + ss
if nt > st:
    st += 24 * 3600
t = st - nt

h = t // 3600
t %= 3600
m = t // 60
t %= 60
h = str(h).zfill(2)
m = str(m).zfill(2)
t = str(t).zfill(2)
print(f"{h}:{m}:{t}")