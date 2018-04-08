colors = {
    'DANGER': '\033[91m',
    'WARNING': '\033[33m',
    'MILD': '\033[94m',
    'OK': '\033[92m',
    'RESET': '\033[0m',
    'BLUE': '\033[94m',
    'CYAN': '\033[96m',
}


def color(text, text_color):
    if text_color in colors:
        return ''.join([colors[text_color], text, colors['RESET']])
    return text

# HEADER = '\033[95m'
# OKBLUE = '\033[94m'
# OKGREEN = '\033[92m'
# WARNING = '\033[93m'
# FAIL = '\033[91m'
# ENDC = '\033[0m'
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m'
# NORMAL = '\033[0m'

# This could be the reset command in windows, currently using os.system('color')
