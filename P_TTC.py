P_HT=float(input('enter the total price excluding tax : '))
if P_HT>200: 
 p_TTC=P_HT+P_HT*(0.20-0.15)
else:
 p_TTC=P_HT+P_HT*0.20
print(' the amount including tax :',p_TTC,"DH")