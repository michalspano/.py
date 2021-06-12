from collections import Counter
round_n = int(input("Round up [decimal places]: "))


def load_data(file):
    data = []
    with open(file, "r") as input_data:
        for line in input_data:
            data.append(int(line.strip()))
    return data


data_set = load_data("data_set1.txt")


def arithmetic_mean(arr):
    x_a = int()
    for i in range(len(arr)):
        x_a += arr[i]
    return round(x_a / len(arr), round_n)


X_a = arithmetic_mean(data_set)
print("Xa:", X_a)


def geometric_mean(arr):
    x_g = arr[0]
    for i in range(1, len(arr)):
        x_g *= arr[i]
    return round(x_g ** (len(arr) ** - 1), round_n)


X_g = geometric_mean(data_set)
print("Xg: ", X_g)


def harmonic_mean(arr):
    x_h = float()
    for i in range(len(arr)):
        x_h += (1 / arr[i])
    return round(len(arr) / x_h, round_n)


X_h = harmonic_mean(data_set)
print("Xh: ", X_h)


def mode(arr):
    frequency = []
    for key, value in Counter(arr).items():
        value_set = (value, key)
        frequency.append(value_set)

    max_frequency = max(frequency)
    return max_frequency[1]


mod_x = mode(data_set)
print("mod(X):", mod_x)


def median(arr):
    r_arr = len(arr)
    ordered_arr = sorted(arr)
    ID = int(r_arr / 2)

    if r_arr % 2 == 0:
        return round((ordered_arr[ID - 1] + ordered_arr[ID]) / 2, round_n)
    else:
        return round(ID)


med_x = median(data_set)
print("med(X): ", med_x)


def range_function(arr):
    return min(arr), max(arr)


r = range_function(data_set)
print(f"<{r[0]};{r[1]}>")


def variance_function(arr, avg):
    v_sum = float()
    for i in range(len(arr)):
        v_sum += (arr[i] - avg) ** 2
    return round(v_sum / len(arr), round_n)


variance = variance_function(data_set, X_a)
print("v: ", variance)


def standard_deviation(v):
    return round(v ** (1 / 2), round_n)


s = standard_deviation(variance)
print("s:", s)
