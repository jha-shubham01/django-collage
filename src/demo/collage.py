import cv2
from django.conf import settings
from PIL import Image
from skimage import io

IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080


def create_collage(images):
    """
    Create and save collage image in ItemList.
    """

    images = [io.imread(img) for img in images]
    images = [cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT)) for image in images]
    if len(images) > 2:
        half = len(images) // 2
        h1 = cv2.hconcat(images[:half])
        h2 = cv2.hconcat(images[half:])
        concat_images = cv2.vconcat([h1, h2])
    else:
        concat_images = cv2.hconcat(images)
    image = Image.fromarray(concat_images)

    # Image path
    image_name = "sj.jpg"
    image = image.convert("RGB")
    image.save(f"{settings.MEDIA_ROOT}/{image_name}")
    return image_name
