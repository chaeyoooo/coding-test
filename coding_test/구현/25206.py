grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
totalscore = 0
total = 0

for _ in range(20):
    a,b,c = map(str, input().split())
    b = float(b)

    #p건너 뛰기
    if c == "P":
        continue

    totalscore += b * grade.get(c,0)
    total += b

    answer = totalscore/total

print(f"{answer:.6f}")
    