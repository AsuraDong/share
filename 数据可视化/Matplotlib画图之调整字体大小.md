> 字体大小就是`fontsize`参数

```python
import matplotlib.pyplot as plt

# 代码中的“...”代表省略的其他参数
ax = plt.subplot(111)
# 设置刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 设置坐标标签字体大小
ax.xlabel(..., fontsize=20)
ax.ylabel(..., fontsize=20)
# 设置图例字体大小
ax.legend(..., fontsize=20)
```


实战：
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus']=False

x_data = [2.59,2.72,2.90,3.02,3.23,3.40,3.47,3.61,3.98,4.02,4.09,4.15,4.35,4.44,4.50,4.55,4.63,5.00,5.15,5.28,5.38,5.51,5.57,5.62,5.71,5.74,5.85,5.92,6.22,6.34,6.37,6.48,6.62,6.73,6.76,6.81,6.86,6.96,7.02,7.54,7.64,7.80,7.98,8.12,8.24,8.53,8.70,8.88,9.04]
y_data = [0.32,0.54,0.61,0.48,0.12,0.01,0.07,0.50,1.32,1.35,1.27,1.05,0.33,0.08,0.02,0.08,0.35,1.74,1.96,1.81,1.39,0.82,0.52,0.38,0.28,0.36,0.80,1.08,2.21,2.34,2.37,2.29,1.85,1.37,1.27,1.07,0.93,0.81,0.94,2.79,2.85,2.69,2.13,1.71,1.54,3.23,5.08,4.86,4.06]

x = np.array(x_data)
y = np.array(y_data)

plt.figure(figsize=(30,30),dpi=400,linewidth = 0.6)
# plt.subplot(1,1,1)

plt.plot(x,y,'-*g')
plt.title("电压电流的比",fontsize = 60)
plt.xlabel('Ug2 (*10V)',fontsize=50)
plt.ylabel('Ip (*10**-8A)',fontsize=50)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)

plt.savefig(r"C:\Users\AsuraDong\Desktop\test2.jpg")
# plt.show()

```