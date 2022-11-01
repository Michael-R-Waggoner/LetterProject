# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

new_letters = []

with open("Input/Names/invited_names.txt", mode="r") as names:
    input = names.readlines()
    strip_names = []
    for name in input:
        new_name = name.strip()
        strip_names.append(new_name)
    with open("Input/Letters/starting_letter.txt", mode="r") as f:
        text = f.read()
        with open("Input/Letters/starting_letter.txt", mode="w") as f:
            for item in strip_names:
                new_letter = text.replace("[name]", f"{item}")
                new_letters.append(new_letter)
            f.write(text)
for int in range(0,8):
    with open(f"Output/ReadyToSend/new_letter{int}.txt", mode="w") as f:
        f.write(new_letters[int])

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
