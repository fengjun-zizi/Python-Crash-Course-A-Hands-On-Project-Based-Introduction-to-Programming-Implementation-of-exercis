python_glossary = {'字典' : '是一系列建值位' , '变量' : '每个变量都指向一个值'  , '字符串' : '是一系列字符串' , '数' : '表示可视化数据、储存信息等' , '浮点数' : '带有小数点的数' , 'keys' : '是字典中用于查找的部分' , 'Value' : '是与键相关联的数据' , 'Item' : ' 是一个完整的键值对。' }

for term, definition in python_glossary.items():
    print(f"{term}: {definition}")

for key in set(python_glossary.keys()) :
    print(f" keys : {key.title()}")

for value in set(python_glossary.values()) :
    print(f" value : {value.title()}")
