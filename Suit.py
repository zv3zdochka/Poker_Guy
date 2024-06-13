from PIL import Image


class Suit():

    # Open the image
    im = Image.open('image.png')

    # Quantize down to 2 colour palettised image using *"Fast Octree"* method:
    q = im.quantize(colors=2, method=2)

    # Now look at the first 2 colours, each 3 RGB entries in the palette:
    print(q.getpalette()[:6])
