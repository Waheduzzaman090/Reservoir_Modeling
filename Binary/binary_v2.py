# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:19:50 2024

@author: Md. Waheduzzaman Nouman
"""


import numpy as np
import ThermoProperty as TP
import math
import pinch

Temp = np.zeros(9)
Pressure = np.zeros(9)
Enthlpy = np.zeros(9)
Entropy = np.zeros(9)


def enthalpy(T, m):
    # m is NaCl molality, Maximum value for m is 2, min = 0
    a = [
        [9633.6, -4080, 286.49],
        [166.58, 68.577,-4.6856],
        [-0.90963,-0.36524,0.24966*10**-1],
        [0.17965*10**-2,0.71924*10**-3,-0.49*10**-4]
    ]

    Q = 0
    for i in range(0,4):
        for j in range(0,3):
            Q = Q + a[i][j] * T**i * m**j

    delh = (4.184 / (1000 + 58.44 * m)) * Q
    x1 = 1000 / (1000 + 58.44 * m)  # Mass fraction of water
    x2 = 58.44 * m / (1000 + 58.44 * m)  # Mass fraction of NaCl
    Enthlpy[6] = 0.12453 * 10 ** -4 * T ** 3 - 0.45137 * 10 ** -2 * T ** 2 + 4.81155 * T - 29.578  # Specific enthalpy of water in kJ/kg
    h2 = (-0.83624 * 10 ** -3 * T ** 3 + 0.16792 * T ** 2 - 25.9293 * T) * (4.184 / 58.44)  # Specific enthalpy of NaCl in kJ/kg
    h_brine = Enthlpy[6] * x1 + h2 * x2 + m * delh  # Specific enthalpy of brine in kJ/kg
    return h_brine


def binary(Data,Turbine_in_temp = True): #Temperature in C and pressure in Pa
    #data given
    average_ambient_temperature = Data['average_ambient_temperature']
    geofluid_temperature_at_wellhead =  Data['geofluid_temperature_at_wellhead']
    geofluid_presure_at_wellhead = Data['geofluid_presure_at_wellhead']
    silica_concentration_of_the_geofluid = Data['silica_concentration_of_the_geofluid']
    geofluid_mass_flow_rate = Data['geofluid_mass_flow_rate']
    geofluid_temperature_at_re_injunction_well = Data['geofluid_temperature_at_re_injunction_well']
    working_fluid = Data['working_fluid']
    turbine_isentropic_efficiency = Data['turbine_isentropic_efficiency']
    pump_isentropic_efficiency = Data['pump_isentropic_efficiency']
    turbine_mechanical_efficiency = Data['turbine_mechanical_efficiency']
    pump_mechanical_efficiency = Data['pump_mechanical_efficiency']
    equivalent_nacl_concentration = Data['equivalent_nacl_concentration']
    PPT = Data['PPT'] #Pinch_point_temp = PPT
    G_fluid = Data['G_fluid']
    
    
    
    fluid = working_fluid
    T_amb = average_ambient_temperature + 273
    n_tur = turbine_isentropic_efficiency/100
    n_pump = pump_isentropic_efficiency/100
    n_tur_m = turbine_mechanical_efficiency/100
    n_pump_m = pump_mechanical_efficiency
    
    subcool_liquid = False #this is use for checking turbine inlet state
    
    try:
       
        #POINT 6
        Temp[6] = geofluid_temperature_at_wellhead+273.15
        Pressure[6] = geofluid_presure_at_wellhead*1e5
        C = silica_concentration_of_the_geofluid
        nacl_c = equivalent_nacl_concentration
        m_g = geofluid_mass_flow_rate
        
        
        #POINT 8
        if geofluid_temperature_at_re_injunction_well == 0:
            # C_max = C_g/SSI
            C_max = C/ 2
            Temp[8] = (273.15*math.log(C_max, 10)-503.638)/(4.52-math.log(C_max, 10))
        else:
            Temp[8] = geofluid_temperature_at_re_injunction_well+273.15
        
        
        
        if G_fluid == 'water':
            if Pressure[6] == '':
                Enthlpy[6] = TP.H_TQ(Temp[6],0,'water')
                Enthlpy[8] = TP.H_TQ(Temp[8],0,'water')
            else:
                Enthlpy[6] = TP.H_TP(Temp[6],Pressure[6],'water')
                Enthlpy[8] = TP.H_TP(Temp[8],Pressure[6],'water')
        else:
            Enthlpy[6] = enthalpy(Temp[6],nacl_c)*1000
            Enthlpy[8] = enthalpy(Temp[8],nacl_c)*1000
        
                
        #POINT 5
        x8 = 0
        Temp[5]= T_amb + 10
        Pressure[5] = TP.P_TQ(Temp[5],x8,fluid)
        Enthlpy[5] = TP.H_TQ(Temp[5],x8,fluid)
        Entropy[5] = TP.S_TQ(Temp[5],x8,fluid)

        #POINT 1
        Pressure[1] = Data['Turbine_inlet_pressure']
        s_1_isen = Entropy[5]
        Enthlpy1_isen = TP.H_PS(Pressure[1],s_1_isen,fluid)
        Enthlpy[1] = Enthlpy[5] + (Enthlpy1_isen-Enthlpy[5])/n_pump   #isentropic effeciency of pump n = (h_out_isen-h_in)/(h_out-h_in)
        Entropy[1] = TP.S_PH(Pressure[1],Enthlpy[1],fluid)
        Temp[1] = TP.T_PH(Pressure[1],Enthlpy[1],fluid) 
        
        #POINT 3 
        if Turbine_in_temp == True:    
            Temp[3] = Data['Turbine_inlet_temp'] +273.15
            Pressure[3] = TP.P_TQ(Temp[3],1,fluid)
            Temp3_cri = TP.T_cri(fluid)
            
            if Data['Turbine_inlet_pressure'] == Pressure[3]:
                Enthlpy[3] = TP.H_TQ(Temp[3],1,fluid)
                Entropy[3] = TP.S_TQ(Temp[3],1,fluid)
            if Data['Turbine_inlet_pressure']  > Pressure[3]:
                Pressure[3] = Data['Turbine_inlet_pressure']
                Enthlpy[3] = TP.H_TP(Temp[3],Pressure[3],fluid)
                Entropy[3] = TP.S_TP(Temp[3],Pressure[3],fluid)
            else:
                subcool_liquid = True
        else:
           
            Enthlpy[3] = Enthlpy[1]+m_g*(Enthlpy[6]-Enthlpy[8])/Data['ORC_fluid_flow_rate']
           
            Pressure[3] = Data['Turbine_inlet_pressure']
            
            Temp[3] = TP.T_PH(Pressure[3],Enthlpy[3],fluid)
            
            Entropy[3] = TP.S_TP(Temp[3],Pressure[3],fluid)
            
            
    

        
        #POINT 4
        Pressure[4] = Pressure[5]
        Entropy4_isen = Entropy[3]
        Enthlpy4_isen = TP.H_PS(Pressure[4],Entropy4_isen,fluid)
        Enthlpy[4] = Enthlpy[3] - n_tur*(Enthlpy[3]-Enthlpy4_isen)  #isentropic effeciency of turbine n = (h_in - h_out)/(h_in-h_out_isen)
        Entropy[4] = TP.S_PH(Pressure[4],Enthlpy[4],fluid)
        Temp[4] = TP.T_PH(Pressure[4],Enthlpy[4],fluid)
        
        
        
        
        #POINT 2
        Pressure[2] = Pressure[1]
        x2 = 0
        Temp[2] = TP.T_PQ(Pressure[2],x2,fluid)
        Enthlpy[2] = TP.H_PQ(Pressure[2],x2,fluid)
        Entropy[2] = TP.S_PQ(Pressure[2],x2,fluid)

        #mass flowrate of WF
        Q_g = m_g*(Enthlpy[6]-Enthlpy[8])
        
        if Data['ORC_fluid_flow_rate'] == 0:
            m_wf = Q_g/(Enthlpy[3]-Enthlpy[1])
            print(m_wf)
        else:
            m_wf = Data['ORC_fluid_flow_rate']
        
        W_tur_in = m_wf*(Enthlpy[3]-Enthlpy[4])
        W_tur_out = n_tur_m*W_tur_in
        W_pump_out = m_wf*(Enthlpy[1]-Enthlpy[5])
        W_pump_in = W_pump_out/n_pump_m
        W_net = W_tur_out - W_pump_in

        n = W_net/Q_g
        
        pin = pinch.Pinch_check(Pressure[6], Temp[6], m_g,G_fluid, Pressure[1], Temp[1], m_wf,fluid, Temp[8], PPT)

        # if (Temp[3] >  Temp3_cri-15) or (Temp[3]> geofluid_temperature_at_wellhead+273.15-20) or (Pressure[3]>3000000) or pin == 0 or subcool_liquid:
        #     #print((Temp[3] >  Temp3_cri-15) , (Temp[3]> geofluid_temperature_at_wellhead+273.15-20) , (Pressure[3]>3000000) , pin == 0,subcool_liquid,pin)
        #     W_net = 0
        #     n = 0
        #     result = {
        #                    "Heat In(MW)":Q_g/1e6,
        #                    "Turbine Power(MW)": W_tur_out/1e6,
        #                    "Pump Power(MW)": W_pump_in/1e6,
        #                    "Net power(MW)": W_net/1e6,
        #                    "Thermal efficiency(%)": n*100,
        #                    "Mass flowrate(kg/s)": m_wf
        #                    }
        #     return result, Temp, Pressure
        # else:
        result = {
                          "Heat In(MW)":Q_g/1e6,
                          "Turbine Power(MW)": W_tur_out/1e6,
                          "Pump Power(MW)": W_pump_in/1e6,
                          "Net power(MW)": W_net/1e6,
                          "Thermal efficiency(%)": n*100,
                          "Mass flowrate(kg/s)": m_wf
                       }
        
        return result, Temp, Pressure
        
    except:
        n = 0
        W_net = 0
        Q_g = 0
        W_tur_out = 0
        W_pump_in = 0
        m_wf = 0
        result = {
                           "Heat In(MW)":Q_g/1e6,
                           "Turbine Power(MW)": W_tur_out/1e6,
                           "Pump Power(MW)": W_pump_in/1e6,
                           "Net power(MW)": W_net/1e6,
                           "Thermal efficiency(%)": n*100,
                           "Mass flowrate(kg/s)": m_wf
                       }
        return result, Temp, Pressure
    


# data = {
#         'average_ambient_temperature' : 29.1,
#         'geofluid_temperature_at_wellhead' :  180.7,
#         'geofluid_presure_at_wellhead' : 10.2,
#         'silica_concentration_of_the_geofluid' : 853,
#         'geofluid_mass_flow_rate' : 48,
#         'geofluid_temperature_at_re_injunction_well' : 114,
#         'working_fluid' : 'Isopentane',
#         'turbine_isentropic_efficiency' : 75,
#         'pump_isentropic_efficiency' : 75,
#         'turbine_mechanical_efficiency' : 95,
#         'pump_mechanical_efficiency' : 93,
#         'equivalent_nacl_concentration' : 0,
#         'PPT' : 10,  #Pinch_point_temp = PPT
#         'G_fluid' : 'water',
#         'Turbine_inlet_temp':0,
#         'Turbine_inlet_pressure':160,
#         'ORC_fluid_flow_rate':30e5}
# R,T,P = binary(data)






