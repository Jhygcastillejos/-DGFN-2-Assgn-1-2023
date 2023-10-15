
#TPRG 2131 Fall 2023 Assignment 1 (test_A_V_calc)

# Jhyg Castillejos (100882960)
# TPRG1131 Section 2131
# October 15, 2023
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
# Test file for A_V_calc.py

#READY FOR MARKING

from A_V_calc import option1, option2, option3, option4

def test_option1():
    assert option1(5, 8) == 40
    
def test_option2():
    assert option2(2, 6) == 6
    
def test_option3():
    assert option3(3)== 254
    
def test_option4():
    assert option4(7)== 343
