print('enter the name of the file that contains the logs')
files = input()
print('Enter the sensibel email that you want to delete from the logs')
search_text = input()
replace_text = "anonymous@appsmith.com"
with open(files) as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
    with open(files, "w") as file:
     file.write(data)
    print("Your sensitive email was replaced in the entire log by anonymous", data)
