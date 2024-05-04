from PIL import Image
import time

chars = ["#", "#", "@", "%", '=', '+', '*', ':', '-', '.', ' ']

def get_ascii_art(image, cols=100, scale=1):
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
      out += chars[luminance // (255 // len(chars)) % len(chars)]
    out += "\n"
  return out

def animate_image(image_path, delay=10.1, loops=10):
  """
  Animates an image by slightly changing the character map for each frame.

  Args:
    image_path: Path to the image file.
    delay: Time (in seconds) to wait between frames (default: 0.1).
    loops: Number of times to repeat the animation (default: 10, infinite if 0).
  """
  image = Image.open(image_path).convert('L')
  for _ in range(loops or float('inf')):
    for i in range(len(chars)):
      modified_chars = chars[:i] + chars[i+1:] + chars[i:i+1]
      ascii_art = get_ascii_art(image, scale=1.0)  # Adjust scale as needed
      print(ascii_art)
      time.sleep(delay)
      # Clear the terminal before printing the next frame
      print("\033c")

# Example usage:
animate_image("image.jpg")