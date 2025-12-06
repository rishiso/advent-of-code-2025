import sys

lines = sys.stdin.readlines()
print()

sol = 0
for bank in lines:
    first = 0
    second = 0
    best = 0
    for battery in bank.strip():
        battery = int(battery)

        if second < battery:
            second = battery

        best = max(best, 10 * first + second)

        if first < second:
            first, second = second, 0

    sol += best

print(sol)