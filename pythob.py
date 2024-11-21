#tinh bmi
def tinh_bmi(can_nang,chieu_cao):
        
    return can_nang / pow(chieu_cao,2)

nhap_cannang = float(input("nhập cân nặng của bạn vào đây: "))
nhap_chieucao= float(input("nhập chiều cao của bạn vào đây: "))

def dem_kitu(name,name1):
    name = name.lower()
    
    name1 = name1.lower()
    dem = 0
    for ki_tu in range(ord('a'), ord('b')):
        dem + 1
    if dem < 3:
        print('chưa có duyên')
    elif dem >= 2:
        print('nên tiến tới nhau')
        
bmi = tinh_bmi(nhap_cannang,nhap_chieucao)


print(f"bmi của bạn là {round(bmi,1)}")
 

if bmi < 18.5:
    print('gầy')
    
elif bmi >= 18.5 and bmi <= 24.9:
    
    print('bình thường')
else:
    
    print("béo phì")
    
name =(str(input('nhập tên bạn:')))
name1 = str(input('nhập tên người yêu bạn:'))

du_bao = dem_kitu(name,name1)

print(du_bao)




    
