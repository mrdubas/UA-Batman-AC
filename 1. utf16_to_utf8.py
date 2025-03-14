import os

def convert_utf16_to_utf8():
    for filename in os.listdir():
        if filename.lower().endswith(".int"):
            with open(filename, "r", encoding="utf-16-le") as f:
                content = f.read()
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Converted: {filename} (UTF-16 LE → UTF-8)")

if __name__ == "__main__":
    convert_utf16_to_utf8()
