import io
import json
import logging

from deepface import DeepFace
from fdk import response

def verify(img1, img2, model_name = "VGG-Face"):
    result = "foo"
    try:
        result = DeepFace.verify(img1, img2, model_name = model_name)
    except (Exception, ValueError) as ex:
        logging.getLogger().error('Error calling DeepFace verifier: ' + str(ex))
    return result

def handler(ctx, data: io.BytesIO = None):
    img1 = "none"
    img2 = "none"
    try:
        body = json.loads(data.getvalue())
        img1 = body.get("img1")
        img2 = body.get("img2")
        if len(img1) < 15 or len(img2) < 15:
            raise ValueError("img1 and img2 must be set")
    except (Exception, ValueError) as ex:
        logging.getLogger().error('Error parsing json payload: ' + str(ex))

    logging.getLogger().info("len(img1): " + str(len(img1)) + " len(img2): " + str(len(img2)))

    logging.getLogger().info("Calling DeepFace Verifier")
    result = verify("data:image/,"+ img1, "data:image/," + img2)

    logging.getLogger().info("Result: " + result)

    return response.Response(
        ctx, response_data=result,
        headers={"Content-Type": "application/json"}
    )


