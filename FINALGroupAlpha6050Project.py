#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Group Project
INF 6050
Fall 2019
Group Alpha
"""
# Import modules for making requests over the internet and handling XML.
import urllib
import xml.etree.ElementTree as etree
# Change path for appending modules
import sys
sys.path.append('./alpha_module')
import alphamodule
# Set a constant for the key needed to access Goodreads API
# Details about the Goodreads API are at https://www.goodreads.com/api
GOODREADS_API_KEY = "Zzj6rZRv0wUDWSgWS5DCvg"


# Give a welcome message and instructions to the user.
alphamodule.print_stars()
alphamodule.single_tab("GOODREADS AUTHOR SEARCH")
alphamodule.print_stars()
alphamodule.new_line()
print("Welcome!  You can use this program to find information about any author " +
      "in the Goodreads database. You will be able to enter an author's " +
      "name and receive a list of the book titles Goodreads has on record for " +
      "that author and each book's average Goodreads rating.")

# Set up a loop to allow the user to quit at any time.
search_again='y'
while search_again=='y':
    # Ask the user to input the name of an author.
    user_input = input("Enter the name of the author you wish to search or press q to quit: ").lower()
    if user_input == 'q':
        print("You have chosen to quit.")
        break
    else:
        pass
    # Encode the author input string in urlib.parse.quote_plus to make it usable in         a URL. Set that value as a variable.
    author_name_goes_here = urllib.parse.quote_plus(user_input)
    
    # Set a variable to build the full URL for the API request for author ID. 
    auFullRequest = "https://www.goodreads.com/api/author_url/" + author_name_goes_here + "?key=" + GOODREADS_API_KEY
    
    # First, we need to request the ID number associated with the author's name in Goodreads. This allows us to make a more specific request when we get the list of books and gives us data that is much less messy.
    # Make the request and save the response as a string.
    auConnection = urllib.request.urlopen(auFullRequest)
    auResponseString = auConnection.read().decode()
    # Turn the string into an XML formatted document in order to find information.
    auTree = etree.fromstring(auResponseString)
    
    # Extract the author's Goodreads ID from the data and set it as a variable to be inserted in the next request.
    authorInfo = auTree.find("author")
    # If the user input is not a recognized author, there will be an AttributeError when trying to find the id number. Restart the loop.
    try:
        auId = authorInfo.attrib["id"]
    except AttributeError:
        print("Goodreads does not recognize that author name.")
        print("Please try again.")
        continue
    
    # Set a variable to build the full URL for the API request for book information. This will give us the book titles and average ratings information associated with the previously gathered author ID.
    bkFullRequest = "https://www.goodreads.com/author/show/" + auId + "?format=xml&key=" + GOODREADS_API_KEY
    
    # Make the request for book information and save the response as a string.
    bkConnection = urllib.request.urlopen(bkFullRequest)
    bkResponseString = bkConnection.read().decode()
    # Turn the string into an XML formatted document in order to find information.
    bkTree = etree.fromstring(bkResponseString)
    
    # Find the author name and confirm it in an introductory line.
    bkWriter = bkTree[1][1].text
    alphamodule.print_stars()
    print("\nThe author you searched is {}. Here are the books listed in Goodreads for {}:".format(bkWriter, bkWriter))
    # Find each book listed in the XML
    for book in bkTree.iter("book"):
        bkTitle = book.find("title").text
        bkRank = book.find("average_rating").text
        # Print out the title and average rating for each book.
        print("\nTitle:", bkTitle, "\n\tAverage Goodreads Rating:", bkRank)
    
    # Message in loop to ask if they want to search another author.
    search_again=input("Do you want to search another author? Press y to search again or anything else to quit: ").lower()

# Thank you/goodbye/quit
alphamodule.print_stars()
alphamodule.single_tab("THANK YOU FOR USING GOODREADS AUTHOR SEARCH")
alphamodule.print_stars()
