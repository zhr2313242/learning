# 导入sympy库
from sympy import *

# 定义符号变量x
x = symbols('x')
# 对tan(x)函数求导
r = diff(tan(x), x)
# 对tan(x)函数求不定积分
a = integrate(tan(x),x)
# 对tanh(x)函数在[0.1,0.5]求定积分
b = integrate(tanh(x),(x,0.1,0.5))

# 打印结果
print(r)
print(a)
print(b)
