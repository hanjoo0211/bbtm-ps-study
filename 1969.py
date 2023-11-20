n, m = map(int, input().split())
dnas = [input() for _ in range(n)]

min_hd = 0
min_dna = ""
for i in range(m):
    nuc = {"A": 0, "C": 0, "G": 0, "T": 0}
    for dna in dnas:
        nuc[dna[i]] += 1
    max_count = 0
    for k, v in nuc.items():
        if v > max_count:
            max_count = v
            max_nuc = k
    min_dna += max_nuc
    min_hd += n - max_count
print(min_dna)
print(min_hd)
