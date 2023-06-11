import matplotlib.pyplot as plt
import numpy as np
import os

def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier


class CalcClass():

    def __init__(self, x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4, r1, r2, r3,r4, rkv1, rkv2, rkv3, rkv4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.z4 = z4
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.rkv1 = rkv1
        self.rkv2 = rkv2
        self.rkv3 = rkv3
        self.rkv4 = rkv4

    # 3 nomalum tenglamalar sistemasi uchun metod
    def formula_sq(self):
        pass

    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    
    # (X,Y,Z)  qiymaylarini qaytaruvchi metod
    def formula_fc(self): 
        a11 = (self.x1 - self.x2)*2
        a12 = (self.y1 - self.y2)*2
        a13 = (self.z1 - self.z2)*2
        a21 = (self.x1 - self.x3)*2
        a22 = (self.y1 - self.y3)*2
        a23 = (self.z1 - self.z3)*2
        a31 = (self.x1 - self.x4)*2
        a32 = (self.y1 - self.y4)*2
        a33 = (self.z1 - self.z4)*2
        R1 = (self.r2**2 - self.r1**2) + (self.x1**2 - self.x2**2) + (self.y1**2 - self.y2**2) + (self.z1**2 - self.z2**2)
        R2 = (self.r3**2 - self.r1**2) + (self.x1**2 - self.x3**2) + (self.y1**2 - self.y3**2) + (self.z1**2 - self.z3**2)
        R3 = (self.r4**2 - self.r1**2) + (self.x1**2 - self.x4**2) + (self.y1**2 - self.y4**2) + (self.z1**2 - self.z4**2)
        A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
        B = np.array([R1, R2, R3])
        x=np.dot(np.linalg.inv(A), B)
        print(f"x={x[0]}")
        print(f"y={x[1]}")
        print(f"z={x[2]}")
        xx = np.linalg.solve(A,B)
        a11 = (self.x1 - self.x2)*2
        a12 = (self.y1 - self.y2)*2
        a13 = (self.z1 - self.z2)*2
        a21 = (self.x1 - self.x3)*2
        a22 = (self.y1 - self.y3)*2
        a23 = (self.z1 - self.z3)*2
        a31 = (self.x1 - self.x4)*2
        a32 = (self.y1 - self.y4)*2
        a33 = (self.z1 - self.z4)*2
        # return f"x={int(x[0])} y={int(x[1])} z={int(x[2])}\n{truncate(a11), a12, a13, truncate(R1,3)}\n{a21,a22,a23,truncate(R2,3)}\n{a31,a32,a33, truncate(R3,3)}"
        return x
    
    # koeffitsientlar uchun
    def get_index(self):
        a11 = (self.x1-self.x2)*2
        a12 = (self.y1-self.y2)*2
        a13 = (self.z1-self.z2)*2
        a21 = (self.x1-self.x3)*2
        a22 = (self.y1-self.y3)*2
        a23 = (self.z1-self.z3)*2
        a31 = (self.x1-self.x4)*2
        a32 = (self.y1-self.y4)*2
        a33 = (self.z1-self.z4)*2
        R1 = (self.r2**2 - self.r1**2) + (self.x1**2 - self.x2**2) + (self.y1**2 - self.y2**2) + (self.z1**2-self.z2**2)
        R2 = (self.r3**2 - self.r1**2) + (self.x1**2 - self.x3**2) + (self.y1**2 - self.y3**2) + (self.z1**2-self.z3**2)
        R3 = (self.r4**2 - self.r1**2) + (self.x1**2 - self.x4**2) + (self.y1**2 - self.y4**2) + (self.z1**2-self.z4**2)
        return [a11, a12, a13, a21, a22, a23, a31, a32, a33,  R1 ,  R2 ,  R3 ]
    
    # o'qlarni chizish va rasm olish
    def get_graph(self, x, y, z):
        # 4 ta koordinatalar
        u = [self.x1, self.y1, self.z1]
        v = [self.x2, self.y2, self.z3]
        q = [self.x3, self.y3, self.z3]
        m = [self.x4, self.y4, self.z4]
        # chiziladigan figura o'lchami
        fig = plt.figure(figsize=(15,15))
        # shaklga subtitle berish
        fig.suptitle("Nishonning 3 o'lchamli joylashuvi", fontsize=14, fontweight='bold')


        ax = plt.axes(projection='3d')
        min_x = min(self.x1, self.x2, self.x3, self.x4)
        max_x = max(self.x1, self.x2, self.x3, self.x4)
        max_y = max(self.y1, self.y2, self.y3, self.y4)
        min_y = min(self.y1, self.y2, self.y3, self.y4)
        min_z = min(self.z1, self.z2, self.z3, self.z4)
        max_z = max(self.z1, self.z2, self.z3, self.z4)
        # jism uchun 3 ta o'qda chegaralar berish
        ax.set_xlim([-10+min_x, 10+max_x])
        ax.set_ylim([-10+min_y, 10+max_y])
        ax.set_zlim([-10+min_z, 10+max_z])

        ax.set_title(f'{x,y,z}')
        # jism koordinatasi
        start = [x,y,z]
      
        ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2],   color="r")
        ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2], color="g")
        ax.quiver(start[0], start[1], start[2], q[0], q[1], q[2],  color="b")
        ax.quiver(start[0], start[1], start[2], m[0], m[1], m[2],    color="y" )
        ax.view_init(x, y, z)
        # rasm saqlangan manzil
        # parent_dir = """C:\\Users\\Mirabror\\Desktop\\BMIcalc\\mainapp"""
        directory = "graphs"
        # path = os.path.join(parent_dir, directory)
        # address = f'{path}\\graph{x,y,z}.png'
        # fig.savefig(address)

        # return address
    
    def step_one(self):
        left, width = .50, .10
        bottom, height = .50, .10
        right = left + width
        top = bottom + height
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.text(0.5*(left+right), 0.7*(bottom+top),
                r'$(x-x1)^2 + (y-y1)^2 + (z-z1)^2=r1^2$',
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=20, color='black',
                transform=ax.transAxes)
        ax.text(0.5*(left+right), 0.6*(bottom+top),
                r'$(x-x3)^2 + (y-y3)^2 + (z-z3)^2=r3^2$',
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=20, color='black',
                transform=ax.transAxes)
        ax.text(0.5*(left+right), 0.5*(bottom+top),
                r'$(x-x2)^2 + (y-y2)^2 + (z-z2)^2=r2^2$',
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=20, color='black',
                transform=ax.transAxes)
        ax.text(0.5*(left+right), 0.4*(bottom+top),
                r'$(x-x4)^2 + (y-y4)^2 + (z-z4)^2=r4^2$',
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=20, color='black',
                transform=ax.transAxes)
        
    def get_3x_index(self):
        a11 = (self.x1-self.x2)*2
        a12 = (self.y1-self.y2)*2
        a13 = (self.z1-self.z2)*2
        a21 = (self.x1-self.x3)*2
        a22 = (self.y1-self.y3)*2
        a23 = (self.z1-self.z3)*2

        d1 = (self.rkv2 - self.rkv1) + (self.x1**2 - self.x2**2) + (self.y1**2 - self.y2**2) + (self.z1**2-self.z2**2)
        d2 = (self.rkv3 - self.rkv1) + (self.x1**2 - self.x3**2) + (self.y1**2 - self.y3**2) + (self.z1**2-self.z3**2)
        # y uchun 
        b1 = (a12*a21 - a22*a11)
        b2 = (a11*a23 - a21*a13)
        t11 = (d1*a21 - d2*a11)
        # x uchun
        t21 = (d1*b1 - a12*t11)
        t22 = (a13*b1 + b2*a12)
        
        # kvadrat tenglama koeffitsientlari
        k1 = (t22/(a11*b1))**2 + (b2/b1)**2 + 1
        k2 = ((-2)*((((t21-a11*b1*self.x1)/(a11*b1))*(t22/(a11*b1))) - ((t11-b1*self.y1)/(b1))*(b2/b1) + (self.z1)))
        k3 = ((t21-a11*b1*self.x1)/(a11*b1))**2 + ((t11-b1*self.y1)/b1)**2 + self.z1**2 - self.rkv1
        print(t22/(a11*b1))
        return {'a11': a11, "a12": a12, 'a13': a13,'d1': d1,
                'a21': a21, "a22": a22, 'a23': a23,'d2': d2,
                'b1': b1, 'b2': b2, 't11': t11, 't21': t21,
                't22': t22, 'k1': k1, 'k2': k2, "k3": k3, "x1": self.x1, 'x2': self.x2, 'x3': self.x3,
                'R1': self.rkv1, "R2": self.rkv2, "R3": self.rkv3, 'check': ((t11-b1*self.y1)/b1)**2 + self.z1**2 - self.rkv1 }
    
    def get_3x_index_r(self):
        a11 = (self.x1-self.x2)*2
        a12 = (self.y1-self.y2)*2
        a13 = (self.z1-self.z2)*2
        a21 = (self.x1-self.x3)*2
        a22 = (self.y1-self.y3)*2
        a23 = (self.z1-self.z3)*2

        d1 = (self.r2*self.r2 - self.r1*self.r1) + (self.x1**2 - self.x2**2) + (self.y1**2 - self.y2**2) + (self.z1**2-self.z2**2)
        d2 = (self.r3*self.r3 - self.r1*self.r1) + (self.x1**2 - self.x3**2) + (self.y1**2 - self.y3**2) + (self.z1**2-self.z3**2)
        # y uchun 
        b1 = (a12*a21 - a22*a11)
        b2 = (a11*a23 - a21*a13)
        t11 = (d1*a21 - d2*a11)
        # x uchun
        t21 = (d1*b1 - a12*t11)
        t22 = (a13*b1 + b2*a12)
        
        # kvadrat tenglama koeffitsientlari
        k1 = (t22/(a11*b1))**2 + (b2/b1)**2 + 1
        k2 = ((-2)*((((t21-a11*b1*self.x1)/(a11*b1))*(t22/(a11*b1))) - ((t11-b1*self.y1)/(b1))*(b2/b1) + (self.z1)))
        k3 = ((t21-a11*b1*self.x1)/(a11*b1))**2 + ((t11-b1*self.y1)/b1)**2 + self.z1**2 - self.r1*self.r1
        print(t22/(a11*b1))
        return {'a11': a11, "a12": a12, 'a13': a13,'d1': d1,
                'a21': a21, "a22": a22, 'a23': a23,'d2': d2,
                'b1': b1, 'b2': b2, 't11': t11, 't21': t21,
                't22': t22, 'k1': k1, 'k2': k2, "k3": k3, "x1": self.x1, 'x2': self.x2, 'x3': self.x3,
                'R1': self.r1*self.r1, "R2": self.r2**2, "R3": self.r3**2, 'check': ((t11-b1*self.y1)/b1)**2 + self.z1**2 - self.rkv1 }
    
    def get_4x_index(self):
        a11 = (self.x1 - self.x2)*2
        a12 = (self.y1 - self.y2)*2
        a13 = (self.z1 - self.z2)*2
        a21 = (self.x1 - self.x3)*2
        a22 = (self.y1 - self.y3)*2
        a23 = (self.z1 - self.z3)*2
        a31 = (self.x1 - self.x4)*2
        a32 = (self.y1 - self.y4)*2
        a33 = (self.z1 - self.z4)*2

        d1 = (self.rkv2 - self.rkv1) + (self.x1**2 - self.x2**2) + (self.y1**2 - self.y2**2) + (self.z1**2 - self.z2**2)
        d2 = (self.rkv3 - self.rkv1) + (self.x1**2 - self.x3**2) + (self.y1**2 - self.y3**2) + (self.z1**2 - self.z3**2)
        d3 = (self.rkv4 - self.rkv1) + (self.x1**2 - self.x4**2) + (self.y1**2 - self.y4**2) + (self.z1**2 - self.z4**2)
        # y uchun 
        b11 = (a22*a11 - a12*a21)
        b12 = (a11*a23 - a21*a13)
        b21 = (a32*a11 - a31*a12)
        b22 = (a33*a11 - a31*a13)
        k1 = a11*d2 - d1*a21
        k2 = a11*d3 - d1*a31
        return {'a11': a11, "a12": a12, 'a13': a13,'d1': d1,
                'a21': a21, "a22": a22, 'a23': a23,'d2': d2,
                'a31': a31, 'a32': a32, 'a33': a33,'d3': d3,
                'b11': b11, 'b12': b12, 'b21': b21, "b22": b22,
                'k1': k1, "k2": k2}
    
    def get_4x_index_r(self):
        a11 = (self.x1 - self.x2)*2
        a12 = (self.y1 - self.y2)*2
        a13 = (self.z1 - self.z2)*2
        a21 = (self.x1 - self.x3)*2
        a22 = (self.y1 - self.y3)*2
        a23 = (self.z1 - self.z3)*2
        a31 = (self.x1 - self.x4)*2
        a32 = (self.y1 - self.y4)*2
        a33 = (self.z1 - self.z4)*2

        d1 = (self.r2 * self.r2 - self.r1*self.r1) + (self.x1**2 - self.x2**2) + (self.y1**2 - self.y2**2) + (self.z1**2-self.z2**2)
        d2 = (self.r3 * self.r3 - self.r1*self.r1) + (self.x1**2 - self.x3**2) + (self.y1**2 - self.y3**2) + (self.z1**2-self.z3**2)
        d3 = (self.r4 * self.r4 - self.r1*self.r1) + (self.x1**2 - self.x4**2) + (self.y1**2 - self.y4**2) + (self.z1**2-self.z4**2)
        # y uchun 
        b11 = (a22*a11 - a12*a21)
        b12 = (a11*a23 - a21*a13)
        b21 = (a32*a11 - a31*a12)
        b22 = (a33*a11 - a31*a13)
        k1 = a11*d2 - d1*a21
        k2 = a11*d3 - d1*a31

        # xatolikni topish
        delta1 = d1 - round(d1)  
        delta2 = d2 - round(d2)  
        delta3 = d3 - round(d3)  
        return {'a11': a11, "a12": a12, 'a13': a13,'d1': d1,
                'a21': a21, "a22": a22, 'a23': a23,'d2': d2,
                'a31': a31, 'a32': a32, 'a33': a33,'d3': d3,
                'b11': b11, 'b12': b12, 'b21': b21, "b22": b22,
                'k1': k1, "k2": k2, "delta1": delta1,"delta2": delta2, "delta3": delta3}
    # agar r^2 bo'lsa
    def calc_4x(self):
        kf = self.get_4x_index()
        z = (kf['b21']*kf['k1'] - kf['b11']*kf['k2'])/(kf['b21']*kf['b12']-kf['b11']*kf['b22'])
        y = (kf['k1'] - z*kf['b12'])/kf['b11']
        x = (kf['d1'] -  kf['a13']*z - kf['a12']*y)/kf['a11']
        return [x,y,z]
    # agar r bo'lsa
    def calc_4x_r(self):
        kf = self.get_4x_index_r()
        z = (kf['b21']*kf['k1'] - kf['b11']*kf['k2'])/(kf['b21']*kf['b12']-kf['b11']*kf['b22'])
        y = (kf['k1'] - z*kf['b12'])/kf['b11']
        x = (kf['d1'] -  kf['a13']*z - kf['a12']*y)/kf['a11']
        return [x,y,z]
    
    def calc_3x(self):
        kf = self.get_3x_index()
        print(kf)
        # diskriminant
        D = kf['k2']**2 - 4*kf['k1']*kf['k3']
        z1 = (-kf['k2'] + pow(D, 0.5))/(2*kf['k1'])
        z2 = (-kf['k2'] - pow(D, 0.5))/(2*kf['k1'])
        x1 = (kf['t21'] - kf['t22']*z1)/(kf['a11']*kf['b1'])
        x2 = (kf['t21'] - kf['t22']*z2)/(kf['a11']*kf['b1'])
        y1 = (kf['t11'] + kf['b2']*z1)/(kf['b1'])
        y2 = (kf['t11'] + kf['b2']*z2)/(kf['b1'])
        return [x1, y1, z1, x2, y2, z2, D]


    def calc_3x_r(self):
        kf = self.get_3x_index_r()
        print(kf)
        # diskriminant
        D = kf['k2']**2 - 4*kf['k1']*kf['k3']
        z1 = (-kf['k2'] + pow(D, 0.5))/(2*kf['k1'])
        z2 = (-kf['k2'] - pow(D, 0.5))/(2*kf['k1'])
        x1 = (kf['t21'] - kf['t22']*z1)/(kf['a11']*kf['b1'])
        x2 = (kf['t21'] - kf['t22']*z2)/(kf['a11']*kf['b1'])
        y1 = (kf['t11'] + kf['b2']*z1)/(kf['b1'])
        y2 = (kf['t11'] + kf['b2']*z2)/(kf['b1'])
        return [x1, y1, z1, x2, y2, z2, D]
    
    def d_koeff(self):
        k = CalcClass.get_4x_index_r(self)
        D_A = (8*k['a11']*k['a22']*k['a33'] + 8*k['a13']*k['a21']*k['a32'] + 8*k['a12']*k['a23']*k['a31']) - (8*k['a13']*k['a22']*k['a31'] + 8*k['a11']*k['a23']*k['a32'] + 8*k['a12']*k['a21']*k['a33'])
        return  D_A

    def get_algebraic_complement(self):
        k = CalcClass.get_4x_index_r(self)
        A11 = 4*(k['a22']*k['a33'] - k['a23']*k['a32'])
        A12 = -4*(k['a21']*k['a33'] - k['a23']*k['a31'])
        A13 = 4*(k['a21']*k['a32'] - k['a22']*k['a31'])
        A21 = -4*(k['a12']*k['a33'] - k['a13']*k['a32'])
        A22 = 4*(k['a11']*k['a33'] - k['a13']*k['a31'])
        A23 = -4*(k['a11']*k['a32'] - k['a12']*k['a31'])
        A31 = 4*(k['a12']*k['a23'] - k['a13']*k['a22'])
        A32 = -4*(k['a11']*k['a23'] - k['a13']*k['a21'])
        A33 = 4*(k['a11']*k['a22'] - k['a12']*k['a21'])

        return {'A11': A11, 'A12': A12, 'A13': A13,
                'A21': A21, 'A22': A22, 'A23': A23,
                'A31': A31, 'A32': A32, 'A33': A33}
    
    def calc_inverse_matrix(self):
        # d = CalcClass(self)
        ins1 = CalcClass.get_4x_index_r(self)
        d = CalcClass.d_koeff(self)
        ins2 = CalcClass.get_algebraic_complement(self)
        k1 = ins2['A11']*ins1['delta1'] + ins2['A21']*ins1['delta2'] + ins2['A31']*ins1['delta3']
        k2 = ins2['A12']*ins1['delta1'] + ins2['A22']*ins1['delta2'] + ins2['A32']*ins1['delta3']
        k3 = ins2['A13']*ins1['delta1'] + ins2['A23']*ins1['delta2'] + ins2['A33']*ins1['delta3']
        c1 = k1/d  
        c2 = k2/d 
        c3 = k3/d 
        return {'k1':k1, 'k2':k2, "k3": k3,
                "c1":c1, 'c2':c2, "c3":c3, 'd':d}





         
         
    