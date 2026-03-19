def clean_input(user_data):
    """
    Standard Security Sanitizer:
    1. Removes whitespace
    2. Normalizes to lowercase
    3. Neutralizes common injection characters (';' and "'")
    """
    # Step 1 & 2: Strip and Lowercase
    cleaned = user_data.strip().lower()

    # Step 3: Neutralize dangerous characters
    cleaned = cleaned.replace("'", "")
    cleaned = cleaned.replace(";", "")

    return cleaned


def validate_path(input_string):
    """
    Checks if the input is a simple alphanumeric string (Safe for basic logic).
    Returns True if safe, False if it contains risky symbols.
    """
    # Only allow letters, numbers, and dots (for IPs/Filenames)
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789."
    return all(char in allowed_chars for char in input_string)


# --- Quick Test Logic ---
if __name__ == "__main__":
    test_input = "  'ADMIN;  "
    result = clean_input(test_input)

    print(f"--- Security Scrub Report ---")
    print(f"Original: [{test_input}]")
    print(f"Cleaned:  [{result}]")
    print(f"Status:   {'Safe' if validate_path(result) else 'Review Required'}")
