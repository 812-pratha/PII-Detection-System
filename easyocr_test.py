import easyocr
import matplotlib.pyplot as plt
import cv2

# Initialize the reader with the languages you want to support
# You can specify more than one language. Here we use English and French.
reader = easyocr.Reader(['en', 'hi'])  # Replace with the desired language codes

# Load the image
image_path = 'path_to_image.jpg'
image = cv2.imread(image_path)

# Perform OCR
results = reader.readtext(image_path)

# Display the results
for (bbox, text, prob) in results:
    print(f"Detected text: {text} (Confidence: {prob:.2f})")

    # Draw bounding boxes around detected text
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# Display the image with the bounding boxes
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()