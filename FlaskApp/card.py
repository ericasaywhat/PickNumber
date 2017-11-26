"""
Python program that takes in a spreadsheet of medical terminology and makes flash cards

author: Erica J. Lee
updated: August 11, 2016

"""
import random
from pattern.web import *
import string

url = URL("https://docs.google.com/spreadsheets/d/1InzQ49dfqkr7XBnxoz8j7mn1Kb8JWl_NoROQH655Pnw/edit?usp=sharing")

sheet = url.download()
bank = plaintext(sheet).encode("UTF-8")

#save sheet to a txt file so we don't have to download multiple times
with open('medicalterms.txt', 'w') as e:	
	e.write(bank)

d = open('medicalterms.txt').read()
start_index = d.index('2')			#skips the intro stuff and finds where the list starts
end_index = d.index('Loading')	#finds where the list ends

just_list = d[start_index:end_index]


def processed_list(fp):
    """
    cleans up the list into just the vocabulary in readable text without numbers that had been
    used to label the rows in the Google Sheet 
    """

    lines = ""
	
    for line in fp.split("\n"):
        if line.isdigit() == True:                    #taking out the row numbers
            continue
        lines += line 
    return lines.split('.')

clean_list = processed_list(just_list)

terms = clean_list[0::2]
examples = clean_list[1::2]



def card(terms,examples):
    """builds the cards and keeps score"""
    score = 0
    for i in range(len(terms)):
        lol = terms[i].index('-')
        print terms[i][0:lol]
        user_ans = raw_input("Please input your definition:")
        print "This is the definition", terms[i][lol:]
        correction = raw_input('Was your answer right? (Y/N)')
        
        while True:
            if correction.upper() in ['Y','YES']:
                score += 1
                print "Awesome! Score:", score
                break
            elif correction.upper() in ['N','NO']:
                print "Darn it! Maybe next time. Score:", score
                break
            else:
                correction = raw_input("Sorry, I didn't understand that. Was your answer right? (Y/N)")

card(terms,examples)