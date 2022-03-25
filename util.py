class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def color_header(text):
    return Colors.HEADER + Colors.BOLD + text + Colors.ENDC

def color_subheader(text):
    return Colors.HEADER + Colors.UNDERLINE + text + Colors.ENDC

def color_codeblock(text):
    return Colors.OKBLUE + Colors.BOLD + text + Colors.ENDC

def color_warning_box(text):
    return Colors.WARNING + Colors.BOLD + text + Colors.ENDC

def color_note_box(text):
    return Colors.OKBLUE + Colors.BOLD + text + Colors.ENDC

def color_tip_box(text):
    return Colors.OKGREEN + Colors.BOLD + text + Colors.ENDC

def color_url(text):
    return Colors.OKCYAN + text + Colors.ENDC