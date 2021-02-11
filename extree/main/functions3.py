answer_string=''
class node():
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None
    def __str__(self):
        return self.value

def what_is_this(char):
    if char.isalpha() or char.isnumeric():
        return ('operation',None)
    elif char=='(':
        return ('openbraket',None)
    elif char ==')':
        return ('closebraket',None)
    else:
        validation={'+':0,'-':0,'*':1,'/':1,'^':2 ,'!':3 }
        return ('operator',validation[char])

def born_children(ex):
    #shart khateme 
    if len(ex)==1:
        return node(ex)

    counter=0
    pointer=['300',None,'index']
    close_count=sum([i for (i,x) in enumerate(list(ex[1:-1])) if x == ")"])
    opencount=sum([i for (i,x) in enumerate(list(ex[1:-1])) if x == "("])

    if ex[0]=='(' and ex[-1]==')' and ex[1:-1].count(')')==ex[1:-1].count('(') and close_count>=opencount :

        ex=ex[1:-1]

    if ex[0]=='!':
        x=node(ex[0])
        x.rchild=born_children(ex[1:])
        return x
    print(ex)
    for (index,char) in enumerate(ex):
        temp=what_is_this(char)

        if temp[0]=='operator' and int(temp[1])<=int(pointer[0]) and counter==0:
            pointer[0]=temp[1]
            pointer[1]=char
            pointer[2]=index

        elif temp[0]=='openbraket':
            counter=counter+1
            

        elif temp[0]=='closebraket':
            counter=counter-1
        

    root=node(pointer[1])
    root.lchild=(born_children(ex[:int(pointer[2])]))
    root.rchild=(born_children(ex[int(pointer[2])+1:]))
    
    return root

def postorder(x):
    answer_string =''
    if x==None:
        return ''
    else:
        answer_string +=postorder(x.lchild)
        answer_string +=postorder(x.rchild)
        answer_string+=str(x.value)
    
    return answer_string

def preorder(x):
    if x==None:
        return ''
    else:
        string=str(x.value)
        string+=preorder(x.lchild)
        string+=preorder(x.rchild)
    
    return string

def inorder(x):
    if x==None:
        return ''
    else:
        string=inorder(x.lchild)
        string+=str(x.value)
        string+=inorder(x.rchild)
    
    return string


def height(x):
    counter=-1
    if x==None:
        return -1
    else:
        counter=max(height(x.lchild),counter)
        counter=max(height(x.rchild),counter)
    return counter+1


def dictionary_of_childrens(x):
    if x==None:
        return None
    else:
        valdict={x.value:''}
        dict1={'lchild':None,'rchild':None}
        dict1['lchild']=dictionary_of_childrens(x.lchild)
        dict1['rchild']=dictionary_of_childrens(x.rchild)
        valdict[x.value]=dict1
        return valdict

# def dictionary_to_childs(dic:dict):

def htmlconvertor(x):
    string=''
    if x==None:
        return ''
    else:
        string= string +'<li>'
        string=string+'<span>'+str(x.value)+'</span>'
        string=string+'<ul>'
        string=string+str(htmlconvertor(x.lchild))
        string=string+htmlconvertor(x.rchild)
        string=string+'</ul>'
        string=string+'</li>'
    return string  

x=born_children('a+b')
                 

            
# print(htmlconvertor(x))
print(postorder(x))

# <li>+<ul><li>x</li><li>y</li></ul></li>



    
