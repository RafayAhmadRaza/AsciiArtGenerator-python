from PIL import Image
import numpy as np
from pathlib import Path
import random
ascii_chars =  ['#', '@', '%', '&', 'M', 'W', 
                '$', '8', 'B', 'H', 'Q', 'E', 'Z', 'N', 'A', 'V', 'X', 
                'U', '0', 'O', 'C', '7', '1', '3', '2', 'r', 'c', 'x', 'o', 'a', 
                's', 'n', 'u', '!', '-', '~', ';', ':', ',', '"', "'", '.']

char_to_rgb = {
    '#': (0, 0, 0),      # Black
    '@': (50, 50, 50),   # Dark Gray
    '%': (100, 100, 100), # Medium Gray
    '&': (150, 150, 150), # Light Gray
    'M': (200, 200, 200), # Very Light Gray
    'W': (255, 255, 255), # White
    '$': (255, 0, 0),    # Red
    '8': (0, 255, 0),    # Green
    'B': (0, 0, 255),    # Blue
    'H': (255, 255, 0),  # Yellow
    'Q': (255, 0, 255),  # Magenta
    'E': (0, 255, 255),  # Cyan
    'Z': (128, 0, 0),    # Dark Red
    'N': (0, 128, 0),    # Dark Green
    'A': (0, 0, 128),    # Dark Blue
    'V': (128, 128, 0),  # Olive
    'X': (128, 0, 128),  # Purple
    'U': (0, 128, 128),  # Teal
    '0': (192, 192, 192),# Silver
    'O': (128, 128, 128),# Gray
    'C': (255, 165, 0),  # Orange
    '7': (255, 105, 180),# Hot Pink
    '1': (255, 69, 0),   # Red-Orange
    '3': (102, 205, 170),# Medium Aquamarine
    '2': (50, 205, 50),  # Lime Green
    'r': (139, 69, 19),  # Saddle Brown
    'c': (0, 255, 255),  # Cyan (Duplicate)
    'x': (139, 0, 139),  # Dark Violet
    'o': (255, 140, 0),  # Dark Orange
    'a': (255, 20, 147), # Deep Pink
    's': (32, 178, 170), # Light Sea Green
    'n': (0, 128, 128),  # Teal (Duplicate)
    'u': (210, 105, 30), # Chocolate
    '!': (255, 192, 203),# Pink
    '-': (211, 211, 211),# Light Gray (Duplicate)
    '~': (240, 248, 255),# Alice Blue
    ';': (255, 228, 225),# Misty Rose
    ':': (255, 240, 245),# Lavender Blush
    ',': (255, 239, 213),# Papaya Whip
    '"': (255, 250, 205),# Lemon Chiffon
    "'": (255, 250, 250),# Snow
    '.': (240, 255, 240) # Honeydew
}


# Define the range of possible colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Update the function to use random colors
def ascii_to_color_image(ascii_art_path, output_path, image_width):
    # Read ASCII art from file
    with open(ascii_art_path, 'r') as file:
        lines = file.readlines()
    
    # Strip extra whitespace and calculate image dimensions
    lines = [line.rstrip() for line in lines]
    image_height = len(lines)
    max_line_length = max(len(line) for line in lines)
    image_width = min(image_width, max_line_length)
    
    # Create a blank image
    image = Image.new('RGB', (image_width, image_height))
    
    # Create pixel data array
    pixels = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    
    # Create a dictionary to map ASCII characters to random colors
    char_to_rgb = {}
    for char in set("".join(lines)):
        char_to_rgb[char] = random_color()
    
    # Map ASCII characters to RGB colors
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if x < image_width:
                pixels[y, x] = char_to_rgb.get(char, (255, 255, 255))  # Default to white if character not found

    # Convert array to image
    image = Image.fromarray(pixels)
    
    # Save the image
    image.save(output_path)

# Example usage
path_of_ascii = Path('sameAsciiArt.txt')
ascii_to_color_image(path_of_ascii, 'convertedImageArt.png', 500)
