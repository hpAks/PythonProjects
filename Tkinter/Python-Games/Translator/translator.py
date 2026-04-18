from translate import Translator


language = []
with open("language.txt",mode="r") as file:
    content = file.read()
    language = str(content).split("\n")


cont = True
while cont:
    print(f"Available languages:\n")
    for option in language:
        print(option)
    select = input("select language code you want to translate to ( or q to quit): ")
    if select == 'q':
        break
    for lang in language:
        if lang.split(":")[1].strip() == select:
            selected_lang = lang.split(":")[0]
            text = input("Enter here: ")
            translation = Translator(from_lang="en", to_lang=select).translate(text)
            print(f"After translating {selected_lang} : {translation}")
            print("*******************************************************")




