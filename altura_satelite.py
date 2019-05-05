# Altura sobre la superficie Terrrestre para un Satélite
print("h=(((G*MT*T**2)/(4*pi**2))**(1/3))-RT")
print("Empieza código")
G=6.67e-11
MT=5.97e24
RT=6371e3
pi=3.1416
#temp = input("Entre el valor para t: ")
#=float(input("entre el valor para t: "));
T=float(input("entre el periodo T: "))
h=(((G*MT*T**2)/(4*pi**2))**(1/3))-RT
print("La altura del satélite para un periodo T es:", h)

T_1=float(input("entre el periodo T_1: "))
h_1=(((G*MT*T_1**2)/(4*pi**2))**(1/3))-RT
print("h_1 es:", h_1)

print("La diferencia de alturas dh")
dh=h-h_1
print("dh es:", dh)                                 
