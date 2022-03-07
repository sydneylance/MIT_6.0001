#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:24:41 2021

@author: sydneylance
"""

# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewsStory object
                
        guid (string): globaly unique identifier
        title (string)
        description (string)
        link (string)
        pubdate (string)
        
        '''
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid
    
    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title
    
    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description
    
    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link
    
    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        '''
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        '''
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2

class PhraseTrigger(Trigger):
    
    def __init__(self, phrase):
        '''
        initializes a PhraseTrigger object
        
        phrase (str): a phrase that one is searching for within the desired text
        '''
        self.phrase = phrase
    
    def get_phrase(self):
        '''
        Used to safely access self.phrase outside of the class
        
        Returns: self.phrase in lowercase
        '''
        return self.phrase.lower()
    

    def is_phrase_in(self, text):
        ''' 
        Determines if the phrase is present in given text
        
        text (str): aspect of a NewsStory
        
        Returns: True if phrase is present in text
        '''
        #define variables
        text = text.lower()
        phrase_list = PhraseTrigger.get_phrase(self).split(" ")
        phrase_str = PhraseTrigger.get_phrase(self)
        text_string = ""
        
        for letter in text:
            if letter in string.punctuation:
                text = text.replace(letter," ")
        
        text_list = text.split(" ")
        
        #in_list accounts for words in phrase being present without trailing characters
        in_list = None
        for word in phrase_list:
            if word in text_list:
                in_list = True
            else:
                in_list = False
        
        for word in text_list:
            if word != '':
                text_string += " " + word
                
        #string accounts for orientation of the phrase (that the words in the phrase are present in the correct order to to eachother)
        in_str = None
        if phrase_str in text_string:
            in_str = True
        else:
            in_str = False
        
        if (in_list == True) and (in_str == True):
            ans = True
        else: 
            ans = False
        
        return ans 

# Problem 3
class TitleTrigger(PhraseTrigger):
    
    def __init__(self, phrase):
        '''
        initializes a TitleTrigger object
        
        phrase (str): a phrase that one is searching for within the desired text
        '''
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        ''' 
        evaluates if a phrase is present in the title of a news story
        
        story: NewsStory object 
        
        Returns: True if phrase is present in title, False if not
        '''
        return self.is_phrase_in(story.get_title())
        

# Problem 4

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        '''
        initializes a DescriptionTrigger object
        
        phrase (str): a phrase that one is searching for within the desired text
        '''
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        ''' 
        evaluates if a phrase is present in the description of a story
        
        story: NewsStory object 
        
        Returns: True if phrase is present in description, False if not
        '''
        return self.is_phrase_in(story.get_description())
    

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        '''
        initializes a TimeTrigger object
        
        time (str): a time in EST (ex. )
        
        self.time is converted to datetime format
        '''
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))
    
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        '''
        initializes a BeforeTrigger object
        
        time (str): a time in EST (ex. ) converted to a datetime format
        
        '''
        TimeTrigger.__init__(self, time)
    
    def evaluate(self, story):
        '''
        Evaluates whether a story was published before a given time
        
        story = a NewsStory object
        
        Returns: True if the story was published before a given time, False if not
        
        '''
        published = story.get_pubdate()
        published = published.replace(tzinfo = pytz.timezone("EST"))
            
        return self.time > published
    
class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        '''
        initializes a BeforeTrigger object
        
        time (str): a time in EST (ex. ) converted to a datetime format
        
        '''
        TimeTrigger.__init__(self, time)
    
    def evaluate(self, story):
        '''
        Evaluates whether a story was published after a given time
        
        story = a NewsStory object
        
        Returns: True if the story was published after a given time, False if not
        
        '''
        published = story.get_pubdate()
        published = published.replace(tzinfo = pytz.timezone("EST"))
            
        return self.time < published
    

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        '''
        initializes a NotTrigger object
        
        Trigger(class): a trigger class
        
        '''
        self.trigger = trigger
        
    def evaluate(self, story):
        '''
        Inverts the result of an existing trigger
        
        story = a NewsStory object
        
        Returns: True if the result of the input trigger is False, False if the input Trigger result is True
        
        '''
        if self.trigger.evaluate(story) == True:
            ans = False
        else:
            ans = True
        return ans
        
        
# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        '''
        initilizes an AndTrigger object
        
        Trigger1 (class): a trigger class
        
        Trigger2(class): a different trigger class
        
        '''
        self.trigger1 = trigger1
        
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        '''
        Evaluates if the results of 2 triggers are both True
        
        story = a NewsStory object
        
        Returns: True if both triggers would fire
        
        '''
        if (self.trigger1.evaluate(story) == True) and (self.trigger2.evaluate(story) == True):
            ans = True
        else:
            ans = False
        return ans

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        '''
        initializes an OrTrigger object
        
         Trigger1 (class): a trigger class
        
        Trigger2(class): a different trigger class
        
        '''
        self.trigger1 = trigger1
        
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        '''
        Evaluates if one or both of input triggers would fire
        
        story = a NewsStory object
        
        Returns: True if one or both triggers would fire
        
        '''
        if (self.trigger1.evaluate(story) == True) or (self.trigger2.evaluate(story) == True):
            ans = True
        else:
            ans = False
        return ans


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    
    story_list = []
    for trigger in triggerlist:
        for story in stories:
            if trigger.evaluate(story) == True:
                story_list.append(story)
    return story_list


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    item_list = []
    trigger_dict = {}
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    for line in lines:
        item_list = line.split(",")
    for i in range(len(item_list)):
        if item_list[i%3] == 0:
            trigger_dict[i] = trigger_dict.get(i, i+1, i+2)
    return trigger_dict



story = NewsStory('guid', 'title', 'description', 'link', 'pubdate')
# print(story.get_title())
# title = story.get_title()
# phrase = PhraseTrigger('title')
test = TitleTrigger('title')
# text = 'purplecowpurplecowpurplecow'

# print(phrase.is_phrase_in(text))


test_eval = test.evaluate(story)

print(test_eval)