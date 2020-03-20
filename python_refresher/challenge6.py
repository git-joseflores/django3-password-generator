words = ["PoGo", "Spange", "Lie-Fi"]
definitions = ["Slang for Pokemon Go", "To collect spare change, either from couches, passerbys on the street or any numerous other ways and means",
               "When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for x in range(3):
    cooldictionary[words[x]] = definitions[x]

for definition_name, definition in cooldictionary.items():
    print(definition_name, definition)
print(cooldictionary)
