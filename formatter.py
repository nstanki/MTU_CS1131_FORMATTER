import re
import tkinter as tk
from tkinter import filedialog


def format_code(code):
    # Add spaces after/before parentheses/brackets and the inside content
    formatted_code = re.sub(r'\(\s*', '( ', code)
    formatted_code = re.sub(r'\s*\)', ' )', formatted_code)
    formatted_code = re.sub(r'\[\s*', '[ ', formatted_code)
    formatted_code = re.sub(r'\s*\]', ' ]', formatted_code)

    # Split long comments into multiple lines
    def split_long_comments(match):
        comment = match.group(0)
        words = comment.split()
        new_comment = ""
        line = ""
        for word in words:
            if len(line) + len(word) + 1 > 80:
                new_comment += line.rstrip() + "\n// "
                line = ""
            line += word + " "
        new_comment += line.rstrip()
        return new_comment

    formatted_code = re.sub(r'//.*', split_long_comments, formatted_code)

    return formatted_code


def main():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select a .java file
    file_path = filedialog.askopenfilename(
        filetypes=[("Java files", "*.java")])

    if file_path:
        with open(file_path, 'r') as file:
            java_code = file.read()

        formatted_code = format_code(java_code)

        # Save the formatted code to a new file
        with open(file_path.replace(".java", "_formatted.java"), 'w') as file:
            file.write(formatted_code)

        print(f"Formatted code saved to {
              file_path.replace('.java', '_formatted.java')}")
    else:
        print("No file selected.")


if __name__ == "__main__":
    main()
