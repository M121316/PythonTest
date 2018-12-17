class Magic(object):
	def __init__(self,name = 'pytohn'):   #初始化对象
		self.name = name
	def __str__(self):      #打印本类对象时自动调用
		return 'hello %s' %self.name	
	def __rerp__(self):   #解释器环境下自动调用
		return self.name
	def __call__(self):     #调用本类时，方法自动调用
		print( 'Magic name : %s' %self.name)


m = Magic()
print(m)
m()
print('*************************')
class Fib(object):
	count = 0        #类变量
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		'''for遍历第一部'''
		return self
	def __next__(self):
		'''for遍历第二步'''
		self.a,self.b = self.b, self.a+self.b
		if self.a>=100:
			raise StopIteration()   #这是一个异常
		Fib.count += 1
		return self.a
	def __len__(self):       #返回一个值
		return Fib.count

	def __getitem__(self,n):    # 索引和切片
		if isinstance(n,int):   # 索引：通过isinstance来判断类n的型
			a,b = 0,1
			while n>=0:
				a,b = b,a+b
				n -= 1
			return a
		if isinstance(n,slice):  # 切片：通过isinstance来判断n的类型 
			if n.start == None:    #slice 有start 和 stop 属性
				start == 0
			else :
				start = n.start
			if n.stop == None:    # 斐波纳切没有结束项
				return 'error'
			stop = n.stop
			l = []
			for i in range(start,stop):
				l.append(self[i])
			return l





f = Fib()
for i in f:   #
	print(i , end = ' ')
print()
print(len(f))   #是这样调用的

print('************************')
print(f[2])     # 用到索引时自动调用__geteitem__
print(f[2:8])   # 用到切片时自动调用__getitem__

print('*************************')
from enum import Enum,unique
@unique            # 防止枚举变量重复
class Menu(Enum):  # 枚举变量不可变
	INSERT = 1
	DEL = 2
	CHOISE = 3
	FIND = 4
	#SHOW = 4


print(Menu.INSERT)
print(Menu.INSERT.value)
# Menu.INSERT.value = '5' 执行出错，变量不可变
















