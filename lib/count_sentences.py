#!/usr/bin/env python3 

import re

class MyString:

    def __init__(self, value = ""):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self,value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    value = property(get_value, set_value)

    def is_sentence(self):
        if self._value.endswith('.'):
            return True 
        else:
            return False

    def is_question(self):
        if self._value.endswith('?'):
            return True 
        else:
            return False

    def is_exclamation(self):
        if self._value.endswith('!'):
            return True 
        else:
            return False

    def count_sentences(self):
        sentences = [s.strip() for s in re.split(r'[.!?]', self._value) if s.strip()]
        return len(sentences)
   
 


