import json
import os



json_file_path = os.path.join('Zootopia', 'animals_data.json')


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data(json_file_path)



def print_animals(data):
    for animal in data:
        name_dog = animal["name"]
        diet_dog = animal["characteristics"]["diet"]
        location_dog = animal["locations"][0]
        
        if "characteristics" in animal and "type" in animal["characteristics"]:
            type_dog = animal["characteristics"]["type"]
        else:
            type_dog = ""
        
        print(f"Name: {name_dog}")
        print(f"Diet: {diet_dog}")
        print(f"Location: {location_dog}")
        if len(type_dog) >0:
            print(f"Type: {type_dog}")
        print()

print_animals(animals_data)