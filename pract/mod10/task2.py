import re

pattern = re.compile(
    r"^(#(?:[0-9a-fA-F]{3}){1,2}"
    r"|rgb\((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|(?:\d{1,2}|100)%)"
    r",\s*(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|(?:\d{1,2}|100)%)"
    r",\s*(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|(?:\d{1,2}|100)%)\)"
    r"|hsl\((\d{1,2}|[1-2]\d{2}|3[0-5]\d|360),\s*(\d{1,2}|100)%,\s*(\d{1,2}|100)%\))$"
)

correct_colors = [
    "#21f48D",
    "#888",
    "rgb(255, 255, 255)",
    "rgb(10%, 20%, 0%)",
    "hsl(200, 100%, 50%)",
    "hsl(0, 0%, 0%)"
]

incorrect_colors = [
    "#2345",
    "ffffff",
    "rgb(257, 50, 10)",
    "hsl(20, 10, 0.5)",
    "hsl(34%, 20%, 50%)"
]

for color in correct_colors + incorrect_colors:
    result = bool(pattern.match(color))
    print(f"{color}: {result}")