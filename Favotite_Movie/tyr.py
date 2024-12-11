# trash bin

# make a file to store th deleted once 
# make another list to store them 
# empty after 30 days

x = {'ask':
     {'year': '2001',
      'director' : 'kar',
      'rating': '9'
     },
    'bos ev':
     {'year': '1990',
      'director' : 'kim',
      'rating': '9'
     }
}
delete = input('movie delete').strip()
d = {}
if delete in x:
    d[delete] = x.pop(delete)
    
print(x)
print(d)



