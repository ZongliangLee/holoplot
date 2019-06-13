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
    def test_load(self,number):
        filename = str(number) + '_saved'
        self.__class__.apps.save(number,filename)
        if number%12 == 0:
            assert self.__class__.apps.load(filename) == 'Output is: Boom'
        elif number%3 == 0:
            assert self.__class__.apps.load(filename) == 'Output is: Bang'
        elif number%4 == 0:
            assert self.__class__.apps.load(filename) == 'Output is: Bing'
        else:
            assert self.__class__.apps.load(filename) == 'Output is: Meh'
        os.remove(str(filename))

    def test_load_nonnumeric_into_file(self,nonnumeric):
        filename = str(nonnumeric) + '_saved'
        self.__class__.apps.save(nonnumeric,filename)
        time.sleep(1)
        assert os.path.exists(filename)
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.load(filename)]
        if res != []:
            raise ValueError("Nonnumeric input should not play any sounds")
        os.remove(str(filename))

    def test_load_float_into_file(self,floatNumber):
        filename = str(floatNumber) + '_saved'
        self.__class__.apps.save(floatNumber,filename)
        time.sleep(1)
        assert os.path.exists(filename)
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.load(filename)]
        if res != []:
            raise ValueError("Float number should not play any sounds")
        os.remove(str(filename))

    def test_load_neative_number_into_file(self,negativeNumber):
        filename = str(negativeNumber) + '_saved'
        self.__class__.apps.save(str(negativeNumber)[1:],filename)
        time.sleep(1)
        assert os.path.exists(filename)
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.load(filename)]
        if res != []:
            raise ValueError("Negative number input should not play any sounds")
        os.remove(str(filename))

    def test_load_exceed_number_into_file(self,exceedNumber):
        filename = str(exceedNumber) + '_saved'
        self.__class__.apps.save(str(exceedNumber)[1:],filename)
        time.sleep(1)
        assert os.path.exists(filename)
        res = [x for x in self.__class__.sounds if x in self.__class__.apps.load(filename)]
        if res != []:
            raise ValueError("Negative number input should not play any sounds")
        os.remove(str(filename))