import json

average_profit = dict()
profits = dict()
losses = dict()
res = []

with open("text_7.txt", encoding="UTF-8") as f:
    for line in f:
        name, type, revenue, cost = line.split()
        profit = int(revenue) - int(cost)
        if profit >= 0:
            profits[name] = profit
        else:
            losses[name] = profit
average_profit['average_profit'] = sum(profits.values()) / len(profits)
res = [profits, average_profit, losses]

with open("json7.json", "w", encoding="UTF-8") as f:
    json.dump(res, f, indent=4)
