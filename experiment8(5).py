class FileEmptyError(Exception):
    """Raised when the file has no content."""
    pass

class SensitiveFileError(Exception):
    """Raised when attempting to access a restricted file."""
    pass

def read_system_file(filename):
    try:
        if filename == "secret.txt":
            raise SensitiveFileError("Access Denied: File is restricted.")
            
        with open(filename, "r") as f:
            content = f.read()
            if not content:
                raise FileEmptyError("The file is empty.")
            print(content)
            
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except SensitiveFileError as e:
        print(f"Security Error: {e}")
    except FileEmptyError as e:
        print(f"Content Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Testing the custom logic
read_system_file("nonexistent.txt")
read_system_file("secret.txt")