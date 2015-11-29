# -*- coding: utf-8 -*-
#总的车辆
cars = 100

#每辆车的容量
space_in_a_car =4.0

#司机数量
drivers=30

#乘客数量
passengers=90

#空闲车辆
cars_not_driven=cars-drivers

#已开的车辆等于司机数量
cars_driven=drivers

#总的容量等于已开车的数量乘以每辆车的空间
carpool_capacity = cars_driven *space_in_a_car

#平均多少乘客坐一辆车
average_passengers_per_car=passengers/cars_driven

#打印车辆总数
print "There are",cars,"cars available."
#打印司机数量
print "There are only",drivers,"drivers avalible."
#打印空车数量
print "There will be",cars_not_driven ,"empty cars today."
#打印载客量
print "we can transport ",carpool_capacity ,"peple today."
#打印乘客数量
print "We  have ",passengers ,"to carpool today."
#打印平均每辆车的乘客数量
print "We need to put about",average_passengers_per_car,"in each car."