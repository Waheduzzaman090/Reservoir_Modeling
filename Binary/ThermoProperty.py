"""
Created on Sun Dec  1 00:54:18 2019

@author: Md. Waheduzzman Nouman
"""

import CoolProp.CoolProp as CP

def D_HP(H,P,fluid):
    D = CP.PropsSI('D','H',H,'P',P,fluid)
    return D
def D_HQ(H,Q,fluid):
    D = CP.PropsSI('D','H',H,'Q',Q,fluid)
    return D
def D_HS(H,S,fluid):
    D = CP.PropsSI('D','H',H,'S',S,fluid)
    return D
def D_HT(H,T,fluid):
    D = CP.PropsSI('D','H',H,'T',T,fluid)
    return D
def D_HU(H,U,fluid):
    D = CP.PropsSI('D','H',H,'U',U,fluid)
    return D
def D_PH(P,H,fluid):
    D = CP.PropsSI('D','P',P,'H',H,fluid)
    return D
def D_PQ(P,Q,fluid):
    D = CP.PropsSI('D','P',P,'Q',Q,fluid)
    return D
def D_PS(P,S,fluid):
    D = CP.PropsSI('D','P',P,'S',S,fluid)
    return D
def D_PT(P,T,fluid):
    D = CP.PropsSI('D','P',P,'T',T,fluid)
    return D
def D_PU(P,U,fluid):
    D = CP.PropsSI('D','P',P,'U',U,fluid)
    return D
def D_QH(Q,H,fluid):
    D = CP.PropsSI('D','Q',Q,'H',H,fluid)
    return D
def D_QP(Q,P,fluid):
    D = CP.PropsSI('D','Q',Q,'P',P,fluid)
    return D
def D_QS(Q,S,fluid):
    D = CP.PropsSI('D','Q',Q,'S',S,fluid)
    return D
def D_QT(Q,T,fluid):
    D = CP.PropsSI('D','Q',Q,'T',T,fluid)
    return D
def D_QU(Q,U,fluid):
    D = CP.PropsSI('D','Q',Q,'U',U,fluid)
    return D
def D_SH(S,H,fluid):
    D = CP.PropsSI('D','S',S,'H',H,fluid)
    return D
def D_SP(S,P,fluid):
    D = CP.PropsSI('D','S',S,'P',P,fluid)
    return D
def D_SQ(S,Q,fluid):
    D = CP.PropsSI('D','S',S,'Q',Q,fluid)
    return D
def D_ST(S,T,fluid):
    D = CP.PropsSI('D','S',S,'T',T,fluid)
    return D
def D_SU(S,U,fluid):
    D = CP.PropsSI('D','S',S,'U',U,fluid)
    return D
def D_TH(T,H,fluid):
    D = CP.PropsSI('D','T',T,'H',H,fluid)
    return D
def D_TP(T,P,fluid):
    D = CP.PropsSI('D','T',T,'P',P,fluid)
    return D
def D_TQ(T,Q,fluid):
    D = CP.PropsSI('D','T',T,'Q',Q,fluid)
    return D
def D_TS(T,S,fluid):
    D = CP.PropsSI('D','T',T,'S',S,fluid)
    return D
def D_TU(T,U,fluid):
    D = CP.PropsSI('D','T',T,'U',U,fluid)
    return D
def D_UH(U,H,fluid):
    D = CP.PropsSI('D','U',U,'H',H,fluid)
    return D
def D_UP(U,P,fluid):
    D = CP.PropsSI('D','U',U,'P',P,fluid)
    return D
def D_UQ(U,Q,fluid):
    D = CP.PropsSI('D','U',U,'Q',Q,fluid)
    return D
def D_US(U,S,fluid):
    D = CP.PropsSI('D','U',U,'S',S,fluid)
    return D
def D_UT(U,T,fluid):
    D = CP.PropsSI('D','U',U,'T',T,fluid)
    return D
def H_DP(D,P,fluid):
    H = CP.PropsSI('H','D',D,'P',P,fluid)
    return H
def H_DQ(D,Q,fluid):
    H = CP.PropsSI('H','D',D,'Q',Q,fluid)
    return H
def H_DS(D,S,fluid):
    H = CP.PropsSI('H','D',D,'S',S,fluid)
    return H
def H_DT(D,T,fluid):
    H = CP.PropsSI('H','D',D,'T',T,fluid)
    return H
