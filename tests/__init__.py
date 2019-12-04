import os

from git_processor import ROOT_PATH

TEST_PATH = os.path.join(ROOT_PATH, "tests")

TEST_STRING_PROJECTS = """project A/
   122	hero
   100	dog
    29	owl
     6	loco
     6	monkey
     3	coder
     1	spy

project B/
    12	dog
    10	owl
     5	owl2
     2	coder"""

TEST_LIST_PROJECTS = [
    'project A/\n   122\thero\n   100\tdog\n    29\towl\n     6\tloco\n     6\tmonkey\n     3\tcoder\n     1\tspy',
    'project B/\n    12\tdog\n    10\towl\n     5\towl2\n     2\tcoder']

TEST_DICT_PROJECTS = {'project A': [['hero', 122], ['dog', 100], ['owl', 29], ['loco', 6], ['monkey', 6], ['coder', 3],
                                    ['spy', 1]],
                      'project B': [['dog', 12], ['owl', 10], ['owl2', 5], ['coder', 2]]}

TEST_VALUES_PROJECTS = [('hero', 'dog', 'owl', 'loco', 'monkey', 'coder', 'spy'),
                        (122, 100, 29, 6, 6, 3, 1)]

TEST_DF_PROJECTS = """     name  project A  project B
0    hero      122.0        0.0
1     dog      100.0       12.0
2     owl       29.0       10.0
3    loco        6.0        0.0
4  monkey        6.0        0.0
5   coder        3.0        2.0
6     spy        1.0        0.0
7    owl2        0.0        5.0"""

TEST_COMPLEX_CDF_PROJECTS = """       name  project A  project B  project C
0       dog      100.0       12.0       98.0
1      hero      122.0        0.0        0.0
2     locom        6.0        0.0       26.0
3    monkey        6.0        0.0        0.0
4       owl       29.0       15.0        0.0
5       spy        1.0        0.0       53.0
6  thecoder        3.0        2.0        1.0"""

TEST_TOTAL_PROJECTS = """       name  total
0       dog  210.0
1      hero  122.0
2     locom   32.0
3    monkey    6.0
4       owl   44.0
5       spy   54.0
6  thecoder    6.0"""

TEST_PERCENTAGE_USER = """          total  total %
name                    
dog       210.0    44.30
hero      122.0    25.74
locom      32.0     6.75
monkey      6.0     1.27
owl        44.0     9.28
spy        54.0    11.39
thecoder    6.0     1.27"""

TEST_PERCENTAGE_USER_PROJECT = """          project B  total %
name                        
dog            12.0    41.38
hero            0.0     0.00
locom           0.0     0.00
monkey          0.0     0.00
owl            15.0    51.72
spy             0.0     0.00
thecoder        2.0     6.90"""

TEST_AVERAGE_USER = """          total  average
name                    
dog       210.0       70
hero      122.0       40
locom      32.0       10
monkey      6.0        2
owl        44.0       14
spy        54.0       18
thecoder    6.0        2"""

TEST_CONTRIBUTORS = """           contributors
project A             7
project B             3
project C             4"""

TEST_PERCENTAGE_PROJECT = """name         dog   hero  locom  monkey   owl   spy  thecoder  total  total %
project A  100.0  122.0    6.0     6.0  29.0   1.0       3.0  267.0    56.33
project B   12.0    0.0    0.0     0.0  15.0   0.0       2.0   29.0     6.12
project C   98.0    0.0   26.0     0.0   0.0  53.0       1.0  178.0    37.55
total      210.0  122.0   32.0     6.0  44.0  54.0       6.0  474.0   100.00"""

TEST_AVERAGE_PROJECT = """name         dog   hero  locom  monkey   owl   spy  thecoder  total  average
project A  100.0  122.0    6.0     6.0  29.0   1.0       3.0  267.0       33
project B   12.0    0.0    0.0     0.0  15.0   0.0       2.0   29.0        3
project C   98.0    0.0   26.0     0.0   0.0  53.0       1.0  178.0       22
total      210.0  122.0   32.0     6.0  44.0  54.0       6.0  474.0       59"""

TEST_FILTERED_DF = """        project A  project B
name                        
dog         100.0       12.0
owl          29.0       10.0
monkey        6.0        0.0"""
