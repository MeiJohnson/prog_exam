import squareseqdigit


def test_squareseqdigit_1():
    assert squareseqdigit.squareSequenceDigit(1) == 1 , " squareSequenceDigit(1) == 1 " 
    
def test_squareseqdigit_2():
    assert squareseqdigit.squareSequenceDigit(2) == 4, " squareSequenceDigit(2) == 4 " 
    
def test_squareseqdigit_3():
    assert squareseqdigit.squareSequenceDigit(7) == 5, " squareSequenceDigit(7) == 5 " 
    
def test_squareseqdigit_4():
    assert squareseqdigit.squareSequenceDigit(12) == 6, " squareSequenceDigit(12) == 6 "
    
def test_squareseqdigit_5():
    assert squareseqdigit.squareSequenceDigit(17) == 0, " squareSequenceDigit(17) == 0 "
    
def test_squareseqdigit_6():
    assert squareseqdigit.squareSequenceDigit(27) == 9, " squareSequenceDigit(27) == 9 " 