def H_DU(D,U,fluid):
    H = CP.PropsSI('H','D',D,'U',U,fluid)
    return H
def H_PD(P,D,fluid):
    H = CP.PropsSI('H','P',P,'D',D,fluid)
    return H
def H_PQ(P,Q,fluid):
    H = CP.PropsSI('H','P',P,'Q',Q,fluid)
    return H
def H_PS(P,S,fluid):
    H = CP.PropsSI('H','P',P,'S',S,fluid)
    return H
def H_PT(P,T,fluid):
    H = CP.PropsSI('H','P',P,'T',T,fluid)
    return H
def H_PU(P,U,fluid):
    H = CP.PropsSI('H','P',P,'U',U,fluid)
    return H
def H_QD(Q,D,fluid):
    H = CP.PropsSI('H','Q',Q,'D',D,fluid)
    return H
def H_QP(Q,P,fluid):
    H = CP.PropsSI('H','Q',Q,'P',P,fluid)
    return H
def H_QS(Q,S,fluid):
    H = CP.PropsSI('H','Q',Q,'S',S,fluid)
    return H
def H_QT(Q,T,fluid):
    H = CP.PropsSI('H','Q',Q,'T',T,fluid)
    return H
def H_QU(Q,U,fluid):
    H = CP.PropsSI('H','Q',Q,'U',U,fluid)
    return H
def H_SD(S,D,fluid):
    H = CP.PropsSI('H','S',S,'D',D,fluid)
    return H
def H_SP(S,P,fluid):
    H = CP.PropsSI('H','S',S,'P',P,fluid)
    return H
def H_SQ(S,Q,fluid):
    H = CP.PropsSI('H','S',S,'Q',Q,fluid)
    return H
def H_ST(S,T,fluid):
    H = CP.PropsSI('H','S',S,'T',T,fluid)
    return H
def H_SU(S,U,fluid):
    H = CP.PropsSI('H','S',S,'U',U,fluid)
    return H
def H_TD(T,D,fluid):
    H = CP.PropsSI('H','T',T,'D',D,fluid)
    return H
def H_TP(T,P,fluid):
    H = CP.PropsSI('H','T',T,'P',P,fluid)
    return H
def H_TQ(T,Q,fluid):
    H = CP.PropsSI('H','T',T,'Q',Q,fluid)
    return H
def H_TS(T,S,fluid):
    H = CP.PropsSI('H','T',T,'S',S,fluid)
    return H
def H_TU(T,U,fluid):
    H = CP.PropsSI('H','T',T,'U',U,fluid)
    return H
def H_UD(U,D,fluid):
    H = CP.PropsSI('H','U',U,'D',D,fluid)
    return H
def H_UP(U,P,fluid):
    H = CP.PropsSI('H','U',U,'P',P,fluid)
    return H
def H_UQ(U,Q,fluid):
    H = CP.PropsSI('H','U',U,'Q',Q,fluid)
    return H
def H_US(U,S,fluid):
    H = CP.PropsSI('H','U',U,'S',S,fluid)
    return H
def H_UT(U,T,fluid):
    H = CP.PropsSI('H','U',U,'T',T,fluid)
    return H
def P_DH(D,H,fluid):
    P = CP.PropsSI('P','D',D,'H',H,fluid)
    return P
def P_DQ(D,Q,fluid):
    P = CP.PropsSI('P','D',D,'Q',Q,fluid)
    return P
def P_DS(D,S,fluid):
    P = CP.PropsSI('P','D',D,'S',S,fluid)
    return P
def P_DT(D,T,fluid):
    P = CP.PropsSI('P','D',D,'T',T,fluid)
    return P
def P_DU(D,U,fluid):
    P = CP.PropsSI('P','D',D,'U',U,fluid)
    return P
def P_HD(H,D,fluid):
    P = CP.PropsSI('P','H',H,'D',D,fluid)
    return P
def P_HQ(H,Q,fluid):
    P = CP.PropsSI('P','H',H,'Q',Q,fluid)
    return P
def P_HS(H,S,fluid):
    P = CP.PropsSI('P','H',H,'S',S,fluid)
    return P
def P_HT(H,T,fluid):
    P = CP.PropsSI('P','H',H,'T',T,fluid)
    return P
def P_HU(H,U,fluid):
    P = CP.PropsSI('P','H',H,'U',U,fluid)
    return P
