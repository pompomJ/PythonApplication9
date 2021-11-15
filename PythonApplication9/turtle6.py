from turtle import *

def branch(length):

    if length < 10:
        return
    forward(length) #length分進む
    left(30)
    branch(length/2) #左の枝を再帰的に描く
    right(60)
    branch(length/2) #右の枝を再帰的に描く
    left(30)
    forward(-length) #length分戻る

branch(50)

input()
