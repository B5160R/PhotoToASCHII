from PIL import Image
from PIL import ImageSequence  # Import the ImageSequence module
import time

class AschiiAnimator:
  def __init__(self):
    self.chars = ["#", "#", "@", "%", '=', '+', '*', ':', '-', '.', ' ']

  def get_ascii_art(self, image, cols=80, scale=1):
    """
    Converts an image to ASCII art using a character map based on luminance.

    Args:
      image: PIL image object.
      cols: Number of columns in the ASCII art output (default: 80).
      scale: Scaling factor to adjust character size (default: 1).
    """
    width, height = image.size
    grid_x, grid_y = width // cols, height // (cols * scale)
    out = ""

    for y in range(0, int(height), int(grid_y)):
      for x in range(0, int(width), int(grid_x)):
        luminance = image.getpixel((float(x), float(y)))
        out += self.chars[luminance // (155 // len(self.chars)) % len(self.chars)]
      out += "\n"
    return out

  def animate_image(self, image_path, delay=0.1, loops=10):
    """
    Animates an image by slightly changing the character map for each frame.

    Args:
      image_path: Path to the image file.
      delay: Time (in seconds) to wait between frames (default: 0.1).
      loops: Number of times to repeat the animation (default: 10, infinite if 0).
    """
    image = Image.open(image_path).convert('L')
    for _ in range(loops or float('inf')):
      for i in range(len(self.chars)):
        self.chars = self.chars[:i] + self.chars[i+1:] + self.chars[i:i+1]
        ascii_art = self.get_ascii_art(image, scale=0.4)  # Adjust scale as needed
        print(ascii_art)
        time.sleep(delay)
        # Clear the terminal before printing the next frame
        print("\033c")

  def animate_gif(self, gif_path, delay=0.1, loops=10):
    """
    Animates a GIF by displaying each frame with a delay between them.

    Args:
      gif_path: Path to the GIF file.
      delay: Time (in seconds) to wait between frames (default: 0.1).
      loops: Number of times to repeat the animation (default: 10, infinite if 0).
    """
    image = Image.open(gif_path)
    for _ in range(loops or float('inf')):
      for frame in ImageSequence.Iterator(image):
        ascii_art = self.get_ascii_art(frame.convert('L'), scale=0.4)  # Adjust scale as needed
        print(ascii_art)
        time.sleep(delay)
        # Clear the terminal before printing the next frame
        print("\033c")
      
# Example usage:
animator = AschiiAnimator()
#animator.animate_image("cat.gif", delay=0.01, loops=20)
animator.animate_gif("cat.gif", delay=0.1, loops=10)