# sample code 
import re

content= ['hello Judy, you are invited to party on 22.04.2021',
          'hey Agatha, you are invited to party on 22.04.2021',
          'hi Chris, you are invited to party on 22.04.2021',
          ' let\'s celebrate World Earth day '
          ]

p0 = re.compile(r'^(\S+)\s+(?P<name>(\w+)),\s+((\w+|\s+)*)(?:22.04.2021)$')

invitee = []
for i in content:
    m = p0.search(i)
    if m:
        var = (m.group('name'))
        invitee.append(var)
    

print('invitees --', invitee)
