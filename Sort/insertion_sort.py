'''
MIT License

Name cs225sp20_env Python Package
URL https://github.com/Xiwei-Wang/cs225sp20_env

Version 1.0
Creation Date 26 April 2020

Copyright(c) 2020 Instructors, TAs and Some Students of UIUC CS 225 SP20 ZJUI Course
Instructorts: Prof. Dr. Klaus-Dieter Schewe
TAs: Tingou Liang, Run Zhang, Enyi Jiang, Xiang Li
Group 1 Students: Shen Zheng, Haozhe Chen, Ruiqi Li, Xiwei Wang
Other Students: Zhongbo Zhu

Above all, due to academic integrity, students who will take UIUC CS 225 ZJUI Course
taught with Python later than Spring 2020 semester are NOT authorized with the access
to this package.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---------
File cs225sp20_env/Sort/insertion_sort.py
Version 1.0
'''
# %%
# for VS Code users
if __name__ != "cs225sp20_env.Sort.insertion_sort":
    import sys
    sys.path.append(__file__[:-len("cs225sp20_env/Sort/insertion_sort.py")])
# %%
# for PyCharm users
if __name__ != "cs225sp20_env.Sort.insertion_sort":
    import sys
    import os
    sys.path.append(os.getcwd())
# %%
from cs225sp20_env.List.PyList import PyList
from cs225sp20_env.List.SPyList import SPyList
from cs225sp20_env.List.DLinkedList import DLinkedList
from cs225sp20_env.List.LinkedList import LinkedList
# %%
def insertion_sort(l):
    l_out = PyList([], l.numItems)
    while l.numItems:
        now = l[l.numItems - 1]
        l.delete(l.numItems - 1)
        if l_out.numItems == 0:
            l_out.append(now)
        else:
            L = 0
            R = l_out.numItems - 1
            ans = l_out.numItems
            while L <= R:
                mid = int((L + R) / 2)
                if l_out[mid] > now:
                    ans = mid
                    R = mid - 1
                else:
                    L = mid + 1
            l_out.insert(ans, now)
    return l_out
