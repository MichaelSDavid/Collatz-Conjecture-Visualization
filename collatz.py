# Import(s)
import matplotlib.pyplot as plt

# Var init and input collection
n = int(input("Enter the initial value (n ∈ ℤ⁺): "))
count = 0
x = [0]
y = []
# Start sequence with n
y.append(n)

# Check conditions until the final number is 1
while y[-1] != 1.0:
	count += 1
	x.append(count)
	# Rule for odd numbers (3x+1)
	if y[-1] % 2 != 0:
		y.append((3 * (y[-1])) + 1)
	# Rule for even numbers (x/2)
	elif y[-1] % 2 == 0:
		y.append(y[-1] / 2)
	print(y[-1], end="   ")

# Zip coords
for i in list(zip(x, y)):
	plt.text(i[0], i[1], f"({i[0]} , {i[1]})")

# Output to graph
plt.xlabel("Iterations")
plt.ylabel("Number (n)")
plt.title(f"Collatz Conjecture for n = {n}")
plt.plot(x, y, "bo-")
plt.show()
