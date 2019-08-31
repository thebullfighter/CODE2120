from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys
import random

# Create your views here.

class insultGenerator(object):
    def __init__(self):
        # lists of insult fodder

        self.nounList = ['Slacker',
                         'Buddha',
                         'nerd',
                         'doodle head',
                         'butthead',
                         'assface',
                         'derp',
                         'moron',
                         'nerf herder']
        self.adjectiveList = ['skinny',
                              'ugly',
                              'shrimp',
                              'slimy',
                              'scrooge',
                              'scabby',
                              'bitch']
        self.connectorList = ['are one',
                              'are the biggest',
                              'are becoming a']

    @csrf_exempt
    def getInsult(self):
        insult = "you"

        # connector phrase
        connector = random.randint(1, len(self.connectorList))
        insult += " " + self.connectorList[connector-1]

        # adjectives
        adjCount = random.randint(2,4)
        random.shuffle(self.adjectiveList)
        for i in xrange(0,adjCount):
            if i != 0:
                insult += ", "

            else:
                insult += " "
            insult += self.adjectiveList[i]

        # ending noun
        noun = random.randint(1,len(self.nounList))
        insult += " " + self.nounList[noun-1]
        return insult


# example
if __name__ == '__main__':
    ig = insultGenerator()
    print ig.getInsult()
    print ig.getInsult()
    print ig.getInsult()
    print ig.getInsult()
