import re

def decode_script(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if n_rows > 0 else 0

    decoded_string = ""
    for col in range(n_cols):
        for row in range(n_rows):
            decoded_string += matrix[row][col]

    decoded_string = re.sub(r'([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])', r'\1 \2', decoded_string)

    return decoded_string

def main():
    matrix = [
        "Tsi",
        "h%x",
        "i #",
        "sM ",
        "$a ",
        "#t%",
        "ir!"
    ]

    decoded_message = decode_script(matrix)
    print(decoded_message)

if __name__ == "__main__":
    main()
