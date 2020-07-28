#! python3
#project(ph.n.& Email).py - finds phone numbers and Email addresses on the clipboard

import pyperclip,re

#creating Phone regex
phoneRegex = re.compile(r'''(
      (\d{3}|\(\d{3}\))?                         #area code
      (\s|-|\.)?                                 #seperator
      (\d{3})                                    #first 3 digits
      (\s|-|\.)                                  #seperator
      (\d{4})                                    #last 4 digits
      (\s*(ext|x|ext.)s*(\d{2,5}))?               #extension
      )''' , re.VERBOSE)

#creating Email address Regex

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+                          #username
        @                                          #@ symbol
        [a-zA-Z0-9.-]+                             #domain name
        (\.[a-zA-Z]{2,4})                          #dot-something
        )
''' , re.VERBOSE)

#Find matches in clibboard text.

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # Groups of Area code, first three digits of number and last four digits.
    #pyperclip.copy() function takes only a single string value, not a list of strings, so we called the join() method on matches
    if groups[8] != '':
        phoneNum += ' x' + groups[8]      #groups[8] is extension.
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard.
if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers and email addresses found.')