def P_QD(Q,D,fluid):
    P = CP.PropsSI('P','Q',Q,'D',D,fluid)
    return P
def P_QH(Q,H,fluid):
    P = CP.PropsSI('P','Q',Q,'H',H,fluid)
    return P
def P_QS(Q,S,fluid):
    P = CP.PropsSI('P','Q',Q,'S',S,fluid)
    return P
def P_QT(Q,T,fluid):
    P = CP.PropsSI('P','Q',Q,'T',T,fluid)
    return P
def P_QU(Q,U,fluid):
    P = CP.PropsSI('P','Q',Q,'U',U,fluid)
    return P
def P_SD(S,D,fluid):
    P = CP.PropsSI('P','S',S,'D',D,fluid)
    return P
def P_SH(S,H,fluid):
    P = CP.PropsSI('P','S',S,'H',H,fluid)
    return P
def P_SQ(S,Q,fluid):
    P = CP.PropsSI('P','S',S,'Q',Q,fluid)
    return P
def P_ST(S,T,fluid):
    P = CP.PropsSI('P','S',S,'T',T,fluid)
    return P
def P_SU(S,U,fluid):
    P = CP.PropsSI('P','S',S,'U',U,fluid)
    return P
def P_TD(T,D,fluid):
    P = CP.PropsSI('P','T',T,'D',D,fluid)
    return P
def P_TH(T,H,fluid):
    P = CP.PropsSI('P','T',T,'H',H,fluid)
    return P
def P_TQ(T,Q,fluid):
    P = CP.PropsSI('P','T',T,'Q',Q,fluid)
    return P
def P_TS(T,S,fluid):
    P = CP.PropsSI('P','T',T,'S',S,fluid)
    return P
def P_TU(T,U,fluid):
    P = CP.PropsSI('P','T',T,'U',U,fluid)
    return P
def P_UD(U,D,fluid):
    P = CP.PropsSI('P','U',U,'D',D,fluid)
    return P
def P_UH(U,H,fluid):
    P = CP.PropsSI('P','U',U,'H',H,fluid)
    return P
def P_UQ(U,Q,fluid):
    P = CP.PropsSI('P','U',U,'Q',Q,fluid)
    return P
def P_US(U,S,fluid):
    P = CP.PropsSI('P','U',U,'S',S,fluid)
    return P
def P_UT(U,T,fluid):
    P = CP.PropsSI('P','U',U,'T',T,fluid)
    return P
def Q_DH(D,H,fluid):
    Q = CP.PropsSI('Q','D',D,'H',H,fluid)
    return Q
def Q_DP(D,P,fluid):
    Q = CP.PropsSI('Q','D',D,'P',P,fluid)
    return Q
def Q_DS(D,S,fluid):
    Q = CP.PropsSI('Q','D',D,'S',S,fluid)
    return Q
def Q_DT(D,T,fluid):
    Q = CP.PropsSI('Q','D',D,'T',T,fluid)
    return Q
def Q_DU(D,U,fluid):
    Q = CP.PropsSI('Q','D',D,'U',U,fluid)
    return Q
def Q_HD(H,D,fluid):
    Q = CP.PropsSI('Q','H',H,'D',D,fluid)
    return Q
def Q_HP(H,P,fluid):
    Q = CP.PropsSI('Q','H',H,'P',P,fluid)
    return Q
def Q_HS(H,S,fluid):
    Q = CP.PropsSI('Q','H',H,'S',S,fluid)
    return Q
def Q_HT(H,T,fluid):
    Q = CP.PropsSI('Q','H',H,'T',T,fluid)
    return Q
def Q_HU(H,U,fluid):
    Q = CP.PropsSI('Q','H',H,'U',U,fluid)
    return Q
def Q_PD(P,D,fluid):
    Q = CP.PropsSI('Q','P',P,'D',D,fluid)
    return Q
def Q_PH(P,H,fluid):
    Q = CP.PropsSI('Q','P',P,'H',H,fluid)
    return Q
def Q_PS(P,S,fluid):
    Q = CP.PropsSI('Q','P',P,'S',S,fluid)
    return Q
def Q_PT(P,T,fluid):
    Q = CP.PropsSI('Q','P',P,'T',T,fluid)
    return Q
def Q_PU(P,U,fluid):
    Q = CP.PropsSI('Q','P',P,'U',U,fluid)
    return Q
