import math
# import sys
# input = []
# while True:
#     line = sys.stdin.readline().rstrip('\n')
#     if line == 'quit':
#         break
#     else:
#         input.append(line)


with open("input1.txt") as f:
    current_total = 50
    overall_total = 0
    for line in f:
        figure = line.strip()
        turn_amount = int(figure[1: ])
        direction = figure[0]

        if direction == 'R':
            current_total += turn_amount
            if current_total > 99:
                overall_total += math.floor(current_total / 100)
                
        if direction == 'L':
            if current_total == 0:
                overall_total -= 1
            current_total -= turn_amount
            if current_total < 1:
                overall_total += 1 + (math.floor(abs(current_total) / 100))

        current_total %= 100
        print(figure, current_total, overall_total)

    print(overall_total)
