from src import slope, pairpackaging, yint


x1 = float(input('Please Enter Your First X-Value:'))
x2 = float(input('Please Enter Your Second X-Value:'))
y1 = float(input('Please Enter Your First Y-Value:'))
y2 = float(input('Please Enter Your Second Y-Value:'))

if x2 == x1:
    print("Cannot Divide By Zero, Slope Unedfined")
    quit()


oper1 = slope.oper1(x2, x1)
oper2 = slope.oper1(y2, y1)
slope_final = slope.slope_final(oper1, oper2)
yint_final = yint.yint_multiply(slope_final, y1)
pair1 = pairpackaging.pair(x1,y1)
pair2 = pairpackaging.pair(x2,y2)


print('y = ' + str(slope_final) + 'x ' + str(yint_final))
print('Slope:' , slope_final)
print('Y-int:' , yint_final)
print('Ordered Pair 1:' , pair1)
print('Ordered Pair 2:' , pair2)
