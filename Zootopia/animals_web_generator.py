import json
import os

def main():
    json_file_path = os.path.join('Zootopia', 'animals_data.json')
    html_file_path = os.path.join('Zootopia', 'animals_template.html')
    animals_data = load_data(json_file_path)
    dog_string = string_animals(animals_data)
    html_template = load_html(html_file_path)
    new_html_template = html_template.replace("__REPLACE_ANIMALS_INFO__",dog_string)
    new_html_file_path = os.path.join('Zootopia', 'new_animals_template.html')
    write_html(new_html_template,new_html_file_path)
    


def load_data(file_path):
    ###loading json file from parameter filepath and returing dictionary###
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError as e:
        print(e) 

def string_animals(data):
    ###Creating a string from Dict parameter for animals returning string outpu###
    output =""
    try:
        for animal in data:
            name_dog = animal["name"]
            diet_dog = animal["characteristics"]["diet"]
            location_dog = animal["locations"][0]
            
            if "characteristics" in animal and "type" in animal["characteristics"]:
                type_dog = animal["characteristics"]["type"]
            else:
                type_dog = ""
            output += '<li class="cards__item">'
            output += f"Name: {name_dog}\n"
            output += f"Diet: {diet_dog}\n"
            output += f"Location: {location_dog}\n"
            if len(type_dog) > 0:
                output += f"Type: {type_dog}\n"
            output += '</li>'  
        return output 
    except Exception as e:
        print(e)           


def load_html(file_path):
    ###Loading html template as parameter and returning it as string###
    try:
        with open(file_path, "r") as dog_data:
            template_content = dog_data.read()
        return template_content
    except FileNotFoundError as e:
        print(e)


def write_html(template,new_html_file_path):
    try:
        with open(new_html_file_path,"w", encoding="UTF8") as html_file:
            html_file.write(template)
    except IOError as e:
        print(e)        



if __name__ == "__main__":
    main()
