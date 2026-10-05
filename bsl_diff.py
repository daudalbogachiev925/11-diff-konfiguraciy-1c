import difflib

def diff(old_code, new_code):
    return '\n'.join(difflib.unified_diff(
        old_code.splitlines(),
        new_code.splitlines(),
        lineterm='', fromfile='old', tofile='new'))
