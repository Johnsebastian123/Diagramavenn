from matplotlib import pyplot as plt
from matplotlib_venn import venn3


U = {8,40,15,10,13,21,58,0}
A = {40,15,10,13}
B = {0,15,10,21}
C = {58,13,10,21}

Y = ((U-A)|B)&((U-B)|C)&((U-C)|A)
print(Y)


venn3((A,B,C),set_labels=("A","B","C"),alpha=0.9)
plt.title('U=8')

plt.show()





