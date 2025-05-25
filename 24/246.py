def read_image(file_path):
    with open(file_path, "rb") as file:
        image_bytes = file.read()
    return image_bytes

def save_modified_image(file_path, modified_bytes):
    with open(file_path, "wb") as file:
        file.write(modified_bytes)

def main():
    try:
        input_image_path = "flowchart_image.png"
        output_image_path = "output_image.png"

        original_image_bytes = read_image(input_image_path)

        modified_image_bytes = original_image_bytes + b"Watermark"

        save_modified_image(output_image_path, modified_image_bytes)

        print("Image read and modified successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()