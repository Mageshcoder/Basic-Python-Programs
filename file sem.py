try:
   f=open("Magesh.txt","w")
   try:
      f.write("HAI GUYS THIS IS MAGESH...")
      print("NAME OF FILE...",f.name)
      print("CLOSED OR NOT...",f.closed)
      print("CURRENT MODE OF FILE....",f.mode)
      
   finally:
      print("GONNA CLOSE A FILE...")
      f.close()
      print("FILE CLOSED...")
except IOError:
      print("ERROR : FILE READING...")

a="MAGESH"
print(a,print(print(a,print(a)),print(print(a),a)))
