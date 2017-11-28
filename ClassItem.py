#! /usr/bin/env python3
# coding: utf-8

import random


class Item:

    def __init__(self, empty_spaces, name):
        self.position = random.choice(empty_spaces)
        self.name = name.capitalize()
