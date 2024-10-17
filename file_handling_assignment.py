# file_handling_assignment.py

# File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write("This is the first line of text.\n")
        file.write("Here is a number: 12345\n")
        file.write("And another line with some more text.\n")
    print("File created and initial content written successfully.")

except FileNotFoundError as fnf_error:
    print(f"File not found error: {fnf_error}")

except PermissionError as perm_error:
    print(f"Permission error: {perm_error}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("File creation block executed.")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)

except FileNotFoundError as fnf_error:
    print(f"File not found error: {fnf_error}")

except PermissionError as perm_error:
    print(f"Permission error: {perm_error}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("File reading block executed.")

# File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("Appending a new line of text.\n")
        file.write("Another appended line with more details.\n")
        file.write("Final appended line to complete the task.\n")
    print("Additional content appended successfully.")

except FileNotFoundError as fnf_error:
    print(f"File not found error: {fnf_error}")

except PermissionError as perm_error:
    print(f"Permission error: {perm_error}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("File appending block executed.")
