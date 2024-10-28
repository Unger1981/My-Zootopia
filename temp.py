import json
import os
from data_fetcher import fetch_data


def main():
    animal_name = input("Please enter an animal ")
    current_directory = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(current_directory, "animals_template.html")
    animals_data = load_data(animal_name)
    print(animals_data)
    dog_string = serialize_animals(animals_data)
    html_template = load_html(html_file_path)
    print(html_template)
    new_html_template = html_template.replace("__REPLACE_ANIMALS_INFO__",dog_string)
    new_html_file_path = os.path.join('Zootopia', 'new_animals_template.html')
    write_html(new_html_template,new_html_file_path)
    


def load_data(animal_name):
    ###loading json file from parameter filepath and returing dictionary###
    try:
        animal_data = fetch_data(animal_name)
        return animal_data
    except FileNotFoundError as e:
        print(e)
    
    return None

def serialize_animals(data):
    ###Creating a string from Dict parameter for animals returning string outpu###
    output =""
    try:
        for animal in data:
            name_dog = animal["name"]
            diet_dog = animal["characteristics"]["diet"]
            location_dog = animal["locations"][0]
            lifespan_dog = animal["characteristics"]["lifespan"]
            
            if "characteristics" in animal and "type" in animal["characteristics"]:
                type_dog = animal["characteristics"]["type"]
            else:
                type_dog = ""
            output += '<li class="cards__item">'
            output += f'<div class="card__title">{name_dog}</div>'
            output += '<p class="card__text">'
            output += f'<strong>Location:</strong> {location_dog}<br/>'
            if len(type_dog) > 0:
                output+=f'<strong>Type:</strong> {type_dog}<br/>'
            output += f'<strong>Diet:</strong> {diet_dog}<br/>'
            output += f'<strong>Lifespan:</strong> {lifespan_dog}<br/>'
            output += ' </p></li>'  
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
