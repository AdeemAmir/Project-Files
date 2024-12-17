import os
import json
import re

def generate_data_json(directory):
    # List of valid image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    
    # Prepare a dictionary to store data
    data = {
        "meta": {
            "lgR_images": 0,
            "image_urls": []
        }
    }

    # Get the current script file name
    script_name = os.path.basename(__file__)
    
    # Regex pattern to match 'live{x}.{format}'
    pattern = re.compile(r'^live(\d+)\.(jpg|jpeg|png|gif)$', re.IGNORECASE)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Skip this script file and the data.json file
        if filename == script_name or filename == 'data.json':
            continue
        
        # Check if the filename matches the 'live{x}.{format}' pattern
        match = pattern.match(filename)
        if match:
            # Extract the image number and format from the filename
            image_number = match.group(1)
            image_format = match.group(2).lower()
            # Store only the filename, without the full URL
            image_url = filename
            
            # Add the image URL to the list and increment the count
            data["meta"]["image_urls"].append(image_url)
            data["meta"]["lgR_images"] += 1

    # Create or overwrite the data.json file with the generated data
    with open(os.path.join(directory, 'data.json'), 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"data.json has been created with {data['meta']['lgR_images']} images.")

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Call the function to generate the data.json file
generate_data_json(current_directory)
