import os
import sys
from PIL import Image
import pygame


class FileManager:
    """
    A class to manage loading and caching of images in a Pygame application.
    """

    def __init__(self, resource_dir='assets'):
        """
        Initialize the ImageManager.

        Args:
            resource_dir (str, optional): The directory where the image files are located. Defaults to 'resources'.
        """
        self.resource_dir = resource_dir
        self.image_cache = {}

    def load_image(self, file_name, convert_alpha=False):
        """
        Load an image file and return a Pygame Surface.

        Args:
            file_name (str): The name of the image file.
            convert_alpha (bool, optional): Whether to convert the image to use per-pixel alpha blending. Defaults to False.

        Returns:
            pygame.Surface: The loaded image as a Pygame Surface.
        """
        if file_name in self.image_cache:
            return self.image_cache[file_name]

        file_path = self.resource_path(file_name)
        try:
            image = pygame.image.load(file_path)
            if convert_alpha:
                image = image.convert_alpha()
            else:
                image = image.convert()
            self.image_cache[file_name] = image
            return image
        except pygame.error as e:
            print(f"Error loading image: {file_path}")
            raise e

    def resource_path(self, relative_path):
        """
        Get the absolute path to a resource file.

        Args:
            relative_path (str): The relative path to the resource file.

        Returns:
            str: The absolute path to the resource file.
        """
        try:
            base_path = getattr(sys, '_MEIPASS',
                                os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, self.resource_dir, relative_path)

    def load_gif(self, filename):
        pil_image = Image.open(self.resource_path(filename))
        print("frames: ",getattr(pil_image, "n_frames", 1))
        frames = []
        try:
            while True:
                frames.append(pil_image.copy())
                pil_image.seek(pil_image.tell() + 1)
        except EOFError:
            pass
        return frames

    def pil_image_to_pygame_surface(self, pil_image):
        # Convert the PIL Image to RGB mode
        pil_image = pil_image.convert("RGB")

        # Get the size of the image
        image_size = pil_image.size

        # Get the image data as bytes
        image_data = pil_image.tobytes()

        # Create a Pygame Surface object with proper size and format
        pygame_image = pygame.image.fromstring(image_data, image_size, "RGB")

        return pygame_image
