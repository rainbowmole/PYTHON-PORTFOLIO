print()
print("-------Translator-------")
print("---English to Tagalog---")
print()
dictionary = {"I love you": "Mahal kita",
              "Thank you": "Salamat",
              "How are you?": "Kamusta ka?",
              "Why": "Bakit",
              "When": "Kailan",
              "Who": "Sino",
              "My Baby": "Princess Jade Elenterio",
              "Angel": "Anghel",
              "Wife": "Princess Jade Elenterio"
              }

for key in dictionary.keys():
        print(key, "->", dictionary[key])