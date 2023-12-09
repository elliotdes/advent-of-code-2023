def get_input(file: str) -> str:
    with open(file, "r") as o:
        lines = o.read()
    return lines
