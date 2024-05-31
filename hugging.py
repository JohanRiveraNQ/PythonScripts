# Use a pipeline as a high-level helper
from transformers import pipeline
def imageClass():  

    pipe = pipeline("image-classification", model="google/vit-base-patch16-224")
    return pipe