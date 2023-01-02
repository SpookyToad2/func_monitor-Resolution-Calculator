def resolution_vertical(vertical):
 	return (vertical * 0.0009765625)

def resolution_horizontal(horizontal):
 	return (horizontal * 0.0009765625)

print("Welcome to Monitor Resolution Calculator!\n")
print("Created by: SpookyToad#5281 or https://steamcommunity.com/profiles/76561198262348311\n")
print("Do not forget to align the monitor screen texture to a corner for proper displaying\n")
print("Enter Vertical Units")

vertical = float(input(""))

print("Enter Horizontal Units")

horizontal = float(input(""))

print("\n")

print("Horizontal Resolution(X): ")
print(resolution_vertical(horizontal))

print("Vertical Resolution(Y): ")
print(resolution_vertical(vertical))

while True:
	if input("").strip().upper() != 'banana':
		break