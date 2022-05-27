import base64

def encode(file_name:str)->str:
    img_str = ""
    with open(file_name, "rb") as img:
        img_str = base64.b64encode(img.read())
    return img_str

print(encode("./img.jpg"))