def validate_non_empty_string(input_str: str, field_name: str):
    if not input_str.strip():
        raise ValueError(f"{field_name} cannot be empty")

def validate_email(email: str):
    if '@' not in email:
        raise ValueError("Invalid email address")

def find_by_attribute(objects: list, attribute: str, value):
    for obj in objects:
        if getattr(obj, attribute, None) == value:
            return obj
    return None