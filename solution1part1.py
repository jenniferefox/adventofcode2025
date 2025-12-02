with open("input1.txt") as f:
    current_total = 50
    overall_total = 0
    for line in f:
        figure = line.strip()
        if figure[0] == 'R':
            current_total += int(figure[1: ])
        if figure[0] == 'L':
            current_total -= int(figure[1: ])
        if current_total % 100 == 0:
            overall_total += 1

    print(overall_total)
