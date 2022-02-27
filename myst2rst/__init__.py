#!/usr/bin/env python3

from docutils.core import publish_string
from myst_parser.docutils_ import Parser
from docutils_rst_writer import RstWriter
import sys

def main()

    writer = RstWriter()

    source = open(sys.argv[1]).read()
    output = publish_string(
        source=source,
        writer=writer,
        settings_overrides={
            "myst_enable_extensions": ["deflist"],
            "embed_stylesheet": False,
        },
        parser=Parser(),
    )
    text = output.decode('utf-8')
    print(text)

if __name__ == "__main__":
    main()
