import sys, pathlib, fitz
fname = sys.argv[1]  # get document filename
with fitz.open(fname) as doc:  # open document
    text = chr(12).join([page.get_text() for page in doc])
# write as a binary file to support non-ASCII characters
pathlib.Path(fname + ".txt").write_bytes(text.encode())