def Q_SD(S,D,fluid):
    Q = CP.PropsSI('Q','S',S,'D',D,fluid)
    return Q
def Q_SH(S,H,fluid):
    Q = CP.PropsSI('Q','S',S,'H',H,fluid)
    return Q
def Q_SP(S,P,fluid):
    Q = CP.PropsSI('Q','S',S,'P',P,fluid)
    return Q
def Q_ST(S,T,fluid):
    Q = CP.PropsSI('Q','S',S,'T',T,fluid)
    return Q
def Q_SU(S,U,fluid):
    Q = CP.PropsSI('Q','S',S,'U',U,fluid)
    return Q
def Q_TD(T,D,fluid):
    Q = CP.PropsSI('Q','T',T,'D',D,fluid)
    return Q
def Q_TH(T,H,fluid):
    Q = CP.PropsSI('Q','T',T,'H',H,fluid)
    return Q
def Q_TP(T,P,fluid):
    Q = CP.PropsSI('Q','T',T,'P',P,fluid)
    return Q
def Q_TS(T,S,fluid):
    Q = CP.PropsSI('Q','T',T,'S',S,fluid)
    return Q
def Q_TU(T,U,fluid):
    Q = CP.PropsSI('Q','T',T,'U',U,fluid)
    return Q
def Q_UD(U,D,fluid):
    Q = CP.PropsSI('Q','U',U,'D',D,fluid)
    return Q
def Q_UH(U,H,fluid):
    Q = CP.PropsSI('Q','U',U,'H',H,fluid)
    return Q
def Q_UP(U,P,fluid):
    Q = CP.PropsSI('Q','U',U,'P',P,fluid)
    return Q
def Q_US(U,S,fluid):
    Q = CP.PropsSI('Q','U',U,'S',S,fluid)
    return Q
def Q_UT(U,T,fluid):
    Q = CP.PropsSI('Q','U',U,'T',T,fluid)
    return Q
def S_DH(D,H,fluid):
    S = CP.PropsSI('S','D',D,'H',H,fluid)
    return S
def S_DP(D,P,fluid):
    S = CP.PropsSI('S','D',D,'P',P,fluid)
    return S
def S_DQ(D,Q,fluid):
    S = CP.PropsSI('S','D',D,'Q',Q,fluid)
    return S
def S_DT(D,T,fluid):
    S = CP.PropsSI('S','D',D,'T',T,fluid)
    return S
def S_DU(D,U,fluid):
    S = CP.PropsSI('S','D',D,'U',U,fluid)
    return S
def S_HD(H,D,fluid):
    S = CP.PropsSI('S','H',H,'D',D,fluid)
    return S
def S_HP(H,P,fluid):
    S = CP.PropsSI('S','H',H,'P',P,fluid)
    return S
def S_HQ(H,Q,fluid):
    S = CP.PropsSI('S','H',H,'Q',Q,fluid)
    return S
def S_HT(H,T,fluid):
    S = CP.PropsSI('S','H',H,'T',T,fluid)
    return S
def S_HU(H,U,fluid):
    S = CP.PropsSI('S','H',H,'U',U,fluid)
    return S
def S_PD(P,D,fluid):
    S = CP.PropsSI('S','P',P,'D',D,fluid)
    return S
def S_PH(P,H,fluid):
    S = CP.PropsSI('S','P',P,'H',H,fluid)
    return S
def S_PQ(P,Q,fluid):
    S = CP.PropsSI('S','P',P,'Q',Q,fluid)
    return S
def S_PT(P,T,fluid):
    S = CP.PropsSI('S','P',P,'T',T,fluid)
    return S
def S_PU(P,U,fluid):
    S = CP.PropsSI('S','P',P,'U',U,fluid)
    return S
def S_QD(Q,D,fluid):
    S = CP.PropsSI('S','Q',Q,'D',D,fluid)
    return S
def S_QH(Q,H,fluid):
    S = CP.PropsSI('S','Q',Q,'H',H,fluid)
    return S
def S_QP(Q,P,fluid):
    S = CP.PropsSI('S','Q',Q,'P',P,fluid)
    return S
def S_QT(Q,T,fluid):
    S = CP.PropsSI('S','Q',Q,'T',T,fluid)
    return S
def S_QU(Q,U,fluid):
    S = CP.PropsSI('S','Q',Q,'U',U,fluid)
    return S
