import zlib

def compress_bytes(byte_obj):
    compressed_bytes = zlib.compress(byte_obj)
    return compressed_bytes

def decompress_bytes(compressed_byte_obj):
    decompressed_bytes = zlib.decompress(compressed_byte_obj)
    return decompressed_bytes

def main():
    try:
        original_string = b"Python Exercises."

        compressed_string = compress_bytes(original_string)
        decompressed_string = decompress_bytes(compressed_string)

        print("Original Bytes:", original_string)
        print("\nCompressed Bytes:", compressed_string)
        print("\nDecompressed Bytes:", decompressed_string)
        print("\nDecompressed String:", decompressed_string.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()