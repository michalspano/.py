print("Test 2")

with open("test2.txt", "r") as inputTextFile:
    load_data = [line.strip() for line in inputTextFile]

slovak_data, english_data = [], []
i = 0
while i < len(load_data):
    if i % 2 == 0:
        english_data.append(load_data[i])
    else:
        slovak_data.append(load_data[i])
    i += 1

language_option = input("Language: SK/EN: ")

j = -1
correct_count, wrong_count = int(), int()
if language_option == "SK":
    while len(english_data) > 0:
        print("*********")
        output = ", ".join(slovak_data)
        print(f"SK: {output}")
        print(f"Remaining answers: {len(slovak_data)}")
        j += 1
        if j >= len(english_data):
            j = 0
        answer = input(f"Enter | {slovak_data[j]} | translation in English: ")
        if answer == english_data[j]:
            if answer in english_data:
                index_val = english_data.index(answer)
                english_data.remove(answer)
                slovak_data.pop(index_val)
                j -= 1
                correct_count += 1
        else:
            wrong_count += 1
else:
    while len(slovak_data) > 0:
        print("*********")
        output = ", ".join(english_data)
        print(f"SK: {output}")
        print(f"Remaining answers: {len(english_data)}")
        j += 1
        if j >= len(slovak_data):
            j = 0
        answer = input(f"Enter | {english_data[j]} | translation in Slovak: ")
        if answer == slovak_data[j]:
            if answer in slovak_data:
                index_val = slovak_data.index(answer)
                slovak_data.remove(answer)
                english_data.pop(index_val)
                j -= 1
                correct_count += 1
        else:
            wrong_count += 1

print("\n" + "Results: ")
print(f"Correct answers: {correct_count}")
print(f"Wrong answers: {wrong_count}")
