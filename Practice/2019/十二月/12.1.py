ui=[kkk for kkk in range(23,78,2)]
print(ui)
if ui:
    print('有值')
else:
    print('空')
#此前为复习阶段
ak={'color':'blue'}
print('I am favorite color is '+ ak['color']+'.')
ak['color']='yellow'#修改字典值
print(ak['color'])#验证
ak['num']=899
ak['nmhh']=89966
print(ak)
del ak['num']#删除字典对
print(ak)#验证结果



