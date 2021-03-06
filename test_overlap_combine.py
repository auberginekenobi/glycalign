# -*- coding: utf-8 -*-
'''
Test suite for
function overlap_score
author Owen Chapman auberginekenobi
2/19/2018
'''

from simple_test import test
from GlycanParser import Glycan
from overlap_score_fast import overlap_score
from agglomerator import __overlap_combine__ as overlap_combine

def test1():
    '''
    Two small glycans
    '''
    #https://glytoucan.org/Structures/Glycans/G00055MO
    #https://glytoucan.org/Structures/Glycans/G00065MO
    lactosamine="beta-D-Galp-(1->4)-beta-D-GlcpNAc(1->"
    a=Glycan(lactosamine)
    VIM="alpha-D-NeupAc-(2->3)-beta-D-Galp-(1->4)-beta-D-GlcpNAc(1->"
    b=Glycan(VIM)
    s,o=overlap_score(a,b)
    c = overlap_combine(a,b,o.pop())
    test(1,b,c)

def test2():
    '''
    Combining two non-subtree glycans
    https://glytoucan.org/Structures/Glycans/G00053MO
    https://glytoucan.org/Structures/Glycans/G00047MO
    https://glytoucan.org/Structures/Glycans/G00065MO
    '''
    sialyl_lewis_a = "alpha-D-NeupAc-(2->3)-beta-D-Galp-(1->3)[alpha-L-Fucp-(1->4)]-beta-D-GlcpNAc(1->"
    lewis_a = "beta-D-Galp-(1->3)[alpha-L-Fucp-(1->4)]-?-D-GlcpNAc(1->"
    notVIM = "alpha-D-NeupAc-(2->3)-beta-D-Galp-(1->3)-beta-D-GlcpNAc(1->"
    a=Glycan(sialyl_lewis_a)
    b=Glycan(lewis_a)
    c=Glycan(notVIM)
    s,o=overlap_score(b,c)
    #print(len(b),len(c),s)
    d=overlap_combine(b,c,o.pop())
    #s,o = overlap_score(a,d)
    #print(len(a), len(d), s)


    test(2,a,d)

test1()
test2()