#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for use with Group Project
INF 6050
Fall 2019
Group Alpha

This module contains a series of functions that are useful for formatting purposes.
"""
def print_stars():
    """
    This function prints a line of 78 asterisks, primarily for formatting use.
    """
    print("*"*78)

def new_line():
    """
    This function prints a blank line.
    """
    print("\n")

def single_tab(x):
    """
    This function prints out whatever is passed with a single indent.
    """
    print("\t",x)

if __name__ == "__main__":
    print_stars()
    print("I am here only if this program is run by itself.")
    print("and not imported as a module.")
    print_stars()
