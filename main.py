def getCalories():
    with open("input.txt") as file:
        lines = file.readlines()

    elfCalories = [0]
    index = 0

    # Loops through each input and writes
    for line in lines:
        if line == "\n":
            index += 1
            elfCalories.append(0)
        else:
            elfCalories[index] += int(line.strip("\n"))

    return elfCalories


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calories = getCalories()
    sorted_calories = sorted(calories)

    print(f"The maximum calories one elf is holding is: {sorted_calories[-1]}")
    print(f"The total number of calories that the top 3 elves are carrying is: "
          f"{sorted_calories[-1] + sorted_calories[-2] + sorted_calories[-3]}")

