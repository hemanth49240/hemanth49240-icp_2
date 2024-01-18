xs = int(input("Enter number of values to be converted\n"))
inches = [float(input("Enter inches value:\n")) for _ in range(xs)]
c = [round(v * 2.54, 2) for v in inches]

print("Inches:", inches)
print("CM:", c)
