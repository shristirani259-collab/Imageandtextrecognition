import cv2
import pytesseract

# Uncomment and change the path if Tesseract is not added to PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = "Sample _ text.jpg"

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Recognize text
text = pytesseract.image_to_string(thresh)

print("===== Recognized Text =====")
print(text)

# Save extracted text
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nText saved in output.txt")

cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()