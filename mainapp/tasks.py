from celery import shared_task
import os
import io
from mainapp.models import InputImages,OutputImage


def image_compare(image_a, image_b):
    """ your own code logic to compare images"""


@shared_task
def save_image_to_models():

    results = InputImages.objects.all()
    for result in results:
        inp_image = result.input_image
        std_image = result.standard_image

        """
        Call your image_compare function here by passing the two images of the InputImages model

        Something like this: output_image = image_compare(std_image, inp_image)

        """
        output = OutputImage.objects.create(output_image="""returned output_image by image_compare function""",input_key=result)


