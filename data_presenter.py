import matplotlib.pyplot as plt


cupcakes = open("CupcakeInvoices.csv")
total_cost = 0.00
total_chocolate = 0.00
total_vanilla = 0.00
total_strawberry = 0.00

for line in cupcakes:
    line = line.rstrip("\n").split(",")
    print(line[2])
    total = round((int(line[3]) * float(line[4])),2)
    print("Total = $"+ str(total))
    total_cost += total
    if line[2] == "Chocolate":
        total_chocolate += total
    elif line[2] == "Vanilla":
        total_vanilla += total
    elif line[2] == "Strawberry":
        total_strawberry += total


print("Total cost = $" + str(round(total_cost, 2)))

print(total_chocolate, total_vanilla, total_strawberry)

flavors = ["Chocolate", "Vanilla", "Strawberry"]
income = [total_chocolate, total_vanilla, total_strawberry]

ax = plt.axes()
ax.set_facecolor("#030f29")
plt.bar(flavors, income, color=["#422901", "#edeaab", "#fa78e4"], edgecolor="white")
plt.grid(color="#143d96", linestyle="--", linewidth=1, axis="y")
plt.xlabel("Flavors")
plt.ylabel("Income")
plt.title("Ice Cream Ception")
plt.show()

cupcakes.close()