for i in range(100000):
    for j in range(10):
        print(i * 10 + j, " ", end="")
    if (i + 1) % 10 == 0:
        print("\n")
    else:
        print(" ", end="")
print(1000000)

# Add a final newline for better formatting
print()