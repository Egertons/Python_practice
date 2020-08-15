#进入第三章列表简介
liebiao=['dongruan','dyyy','xiaomi','meizu','jyyy']
print(liebiao)
liebiao[0]='daliandongruan'
print(liebiao)
liebiao.append('8777')
print(liebiao)
liebiao.insert(0,'zhanglin')
print(liebiao)
del liebiao[0]
ghhh=liebiao.pop()#将列表的最高项顶出，将其赋值至新列表ghhh
print(ghhh)
tyt=liebiao.pop(0)#指定栈顶项顶出。
print(tyt)
jihe=tyt+ghhh#列表间的相加减（内容部分）
print(jihe)
liebiao.append('daliandongruanxinxixueyuan')
print(liebiao)
liebiao.remove('dyyy')#remove函数对列表项进行删除。
print(liebiao)

print('\n')
print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
print('\n')
#强行隔断，代码实在太长了，没法在输出行中定义。
print(liebiao)
del liebiao
#del  一个列表后会把整个列表整体性一次性的删除。


#进入第四章操作列表
print('Just begin!')
pizza=['jiaozi','hundun','wareddy','lihtysDVFKgsdv']
print(pizza)
for zl in pizza:
    print('\n\t'+zl)
    print('I like the '+zl+'.\n\t')
print('item')
#复习结束
for value in range(1,5):
    print(value)
xin=list(range(1,66))#实际上打印到65。
print(xin)

hju=[]
for vyu in range(55,90,3):
    iuy=vyu**2
    hju.append(iuy)
    print(hju)#正三角形显示~

    
squares=[]
for value in range(1,11):
    squares.append(value**2)#事实证明append中什么都 能写 不只是能写‘***’
    print(squares)


min(squares)#最小函数
#私は张霖です。授業後の練習です。
for fg in range(1,21):
    print(fg)
#liebiao=list(range(1,1000001))
#for lb in liebiao:
#    print(lb)
#这玩意儿太费时间了~
kiu=[]
for ui in range(1,21,2):
    kiu.append(ui)
print(kiu)
kiy=[]
for qw in range(3,31,3):
    kiy.append(qw)
print(kiy)
lo=[]
for bn in range(1,11):
    hdd=bn**3
    lo.append(hdd)
print(lo)
le=[bw**3 for bw in range(1,11)]
print(le)
#以上练习都是一个意思，对range 语法的理解。
