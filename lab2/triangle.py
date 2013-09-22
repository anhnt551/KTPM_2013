def is_triangle(a,b,c):
    if(a<0)or(b<0)or(c<0):
        print "Phai nhap so duong"
    elif( (a + b) <= c)or((a+c)<=b)or((b+c)<=a):
        print "Khong phai la ba canh tam giac"
    elif((a==b)and(b==c)and(a==c)):
        print "la tam giac deu"
    elif((a==b)or(a==c)or(b==c)):
        if(((a*a+b*b)==c*c)or((a*a + c*c)==b*b)or((b*b + c*c) == a*a)):
			print "Tam giac vuong can"
        else:
			print "Tam giac can"
    elif(((a*a+b*b)==c*c)or((a*a + c*c)==b*b)or((b*b + c*c) == a*a)):
		print "Tam giac vuong"
    else:
        print "Tam giac thuong"
if __name__=="__main__":
    a=int(raw_input())
    b=int(raw_input())
    c=int(raw_input())
    is_triangle(a,b,c);
    
    
