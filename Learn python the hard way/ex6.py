# -*- coding: utf-8 -*-
x ="There are %d types of people." %10
binary ="binary"
do_not ="don't"

#通过将变量放（）里面，实现通过格式化字符放入多个变量
y="Those who know %s and those who %s."%(binary ,do_not)

print x
print y

#字符串里面引用字符串，里面的字符串双引号变为单引号
print "I said :%r."%x
print "I also said:'%s'."% y

#变量
hilarious=False
joke_evalution ="Isn't that joke so funny?! %r"
print joke_evalution % hilarious

#通过‘+’实现字符串拼接
w="This is the left side of ..."
e="a string with a right side."
print w+e

