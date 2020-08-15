schools=['DNUI','NCHJ']
#这是一个列表，所表述的是一个学校的列表信息
for school in schools:
    if school !='jjjjj':
        print('没有这个jjjjj的列表信息')
    else:
        prnt('有信息~')
print('success~')




#复习部分(1.13重新复习前序所有部分）
#Hello World
print('\n\tHello World~')#你这个\n\t得写在字符引导串‘’的里面啊~



#正好趁这个机会读读以前的源码吧
#del  liebiao
liebiao=[kkk for kkk in range(2,99,2)]
print(liebiao)
del liebiao
#print(liebiao) //此时输出结果失败，则说明del直接一个列表后会把整个列表都删除。
