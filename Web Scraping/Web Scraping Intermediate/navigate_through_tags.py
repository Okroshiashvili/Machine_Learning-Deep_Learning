"""
Created on Sun Mar 31 2019

@author: Nodar Okroshiashvili
"""



from bs4 import BeautifulSoup


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# Directly access p tag by its name
# We know that this gives only first occurance of tag
title = soup.title

p = soup.p


print(p)
print(title)