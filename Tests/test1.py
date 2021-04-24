# test Text Files
from collections import Counter
with open("test1.txt", "r") as inputTextFile:
    participants = [line.strip().split() for line in inputTextFile]

name = [participants[i][0] for i in range(len(participants))]
country = [participants[j][1] for j in range(len(participants))]
score = [participants[s][2:] for s in range(len(participants))]

# a) Print a list of the countries the participants came from.
print(f"List of names: {name}")
print(f"List of countries: {country}")

# b) Print the numbers of participants from the individual countries.
print(f"Occurrence of participants: {Counter(country)}")

# c) Print the name of the absolute winner - the competitor who managed to jump the greatest distance.
score_list = []
for i in range(len(score)):
    for j in range(len(score[i])):
        score_list.append(int(score[i][j]))
highest_value = max(score_list)

index_winners = []
for i in range(len(score_list)):
    if score_list[i] == highest_value:
        index_winners.append(int(i//len(score[0])))

print(f"Highest score: {max(score_list)}")
print("Winner(s): ")
if len(index_winners) == 1:
    print(name[index_winners[0]])
else:
    for w in range(len(index_winners)):
        print(name[w])
