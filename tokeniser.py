import sys
 
text = sys.stdin.readlines() 
for i in range(0, len(text)):
    line = text[i].strip()
    if line == "":
        continue
    print("# sent_id = ",i+1,"\n"+"# text = ", line)
    token_id = 1
    punctuation = [".", ",", "?", "!", ":", ";"]
    newline1=line.replace("с. ш.","&&&&")
    newline2=newline1.replace("з. д.","////")
    for hats in punctuation:
            newline2 = newline2.replace(hats, " " + hats)
    tokens = newline2.split(" ")
    for token in tokens:
        token=token.replace("&&&&", "с. ш. ")
        token=token.replace("////","з. д. ")
        print("%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_" % (token_id, token))
        token_id = token_id+1
    print()


#for i in range(0, 2):
     	#line = text[i]

	#print("# sent_id =",i+1,"\n","#text=",line)
	#k=line.replace(" ","\n")
	#print(k)

      
	#line = line.replace( ' . ', ' )
	#index = index + 1 
	#tokens = line.split (' ')
	
	