# Create a program that will:

with open("input_weather.txt", "r") as inputTextFile:
    data = [line.strip().split() for line in inputTextFile]

# a. determine the number of measurements,
number_measurements = len(data)
print(f"The number of measurements was: {number_measurements}\n")

# b. print only the temperatures,
j = 0
temperatures = [data[i][3].replace(",", ".") for i in range(len(data))]
while j < len(temperatures):
    print(f"{j + 1}: {temperatures[j]}")
    j += 1

# c. determine and print the highest recorded temperature,
temperatures = [float(temperatures[t]) for t in range(len(temperatures))]
highest_value = max(temperatures)
print(f"\nThe highest temperature was: {highest_value}")

# d. determine and print the code of the station where the highest temperature was recorded,
index = temperatures.index(highest_value)
stations = [data[i][0] for i in range(len(data))]
print(f"\nThe station with the temperature was: {stations[index]}")

# e. calculate and print the average temperature across all the stations.
_sum = float()
for i in range(len(temperatures)):
    _sum += temperatures[i]

average_t = _sum / number_measurements
print(f"\nThe average temperature was: {round(average_t, 2)}")
