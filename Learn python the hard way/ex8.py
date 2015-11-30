# -*- coding: utf-8 -*-
formatter ="%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True ,False ,True ,False )
print formatter %(formatter ,formatter ,formatter ,formatter )
print formatter %(
    "I had this thing.",
    "That you could type up tight.",
    "But it didn't sing.", #  因为这句话中含有单引号，故打印出来后为双引号
    "So i said goodnight."

)