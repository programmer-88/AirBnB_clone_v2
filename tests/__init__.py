#!/usr/bin/python3
"""
This module contains functions found in the tests
"""

from typing import TextIO

def clear_output(stream: TextIO):
    """
    function that clears the contents of stream
    """
    stream.seek(0)
    stream.truncate(0)