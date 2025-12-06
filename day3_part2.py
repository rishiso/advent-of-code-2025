import sys

lines = sys.stdin.readlines()
print()

sol = 0
for bank in lines:
    curr = []
    best = 0
    for battery in bank.strip():
        battery = int(battery)

        if len(curr) < 12:
            curr.append(battery)
        elif curr[-1] < battery:
            curr[-1] = battery

        if len(curr) < 12:
            continue

        total = 0
        mult = 1
        for i in reversed(curr):
            total += mult * i
            mult *= 10

        best = max(best, total)

        for i in range(11):
            if curr[i] < curr[i + 1]:
                curr.pop(i)
                break

    sol += best

print(sol)