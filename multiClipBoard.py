#! python3
# multiClipBoard.py - Saves and loads pieces of text to the clipboard.
# Usage:    python3 multiClipBoard.py save <keyword> - Saves clipboard or typed keyword to keyword.
#           python3 multiClipBoard.py <keyword> - Loads keyword to clipboard.
#           python3 multiClipBoard.py list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
