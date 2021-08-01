# Import(s)
import matplotlib.pyplot as plt
from math import cos, pi

# Var init and input collection
n = int(input("Enter the initial value (n ∈ ℤ⁺): "))
count = 0
x = [0]
y = []
# Start sequence with n
y.append(n)

# Collatz function
def collatz(z):
	# Unification of 3x+1 for odd and x/2 for even
	return 0.25*(2 + 7*z + (-1)*(2 + 5*z)*cos(pi*z))

# Repeat until the 4,2,1 loop
while y[-1] != 1.0:
	count += 1
	x.append(count)
	y.append(collatz(y[-1]))
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
