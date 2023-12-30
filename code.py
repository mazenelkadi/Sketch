import cv2  # OpenCV library for computer vision tasks

# Reading image
image_path = "Your-Path-To-File"
image = cv2.imread(image_path)  # Load the image from the specified path

# Converting BGR image to grayscale
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Image invert
inverted_image = 255 - gray_image  # Invert the grayscale image

# Blurring image
blurred_image = cv2.GaussianBlur(
    inverted_image, (43, 43), 0)  # Apply Gaussian Blur
# Create pencil sketch effect
pencil_sketch = cv2.divide(gray_image, blurred_image, scale=250.0)

# Display the original and the pencil sketch images
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)  # Wait for a key press to close the image windows

# Specify the output file names and paths
output_file = "Your-Path-To-File"  # Output path for grayscale image
output_sketch_file = "Your-Path-To-File"  # Output path for pencil sketch image

# Save the grayscale and pencil sketch images
cv2.imwrite(output_file, gray_image)  # Save the grayscale image
cv2.imwrite(output_sketch_file, pencil_sketch)  # Save the pencil sketch image
