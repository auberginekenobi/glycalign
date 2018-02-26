# jtsorren

from GlycanParser import *
# from OwensBeautifulAgglomerativeAlgorithm import *

def Test(name, expecteds, observed):
    '''
    Test suite for the Agglomerative algorithm. 
    This function loops through possible accepted 
    solutions and if an observed solution is viable - pass.
    '''
    failed = 0
    if len(expecteds) == 0:
        if expecteds == observed:
            print('Passed test {}, yay!'.format(name))
        else:
            print('Failed test {}. expected {} got {}, boo!'.format(name, expecteds, observed))
    else:
        for expected in expecteds:
            try:
                assert(expected == observed)
            except:
                failed += 1
        if failed == len(expecteds):
            print('Failed test {}. expected {} got {}, boo!'.format(name, expecteds, observed))
        else:
            print('Passed test {}, yay!'.format(name))
        
def TestOne():
    '''
    Empty Test
    '''
    fragments = []
    expecteds = []
    Test(1, expecteds, OwensBeautifulAgglomerativeAlgorithm(fragments))
    return

def TestTwo():
    '''
    Non-Overlapping Fragments
    '''
    fragments = [Glycan(['L-Fucp', 'D-Galp'], [{1: ('alpha', 1, 2)}, {0: ('alpha', 2, 1)}]), 
                 Glycan(['L-Fucp', 'D-GlcpNAc'], [{1: ('alpha', 1, 3)}, {0: ('alpha', 3, 1)}])]
    expecteds = [[Glycan(['L-Fucp', 'D-Galp'], [{1: ('alpha', 1, 2)}, {0: ('alpha', 2, 1)}]), 
                  Glycan(['L-Fucp', 'D-GlcpNAc'], [{1: ('alpha', 1, 3)}, {0: ('alpha', 3, 1)}])],
                 [Glycan(['L-Fucp', 'D-GlcpNAc'], [{1: ('alpha', 1, 3)}, {0: ('alpha', 3, 1)}]), 
                  Glycan(['L-Fucp', 'D-Galp'], [{1: ('alpha', 1, 2)}, {0: ('alpha', 2, 1)}])]]
    Test(2, expecteds, OwensBeautifulAgglomerativeAlgorithm(fragments))
    return

def TestThree():
    '''
    Identical Fragments
    '''
    fragments = [Glycan(['L-Fucp', 'D-Galp'], [{1: ('alpha', 1, 2)}, {0: ('alpha', 2, 1)}]), 
                 Glycan(['L-Fucp', 'D-Galp'], [{1: ('alpha', 1, 2)}, {0: ('alpha', 2, 1)}])]
    expecteds = [Glycan(['L-Fucp', 'D-Galp'], [{1: ('alpha', 1, 2)}, {0: ('alpha', 2, 1)}])]
    Test(3, expecteds, OwensBeautifulAgglomerativeAlgorithm(fragments))
    return

def TestFour():
    '''
    Linear Glycan
    '''
    fragments = [Glycan(['L-Fucp', 'D-GlcpNAc'], [{1: ('alpha', 1, 4)}, {0: ('alpha', 4, 1)}]), 
                 Glycan(['D-GlcpNAc', 'D-GlcpNAc'], [{1: ('beta', 1, 4)}, {0: ('beta', 4, 1)}]), 
                 Glycan(['D-GlcpNAc', 'D-GlcpNAc', 'D-GlcpNAc'], [{1: ('beta', 1, 4)}, {0: ('beta', 4, 1), 2: ('beta', 1, 4)}, {1: ('beta', 4, 1)}]), 
                 Glycan(['D-Manp', 'D-GlcpNAc'], [{1: ('alpha', 4, 1)}, {0: ('alpha', 1, 4)}])]
    expecteds = [Glycan(['L-Fucp', 'D-GlcpNAc', 'D-GlcpNAc', 'D-GlcpNAc', 'D-Manp'], [{1: ('alpha', 1, 4)}, {0: ('alpha', 4, 1), 2: ('beta', 1, 4)}, {1: ('beta', 4, 1), 3: ('beta', 1, 4)}, {2: ('beta', 4, 1), 4: ('alpha', 1, 4)}, {3: ('alpha', 4, 1)}])]
    Test(4, expecteds, OwensBeautifulAgglomerativeAlgorithm(fragments))
    return

def TestFive():
    '''
    Branched Glycan
    '''
    fragments = [Glycan(['L-Fucp', 'D-GlcpNAc', 'L-Fucp'], [{1: ('alpha', 1, 3)}, {0: ('alpha', 3, 1), 2: ('alpha', 1, 3)}, {1: ('alpha', 3, 1)}]), 
                 Glycan(['L-Fucp', 'D-GlcpNAc', 'D-Manp'], [{1: ('alpha', 3, 1)}, {0: ('alpha', 1, 3), 2: ('beta', 4, 1)}, {1: ('beta', 1, 4)}]), 
                 Glycan(['L-Fucp', 'D-Manp'], [{1: ('beta', 1, 1)}, {0: ('beta', 1, 1)}])]
    expecteds = [Glycan(['L-Fucp', 'D-GlcpNAc', 'L-Fucp', 'D-Manp', 'D-Manp'], [{1: ('alpha', 1, 3)}, {0: ('alpha', 3, 1), 2: ('alpha', 1, 3), 4: ('beta', 4, 1)}, {1: ('alpha', 3, 1), 3: ('beta', 1, 1)}, {2: ('beta', 1, 1)}, {1: ('beta', 1, 4)}])]
    Test(5, expecteds, OwensBeautifulAgglomerativeAlgorithm(fragments))
    return

#TestOne()
#TestTwo()
#TestThree()
#TestFour()
#TestFive()