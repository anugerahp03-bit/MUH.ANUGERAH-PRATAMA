print (" ============== IS ")
a =5
b =5
print ("Nilai a =’,a ,’Identitas =",hex (id( a ) ) )
print ("Nilai b =’,b ,’Identitas =",hex (id( b ) ) )
hasil = a is b
print ("a is b = ", hasil )

a =5
b =6
print ("Nilai a =’,a ,’Identitas =",hex (id( a ) ) )
print ("Nilai b =’,b ,’Identitas =",hex (id( b ) ) )
hasil = a is b

print ("a is b = ", hasil )

print (" ============== IS NOT ")
a =5
b =5
print ("Nilai a =’,a ,’Identitas =",hex (id( a ) ) )
print ("Nilai b =’,b ,’Identitas =",hex (id( b ) ) )
hasil = a is not b
print ("a is not b = ", hasil )

a =5
b =6
print ("Nilai a =’,a ,’Identitas =",hex (id( a ) ) )
print ("Nilai b =’,b ,’Identitas =",hex (id( b ) ) )
hasil = a is not b
print ("a is not b = ", hasil )
