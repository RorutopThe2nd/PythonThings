import sys


def file_perm_check(filename: str):
    try:
        with open(filename, "a"):
            pass
    except PermissionError:
        sys.exit(f"Write permission denied for '{filename}'")
    except OSError as e:
        sys.exit(f"Cannot access file: {e}")
