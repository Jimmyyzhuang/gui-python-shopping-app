#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:49:23 2024

@author: maluroldan
"""


import random
def chatter():
    greetings = ["Hello!", "What's up?", "How's it going?", "Greetings from Prime Threads!"]
    goodbyes = ["Bye!", "Goodbye!", "See you next time!", "Hope to see you soon!"]

    keywords = ["warriors","49ers", "giants", "sharks", "earthquakes"]
    responses = ["$100", "$75", "$50", "$25", "$10"]

    print(random.choice(greetings))
    user = input("What jersey do you want? (or type none to quit): ")        
    user = user.lower()

    while (user != "none"):
        keyword_found = False

        for index in range(len(keywords)):
            if (keywords[index] in user):
                print("The price is: " + responses[index])
                keyword_found = True

        if (keyword_found == False):
            new_keyword = input("I'm not sure how to answer you. What is a keyword that I should respond to? ")
            keywords.append(new_keyword)
            new_response = input("How would you like me to respond to " + new_keyword + "? ")
            responses.append(new_response)
   
        user = input("What jersey do you want? (or type none to quit): ")
        user = user.lower()

    print(random.choice(goodbyes))
    
chatter()