from django.shortcuts import render
from . import functions

def main_views(request):
    if request.method=="GET":
        return render(request,'main/index.html' ,{'htm':'' ,'expression':' . . . برسی'})

    elif request.method=='POST':
        try:
            expression=str(request.POST['search'])
            if expression=='' or expression.isspace():
                return render(request,'main/index.html' ,{'htm':'' ,'expression':'تعریف نشده'})
            x=functions.born_children(expression)
            htm=functions.htmlconvertor(x)
            htm=htm.replace('<ul></ul>','')
            posorder_expression=functions.postorder(x)
            preorder_expression=functions.preorder(x)
            inorder_expression=functions.inorder(x)
            height=functions.height(x)
            number_of_nodes=functions.number_of_nodes(x)

            return render(request,'main/index.html',{'htm':htm ,'expression':expression,'postorder':posorder_expression , 'preorder':preorder_expression, 'inorder':inorder_expression , 'height':height,'number_of_nodes':number_of_nodes})
        except:
            return render(request,'main/index.html' ,{'htm':'' ,'expression':'تعریف نشده'})
