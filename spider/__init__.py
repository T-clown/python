import re

html = '''
<h1> test1 </h1>
<h1> test2 </h1>
<h1> test3 </h1>
'''
content = re.findall('<h1>(.*?)</h1>', html)
content2 = re.findall('<h1>(?:.*?)</h1>', html)

print(content)
print(content2)
