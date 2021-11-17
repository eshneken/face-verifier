from deepface import DeepFace
import base64

def verify(img1, img2, model_name = "VGG-Face"):
    result = DeepFace.verify(img1, img2, model_name = model_name)
    return result

with open("./images/aniston1.jpg", "rb") as img1_path:
    img1 = "data:image/," + base64.b64encode(img1_path.read()).decode("utf-8")
with open("./images/cox1.jpg", "rb") as img2_path:
    img2 = "data:image/," + base64.b64encode(img2_path.read()).decode("utf-8")

result = verify(img1, img2)
print(result)

