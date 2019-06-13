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

    @pytest.mark.parametrize('number', range(0, 10))
    def test_save(self,number):
        filename = str(number) + '_saved'
        self.__class__.apps.save(number,filename)
        time.sleep(1)
        assert os.path.exists(filename)
        os.remove(str(filename))
    
    def test_save_nonnumeric_into_file(self,nonnumeric):
        filename = str(nonnumeric) + '_saved'
        self.__class__.apps.save(nonnumeric,filename)
        time.sleep(1)
        assert os.path.exists(filename)
        os.remove(str(filename))

    def test_save_float_into_file(self,floatNumber):
        filename = str(floatNumber) + '_saved'
        self.__class__.apps.save(floatNumber,filename)
        time.sleep(1)
        assert os.path.exists(filename)
        os.remove(str(filename))

    def test_save_neative_number_into_file(self,negativeNumber):
        filename = str(negativeNumber) + '_saved'
        self.__class__.apps.save(str(negativeNumber)[1:],filename)
        time.sleep(1)
        assert os.path.exists(filename)
        os.remove(str(filename))
    
    def test_save_exceed_range(self,exceedNumber):        
        filename = str(exceedNumber) + '_saved'
        self.__class__.apps.save(str(exceedNumber)[1:],filename)
        time.sleep(1)
        assert os.path.exists(filename)
        os.remove(str(filename))