from BingBnagBoomLibs import BingBnagBoomLibs
import re
import pytest
import os
import time
from application_locattion import *

@pytest.fixture
def nonnumeric():
    return 'nonnumeric'

@pytest.fixture
def floatNumber():
    return 1.1

@pytest.fixture
def negativeNumber():
    return -1

@pytest.fixture
def exceedNumber():
    return 101

class TestCase(object):
    
    sounds = ['Boom','Bing','Meh','Bang']
    apps = BingBnagBoomLibs(path)

    @pytest.mark.parametrize('number', range(0, 100))
    def test_calculate(self,number):
        if number%12 == 0:
            assert self.__class__.apps.calculate(number) == 'Output is Boom'
        elif number%3 == 0:
            assert self.__class__.apps.calculate(number) == 'Output is Bang'
        elif number%4 == 0:
            assert self.__class__.apps.calculate(number) == 'Output is Bing'
        else:
            assert self.__class__.apps.calculate(number) == 'Output is Meh'
    
    def test_nonnumeric(self,nonnumeric):        
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.calculate(nonnumeric)]
        if res != []:
            raise ValueError("Nonnumeric input should not play any sounds")

    def test_float(self,floatNumber):
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.calculate(floatNumber)]
        if res != []:
            raise ValueError("Float number input should not play any sounds")

    def test_neative_number(self,negativeNumber):
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.calculate(negativeNumber)]
        if res != []:
            raise ValueError("Number less than 100 should not play any sounds")
    
    def test_exceed_range(self,exceedNumber):        
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.calculate(exceedNumber)]
        if res != []:
            raise ValueError("Number larger than 100 should not play any sounds")