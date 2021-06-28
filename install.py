#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path

DIR = "./home"
MARKER_BEGIN = b"EXTENSIBLE-DOTFILES BEGINS, DO NOT EDIT DIRECTLY {"
MARKER_END = b"EXTENSIBLE-DOTFILES ENDS, DO NOT EDIT DIRECTLY }"
COMMENT_CHAR_MARK = b"THE COMMENT CHAR"


def install_file(fn):
    if fn.endswith(('.pyc')):
        print("Ignore", fn)
        return

    with open(fn, "rb") as f:
        line = f.readline()
        if not line or line.find(COMMENT_CHAR_MARK) == -1:
            print("Skip {} as no '{}' found at the first line".format(
                fn, COMMENT_CHAR_MARK.decode('utf-8')))
            return

        comment_char = line.replace(COMMENT_CHAR_MARK, b'').strip(b'\n')
        marker_begin = comment_char + MARKER_BEGIN
        marker_end = comment_char + MARKER_END
        content = marker_begin + b'\n' + f.read() + b'\n' + marker_end
        # print(comment_char, content)

    dst_fn = os.path.expanduser(
        os.path.join('~', os.path.relpath(fn, DIR)))
    # print("filename", fn, dst_fn)
    Path(os.path.dirname(dst_fn)).mkdir(parents=True, exist_ok=True)

    old_content = b''
    try:
        with open(dst_fn, "rb") as f:
            old_content = f.read()
    except FileNotFoundError:
        pass

    begin = old_content.find(marker_begin)
    if -1 == begin:
        new_content = old_content + b'\n' + content
    else:
        end = old_content.find(marker_end)
        new_content = old_content[:begin] + content + \
            old_content[(end+len(marker_end)):]

    # print(new_content)
    print("Install {} to {}".format(fn, dst_fn))
    with open(dst_fn, "wb") as f:
        f.write(new_content)


for dirpath, dirnames, filenames in os.walk(DIR):
    for fn in filenames:
        install_file(os.path.join(dirpath, fn))
