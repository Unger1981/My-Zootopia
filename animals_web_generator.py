import os
from data_fetcher import fetch_data


def main():
    while True:
        try:
            animal_name = input("Please enter an animal: ")
            if len(animal_name) >= 3:
                break
            else:
                 raise Exception("Please enter at least 3 characters")
        except Exception as e:
            print(e)
    html_file_path = 'animals_template.html'
    animals_data = load_data(animal_name)
    print(animals_data)
    dog_string = serialize_animals(animals_data)
    html_template = load_html(html_file_path)
    new_html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", dog_string)
    new_html_file_path = 'new_animals_template.html'
    write_html(new_html_template, new_html_file_path)


def load_data(animal_name):
    """
    Load animal data for the specified animal from ninja api.
    
    Parameter: animal_name as string

    Return: animal data as list with dictionaries or None if failed to fetch
    """
    try:
        animal_data = fetch_data(animal_name)
        return animal_data  # Ensure data is returned
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None  # Return None if data cannot be fetched


def serialize_animals(data):
    """
    Create a string representation of animals for HTML by fetched data
    
    Prameters: Data received from ninja api list of dictionaries (data)

    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    
    """
    output = ""
    if data is None or len(data) == 0:
            print("No Data")
            output += '<li class="cards__item">'
            output += f'<div class="card__title">No Data</div>'
            
    else:
            for animal in data:
                name_dog = animal["name"]
                diet_dog = animal["characteristics"]["diet"]
                location_dog = animal["locations"][0]
                lifespan_dog = animal["characteristics"]["lifespan"]
                type_dog = animal["characteristics"].get("type", "")

                output += '<li class="cards__item">'
                output += f'<div class="card__title">{name_dog}</div>'
                output += '<p class="card__text">'
                output += f'<strong>Location:</strong> {location_dog}<br/>'
                if type_dog:
                    output += f'<strong>Type:</strong> {type_dog}<br/>'
                output += f'<strong>Diet:</strong> {diet_dog}<br/>'
                output += f'<strong>Lifespan:</strong> {lifespan_dog}<br/>'
                output += '</p></li>'
                
    return output
    

def load_html(file_path):
    """
    Load HTML template from the specified file path.
    
    Parameter: filepath as string

    Returns: HTML as string
    """
    try:
        with open(file_path, "r") as dog_data:
            template_content = dog_data.read()
        return template_content
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None  # Return None if file not found
    except IOError as e:
        print(f"IO Error: {e}")
        return None  # Return None for IO errors


def write_html(template, new_html_file_path):
    """
    Write the HTML template to a new file.
    
    Parameter: html template as string (template)
               filepath for storage as string (new_html_file_path)
    """
    try:
        with open(new_html_file_path, "w", encoding="UTF8") as html_file:
            html_file.write(template)
    except IOError as e:
        print(f"Error writing HTML file: {e}")


if __name__ == "__main__":
    main()
