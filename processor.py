import matplotlib.pyplot as plt

filename = input("Enter the filename: ")
substring = "time="

lines = []

with open(filename, "r") as file:
    for line in file:
        line = line.replace(substring, "")
        line = line.rstrip() # remove the newline character from the end of the line
        if line == "---":
            lines.append(lines[-1])
        else:
            lines.append(float(line))

time = [i/2 for i in range(len(lines))]

plt.plot(time, lines)
plt.xlabel("Time (seconds)")
plt.ylabel("Value")
plt.title("Line Plot")
plt.show()


