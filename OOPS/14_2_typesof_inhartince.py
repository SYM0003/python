''' types of inhertance'''

# # ::::::::::::::::::::::::::
# # single inharitance
# # multi level inharitance
# # hirachical inharitance
# # multiple inharitance
# # hybrid inharitance
# # cyclic inharitance(not supported in any programing language)





# # single inharitance
# # this is simplest form of inhartance where one class inharite with
# # with only one class.
# class P:
#     pass
# class C(P):
#     pass

# # in the above example class P is inharited by the class C,it means
# # class C can access the members of P class.


# # multilevel inharitance
# # in multilevel inharitance one class access the member of multiple class
# # one by one
# # i.e:
# class P:
#     pass
# class C(P):
#     pass
# class CC(C):
#     pass

# # in the above example the class Ccan access the members of class P and 
# # class CC can access the member of class Pas well as class C.




# # hirachical inharitance
# # in hirachical inharitace 2 or more class inharite single class only
# # means one class has 2 or more child class

class P:
    pass
class C1(P):
    pass
class C2(P):
    pass


# # # MRO ALGORITHM:
# mro of class a
# class_name.mro()
class A:
    pass
class B:
    pass
class C:
    pass
class X(B,C):
    pass
class Y(C,A):
    pass
class Z(A,B):
    pass

class P(X,Y):
    pass
    
class Q(Y,Z,P):
    pass
    #mro(a)->ao
    #mro(b)->bo
    #mro(c)->co
    #mro(x)=x+merge(mro(b),mro(c),bc)=xbco
    #mro(y)=y+merge(mro(c),mro(a),ca)=ycao
    #mro(z)=x+merge(mro(a),mro(b),ab)=zabo
    #mro(p)=p+merge(mro(x),mro(y),xy)=pxbycao
    #mro(q)=q+merge(mro(x),mro(y),mro(p),xyp)=q+merge(xbco,ycao,pxbycao,xyp)=q
     
print(P.mro())