def S_TD(T,D,fluid):
    S = CP.PropsSI('S','T',T,'D',D,fluid)
    return S
def S_TH(T,H,fluid):
    S = CP.PropsSI('S','T',T,'H',H,fluid)
    return S
def S_TP(T,P,fluid):
    S = CP.PropsSI('S','T',T,'P',P,fluid)
    return S
def S_TQ(T,Q,fluid):
    S = CP.PropsSI('S','T',T,'Q',Q,fluid)
    return S
def S_TU(T,U,fluid):
    S = CP.PropsSI('S','T',T,'U',U,fluid)
    return S
def S_UD(U,D,fluid):
    S = CP.PropsSI('S','U',U,'D',D,fluid)
    return S
def S_UH(U,H,fluid):
    S = CP.PropsSI('S','U',U,'H',H,fluid)
    return S
def S_UP(U,P,fluid):
    S = CP.PropsSI('S','U',U,'P',P,fluid)
    return S
def S_UQ(U,Q,fluid):
    S = CP.PropsSI('S','U',U,'Q',Q,fluid)
    return S
def S_UT(U,T,fluid):
    S = CP.PropsSI('S','U',U,'T',T,fluid)
    return S
def T_DH(D,H,fluid):
    T = CP.PropsSI('T','D',D,'H',H,fluid)
    return T
def T_DP(D,P,fluid):
    T = CP.PropsSI('T','D',D,'P',P,fluid)
    return T
def T_DQ(D,Q,fluid):
    T = CP.PropsSI('T','D',D,'Q',Q,fluid)
    return T
def T_DS(D,S,fluid):
    T = CP.PropsSI('T','D',D,'S',S,fluid)
    return T
def T_DU(D,U,fluid):
    T = CP.PropsSI('T','D',D,'U',U,fluid)
    return T
def T_HD(H,D,fluid):
    T = CP.PropsSI('T','H',H,'D',D,fluid)
    return T
def T_HP(H,P,fluid):
    T = CP.PropsSI('T','H',H,'P',P,fluid)
    return T
def T_HQ(H,Q,fluid):
    T = CP.PropsSI('T','H',H,'Q',Q,fluid)
    return T
def T_HS(H,S,fluid):
    T = CP.PropsSI('T','H',H,'S',S,fluid)
    return T
def T_HU(H,U,fluid):
    T = CP.PropsSI('T','H',H,'U',U,fluid)
    return T
def T_PD(P,D,fluid):
    T = CP.PropsSI('T','P',P,'D',D,fluid)
    return T
def T_PH(P,H,fluid):
    T = CP.PropsSI('T','P',P,'H',H,fluid)
    return T
def T_PQ(P,Q,fluid):
    T = CP.PropsSI('T','P',P,'Q',Q,fluid)
    return T
def T_PS(P,S,fluid):
    T = CP.PropsSI('T','P',P,'S',S,fluid)
    return T
def T_PU(P,U,fluid):
    T = CP.PropsSI('T','P',P,'U',U,fluid)
    return T
def T_QD(Q,D,fluid):
    T = CP.PropsSI('T','Q',Q,'D',D,fluid)
    return T
def T_QH(Q,H,fluid):
    T = CP.PropsSI('T','Q',Q,'H',H,fluid)
    return T
def T_QP(Q,P,fluid):
    T = CP.PropsSI('T','Q',Q,'P',P,fluid)
    return T
def T_QS(Q,S,fluid):
    T = CP.PropsSI('T','Q',Q,'S',S,fluid)
    return T
def T_QU(Q,U,fluid):
    T = CP.PropsSI('T','Q',Q,'U',U,fluid)
    return T
def T_SD(S,D,fluid):
    T = CP.PropsSI('T','S',S,'D',D,fluid)
    return T
def T_SH(S,H,fluid):
    T = CP.PropsSI('T','S',S,'H',H,fluid)
    return T
def T_SP(S,P,fluid):
    T = CP.PropsSI('T','S',S,'P',P,fluid)
    return T
def T_SQ(S,Q,fluid):
    T = CP.PropsSI('T','S',S,'Q',Q,fluid)
    return T
def T_SU(S,U,fluid):
    T = CP.PropsSI('T','S',S,'U',U,fluid)
    return T
