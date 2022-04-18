import scapy.all as sc


e = sc.Ether()
e.dst = 'ff:ff:ff:ff:ff:ff'

# e.src - MAC
# print("e.src = ", e.src)
# print('sc.ls(e) = ', sc.ls(e))
print("e.show() = ", e.show())
# print("e.display() = ", e.display())
