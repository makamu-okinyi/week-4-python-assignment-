# file_processor.py

def process_file():
    filename = input("Enter the filename to read: ")

    try:
        # Try to read the file
        with open(filename, "r") as infile:
            content = infile.read()
            print("\n✅ File read successfully!")

        # Ask user for modification choice
        print("\nChoose a modification:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Count words")
        print("4. Reverse content")
        choice = input("Enter your choice (1-4): ")

        # Modify content based on choice
        if choice == "1":
            modified_content = content.upper()
        elif choice == "2":
            modified_content = content.lower()
        elif choice == "3":
            word_count = len(content.split())
            modified_content = f"Word Count: {word_count}\n\n{content}"
        elif choice == "4":
            modified_content = content[::-1]
        else:
            print("❌ Invalid choice. No modification applied.")
            return

        # Create new filename
        output_file = "modified_" + filename

        # Write modified content
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Modified content written to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Run the function
if __name__ == "__main__":
    process_file()
