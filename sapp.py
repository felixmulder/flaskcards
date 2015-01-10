#!/bin/env python

import random
import sys

from questions import questions

def main():
    def get_question():
        q_iter = [(k, v) for k, v in questions.items()]
        
        if len(q_iter) == 0:
            print("DONE")
            sys.exit(0)
            
        rand = random.randint(0, len(q_iter)-1)
        q, a = q_iter[rand]
        del questions[q]
        return q, a

    while True:
        print("%s question remaining!" % len(questions.items()))
        raw_input("Press key to get question...")
        q, a = get_question()
        print("%s\n" % q)
        raw_input("Please answer the question in you mind, then press any key to view answer...")
        print("%s\n" % a)
    
if __name__ == "__main__":
    main()
