import os

def convert_utf8_to_utf16():
    for filename in os.listdir():
        if filename.lower().endswith(".int"):
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            with open(filename, "w", encoding="utf-16-le") as f:
                f.write(content)
            print(f"Converted: {filename} (UTF-8 → UTF-16 LE)")

if __name__ == "__main__":
    convert_utf8_to_utf16()
