class Style:
    """
    Styled output
    """
    Reset = "\033[0m"
    Bold = "\033[1m"
    Dim = "\033[2m"
    Italic = "\033[3m"
    Underlined = "\033[4m"
    Blink = "\033[5m"
    Inverted = "\033[7m"
    Hidden = "\033[8m"
    Strikethrough = "\033[9m"
    Underlined_double = "\033[21m"
    Underlined_lower = "\033[52m"


class Fg:
    """
    Foreground coloured output
    """
    Reset = "\033[0m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    Beige = "\033[37m"
    White = "\033[38m"
    Grey = "\033[90m"
    Light_red = "\033[91m"
    Light_green = "\033[92m"
    Light_yellow = "\033[93m"
    Light_blue = "\033[94m"
    Light_magenta = "\033[95m"
    Light_cyan = "\033[96m"


class Bg:
    """
    Background coloured output
    """
    Reset = "\033[0m"
    Black = "\033[40m"
    Red = "\033[41m"
    Green = "\033[42m"
    Yellow = "\033[43m"
    Blue = "\033[44m"
    Magenta = "\033[45m"
    Cyan = "\033[46m"
    Beige = "\033[47m"
    White = "\033[48m"
    Grey = "\033[100m"
    Light_red = "\033[101m"
    Light_green = "\033[102m"
    Light_yellow = "\033[103m"
    Light_blue = "\033[104m"
    Light_magenta = "\033[105m"
    Light_cyan = "\033[106m"


class ControlCharacters:
    """
    Backslash: \\
    Double quote: \"
    Quote: \'
    """
    # Backslash \\
    # Double quote \"
    # Quote \'

    Backspace = "\b"
    Tab = "\t"
    Carriage_return = "\r"
