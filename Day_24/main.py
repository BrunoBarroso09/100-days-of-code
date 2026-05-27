with open("./Name/names.txt") as invited_names:
    names_list = (invited_names.readlines())

with open("./Letter/letter.txt") as file:
    contents = file.read()

    for name in names_list:
        name = name.strip()
        new = contents.replace("[name]", name)
        with open(f"./SendLetter/letter_for_{name}.txt",
                  mode="w") as final_file:
            final_file.write(new)