import os
import json

def generate_index():
    base_url = "https://raw.githubusercontent.com/jqms/RandomSkinsAPI/main/Skins/"
    skins_dir = "Skins"
    
    if not os.path.exists(skins_dir):
        print("Skins directory not found")
        return
    
    image_files = []
    for file in os.listdir(skins_dir):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(base_url + file)
    
    index = {"skins": image_files}
    
    with open('index.json', 'w') as f:
        json.dump(index, f, indent=2)
    
    print(f"Generated index.json with {len(image_files)} skin URLs")

if __name__ == "__main__":
    generate_index()
