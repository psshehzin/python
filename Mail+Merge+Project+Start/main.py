with open("./Input/Letters/starting_letter.txt") as file1:
    letter=file1.read()
with open("./Input/Names/invited_names.txt") as file2:
    names=file2.readlines()
for i in range(len(names)):
    names[i]=names[i].strip()
for name in names:
    letterto=letter.replace("[name]",name)
    letterto=letterto.replace("Angela","Shehzin")
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt",mode="w") as tfile:
        tfile.write(letterto)