def T_UD(U,D,fluid):
    T = CP.PropsSI('T','U',U,'D',D,fluid)
    return T
def T_UH(U,H,fluid):
    T = CP.PropsSI('T','U',U,'H',H,fluid)
    return T
def T_UP(U,P,fluid):
    T = CP.PropsSI('T','U',U,'P',P,fluid)
    return T
def T_UQ(U,Q,fluid):
    T = CP.PropsSI('T','U',U,'Q',Q,fluid)
    return T
def T_US(U,S,fluid):
    T = CP.PropsSI('T','U',U,'S',S,fluid)
    return T
def U_DH(D,H,fluid):
    U = CP.PropsSI('U','D',D,'H',H,fluid)
    return U
def U_DP(D,P,fluid):
    U = CP.PropsSI('U','D',D,'P',P,fluid)
    return U
def U_DQ(D,Q,fluid):
    U = CP.PropsSI('U','D',D,'Q',Q,fluid)
    return U
def U_DS(D,S,fluid):
    U = CP.PropsSI('U','D',D,'S',S,fluid)
    return U
def U_DT(D,T,fluid):
    U = CP.PropsSI('U','D',D,'T',T,fluid)
    return U
def U_HD(H,D,fluid):
    U = CP.PropsSI('U','H',H,'D',D,fluid)
    return U
def U_HP(H,P,fluid):
    U = CP.PropsSI('U','H',H,'P',P,fluid)
    return U
def U_HQ(H,Q,fluid):
    U = CP.PropsSI('U','H',H,'Q',Q,fluid)
    return U
def U_HS(H,S,fluid):
    U = CP.PropsSI('U','H',H,'S',S,fluid)
    return U
def U_HT(H,T,fluid):
    U = CP.PropsSI('U','H',H,'T',T,fluid)
    return U
def U_PD(P,D,fluid):
    U = CP.PropsSI('U','P',P,'D',D,fluid)
    return U
def U_PH(P,H,fluid):
    U = CP.PropsSI('U','P',P,'H',H,fluid)
    return U
def U_PQ(P,Q,fluid):
    U = CP.PropsSI('U','P',P,'Q',Q,fluid)
    return U
def U_PS(P,S,fluid):
    U = CP.PropsSI('U','P',P,'S',S,fluid)
    return U
def U_PT(P,T,fluid):
    U = CP.PropsSI('U','P',P,'T',T,fluid)
    return U
def U_QD(Q,D,fluid):
    U = CP.PropsSI('U','Q',Q,'D',D,fluid)
    return U
def U_QH(Q,H,fluid):
    U = CP.PropsSI('U','Q',Q,'H',H,fluid)
    return U
def U_QP(Q,P,fluid):
    U = CP.PropsSI('U','Q',Q,'P',P,fluid)
    return U
def U_QS(Q,S,fluid):
    U = CP.PropsSI('U','Q',Q,'S',S,fluid)
    return U
def U_QT(Q,T,fluid):
    U = CP.PropsSI('U','Q',Q,'T',T,fluid)
    return U
def U_SD(S,D,fluid):
    U = CP.PropsSI('U','S',S,'D',D,fluid)
    return U
def U_SH(S,H,fluid):
    U = CP.PropsSI('U','S',S,'H',H,fluid)
    return U
def U_SP(S,P,fluid):
    U = CP.PropsSI('U','S',S,'P',P,fluid)
    return U
def U_SQ(S,Q,fluid):
    U = CP.PropsSI('U','S',S,'Q',Q,fluid)
    return U
def U_ST(S,T,fluid):
    U = CP.PropsSI('U','S',S,'T',T,fluid)
    return U
def U_TD(T,D,fluid):
    U = CP.PropsSI('U','T',T,'D',D,fluid)
    return U
def U_TH(T,H,fluid):
    U = CP.PropsSI('U','T',T,'H',H,fluid)
    return U
def U_TP(T,P,fluid):
    U = CP.PropsSI('U','T',T,'P',P,fluid)
    return U
def U_TQ(T,Q,fluid):
    U = CP.PropsSI('U','T',T,'Q',Q,fluid)
    return U
def U_TS(T,S,fluid):
    U = CP.PropsSI('U','T',T,'S',S,fluid)
    return U
def T_cri(fluid):
    return CP.PropsSI('Tcrit', fluid)

def P_cri(fluid):
    return CP.PropsSI('Pcrit', fluid)