print("Test 3\n")

with open("test3.txt", "r") as inputTextFile:
    data = [line.strip().split() for line in inputTextFile]

# 1)
print(f"Number of competitors: {len(data)}\n")
# 2)
for i in range(len(data)):
    print(f"Athlete {i + 1}: {data[i][0]}'s time: {data[i][1]}s")
# 3)
times = [int(data[i][1]) for i in range(len(data))]
best_score = min(times)
index = times.index(best_score)
print(f"\n{data[index][0]} reached the best score: {best_score}s")

# 4)
output_times = []
for t in times:
    output_times.append((t//60, t % 60))
output_time = output_times[index]
print(f"The best time (in min(s)): {output_time[0]}min, {output_time[1]}s")
