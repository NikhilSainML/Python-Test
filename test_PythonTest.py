from PythonTest.SeleniumScript import Test
import pandas as pd

def test_preprocess():
    obj1= Test()
    df = obj1.PreProcessing()
    assert 'an' not in df['Name']

def test_formauto():
    obj2= Test()
    fAuto = obj2.FormAuthomation()
    assert fAuto == 43