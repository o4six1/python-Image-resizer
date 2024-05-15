"""."""
import os
from PIL import Image

def resize_images(folder_path, max_size):
    """
    This function resizes all images in a folder to a maximum size while maintaining aspect ratio.

    Args:
        folder_path: The path to the folder containing the images.
        max_size: The maximum dimension (width or height) for the resized images.
    """
    for filename in os.listdir(folder_path):
        # Get the full path of the image
        image_path = os.path.join(folder_path, filename)

        # Check if it's an image file
        if os.path.isfile(image_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # Open the image
                img = Image.open(image_path)

                # Get original dimensions
                width, height = img.size

                # Maintain aspect ratio
                if width > height:
                    # Resize based on width
                    new_width = max_size
                    new_height = int(height * (max_size / width))
                else:
                    # Resize based on height
                    new_height = max_size
                    new_width = int(width * (max_size / height))

                # Resize the image
                resized_img = img.resize((new_width, new_height), Image.Resampling.BICUBIC)

                # Save the resized image with the same filename
                resized_img.save(image_path)
                print(f"Resized {filename} to maximum dimension {max_size}")
            except OSError as e:
                print(f"Error resizing {filename}: {e}")

# Get user input for maximum size
while True:
    try:
        user_size = int(input("Enter the maximum size (width or height) for resized images: "))
        if user_size > 0:
            break
        else:
            print("Please enter a positive value for the maximum size.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

# Specify the folder path
path = os.getcwd()

resize_images(path, user_size)

print("Finished resizing images!")
