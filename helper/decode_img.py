import numpy as np
from PIL import Image
import io
import base64

def decode(str_img:str):
    # this method take base64 incoded image and returns the data
    # which is required for decoding the image.
    return np.array(Image.open(io.BytesIO(base64.b64decode(str_img))))