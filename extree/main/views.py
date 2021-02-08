from django.shortcuts import render
from . import functions

def main_views(request):
    if request.method=="GET":
        return render(request,'main/index.html' ,{'htm':'' ,'expression':' . . . برسی'})

    elif request.method=='POST':

        expression=str(request.POST['search'])
        if expression=='' or expression.isspace():
            return render(request,'main/index.html' ,{'htm':'' ,'expression':'یک عبارت صحیح وارد کنید...'})
        x=functions.born_children(expression)
        htm=functions.htmlconvertor(x)
        htm=htm.replace('<ul></ul>','')
        posorder_expression=functions.postorder(x)
        preorder_expression=functions.preorder(x)
        inorder_expression=functions.inorder(x)

        return render(request,'main/index.html',{'htm':htm ,'expression':expression,'postorder':posorder_expression , 'preorder':preorder_expression, 'inorder':inorder_expression})
