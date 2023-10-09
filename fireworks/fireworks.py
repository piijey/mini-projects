import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 初期値設定
v0 = 10  # 初速度
k_prime = 0.1  # 空気抵抗の係数
tmax = 20
t = np.linspace(0, tmax, 200)  # 時間
angles = np.linspace(0, 2*np.pi, 36)  # 角度方向の広がり

fig, ax = plt.subplots(figsize=(7,7))
fig.patch.set_facecolor('black') #図全体の背景色を指定
ax.set_facecolor('black') #プロットの背景色を指定

def init():
    return []

# s軌道の計算関数
def s_orbit(t, angle):
    r = v0/k_prime * (1 - np.exp(-k_prime * t))
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return x, y

# p軌道の計算関数
def p_orbit(t, angle):
    r = v0/k_prime * (1 - np.exp(-k_prime * t))
    x = r * np.sin(angle)
    y = r * np.sin(angle) * np.cos(angle)
    return x, y

def animate(i):
    ax.clear()
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # s軌道のアニメーション
    if i < len(t)//2:  # 前半はs軌道のみ
        for angle in angles:
            x, y = s_orbit(t[i], angle)
            ax.plot(x, y, 'o', color='red')
            ax.plot(x*0.5, y*0.5, 'o', color='yellow')
    # p軌道のアニメーション
    else:
        for angle in angles:
            delay = t[len(t)//2] #前半の分だけ時間を遅らせて位置を決める
            x, y = p_orbit(t[i]-delay, angle)
            ax.plot(x, y, 'o', color='blue')
            ax.plot(y, x, 'o', color='yellow')

    return []

ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True, repeat=True)

# GIFとして保存
ani.save('fireworks.gif', writer='pillow', fps=20)

plt.show()
