pets = {}
pets2 = {}
while(True):
    k=input("������� ��� ������� (������� Enter - �����): ")
    if k=='':
        break
    else:
        k1=input("��� �������: ")
        k2=int(input("������� �������: "))
        k3=input("��� ���������: ")

pets2 = {'��� �������:':k1,'������� �������:':k2, '��� ���������:':k3 }
pets[k] = pets2

for key, value in pets.items():

        vid=value['��� �������:']
        vozrast=value['������� �������:']
        imy=value['��� ���������:']
        year_case = ''
        if vozrast % 10 == 1 and vozrast != 11 and vozrast % 100 != 11:
            year_case = '���'
        elif 1 < vozrast % 10 <= 4 and vozrast != 12 and vozrast != 13 and vozrast != 14:
           year_case = '����'
else:
    year_case = '���'

print("���", vid, "�� ������", key,". ������� �������:", vozrast, year_case, "��� ���������:", imy)