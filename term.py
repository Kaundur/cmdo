
# TOOD - Are these valid on unix
# http://misc.flogisoft.com/bash/tip_colors_and_formatting

colors = {
    'DANGER': '\033[91m',
    'WARNING': '\033[33m',
    'MILD': '\033[94m',
    'OK': '\033[92m',
    'RESET': '\033[0m',
    'BLUE': '\033[94m',
    'CYAN': '\033[96m',
}

def color(text, color):
    if color in colors:
        return ''.join([colors[color], text, colors['RESET']])
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

