def image_caption(image):
    if image == "beach":
        return "A sunny day at the beach"
    elif image == "mountain":
        return "A breathtaking view of the mountains"
    elif image == "city":
        return "A bustling cityscape with towering buildings"
    else:
        return "Unable to generate caption for this image"

# Example usage:
image1 = "beach"
caption1 = image_caption(image1)
print("Image:", image1)
print("Caption:", caption1)

image2 = "mountain"
caption2 = image_caption(image2)
print("\nImage:", image2)
print("Caption:", caption2)

image3 = "forest"
caption3 = image_caption(image3)
print("\nImage:", image3)
print("Caption:", caption3)