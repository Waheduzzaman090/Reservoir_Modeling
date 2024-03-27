# -*- coding: utf-8 -*-
"""
Created on 21/02/2024

@author: % Md. Waheduzzaman Nouman
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
from binary_optimaizar import optimize
from binary_v2 import binary

from FOFT import prod_well_temp

file = 'C:\\Users\\USER\\Desktop\\TVS\Petrasim_reservoir_modeling\\hetaroginious\\FOFT'

time, pro_temp, inj_temp = prod_well_temp(file)

temp = pro_temp
data = {
        'average_ambient_temperature' : 29,
        'geofluid_temperature_at_wellhead' : 180.7,
        'geofluid_presure_at_wellhead' : 20,
        'silica_concentration_of_the_geofluid' : 853,
        'geofluid_mass_flow_rate' : 48,
        'geofluid_temperature_at_re_injunction_well' : 114,
        'working_fluid' : 'Isopentane',
        'turbine_isentropic_efficiency' : 75,
        'pump_isentropic_efficiency' : 75,
        'turbine_mechanical_efficiency' : 95,
        'pump_mechanical_efficiency' : 93,
        'equivalent_nacl_concentration' : 0,
        'PPT' : 10,  #Pinch_point_temp = PPT
        'G_fluid' : 'water',
        'Turbine_inlet_temp':0,
        'Turbine_inlet_pressure': 0,
        'ORC_fluid_flow_rate':0}
res = optimize(data)


#%%
opt_temp = res.X[0]
opt_pressure = res.X[1]
print(res.X,res.F)

data['Turbine_inlet_temp'] = opt_temp
data['Turbine_inlet_pressure'] = opt_pressure
result,T,P = binary(data)
data['ORC_fluid_flow_rate'] = result['Mass flowrate(kg/s)']
print('power: ',result['Net power(MW)'])

#%%
from binary_v2 import binary
net_work = []
eff = []
Tur_temp = []
m_wf = []
for i in range(len(time)):
    data['geofluid_temperature_at_wellhead'] = temp[i]
    result,T,P = binary(data,Turbine_in_temp = False)
    #print(result['Thermal efficiency(%)'])
    net_work.append(result['Net power(MW)'])
    eff.append(result["Thermal efficiency(%)"])
    Tur_temp.append(T[3]-273.15)
    m_wf.append(result["Mass flowrate(kg/s)"])



#%%
fig = plt.figure()
ax = fig.add_subplot(111)

net_energy = []
for t in range(len(time)):
    net_energy.append(sum(time[:t]*net_work[:t]*365*24)/1000000)

lns1 = ax.plot(time, temp, 'og', label = 'Temp.at Prod. Well Outlet')
lns2 = ax.plot(time,Tur_temp,'x',label = 'Temperature at Turbine Inlet')
ax2 = ax.twinx()
lns3 = ax2.plot(time, net_work, '-r', label = 'Net Power')
#ax3 = ax.twinx()
#lns4 = ax3.plot(time,net_energy,'.-',label = "Total Energy")
Unit = np.sum((np.asarray(net_work)*40/196))*365*24/1000 # Giga Unit
print('unit: ', Unit)

# added these three lines
lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=1)

ax.grid()
ax.set_xlabel("Time (years)")
ax2.set_ylabel(r"Net Power (MW)")
#ax3.set_ylabel(r"Net Enrgy (Giga Unit)")
#ax3.spines["right"].set_position(("axes", 1.2))
ax.set_ylabel(r"Temperature ($^\circ$C)")
plt.savefig('27-03-24_hetro_20C.png', dpi = 500,bbox_inches='tight')
plt.show()

#%%
#Hetaro 20C 505.17
#Hetaro 10C 537.22
#Homo 10C 324.58
#Homo 20C 304.81