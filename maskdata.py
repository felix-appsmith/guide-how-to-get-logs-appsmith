import scrubadub
print('Enter the name of the file that contains the logs.')
files = input()
with open(files) as file:
    data = file.read()
    newdata = scrubadub.clean(data)
    with open(files, "w") as file:
        print(data)
        file.write(newdata)
        print("Your sensitive data was replaced", newdata)
