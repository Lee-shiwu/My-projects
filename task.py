import numpy as np
temperatures_week = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures_ave=np.mean(temperatures_week)
print(f"Average temperature: {temperatures_ave:.2f}°C")
temperatures_max=np.max(temperatures_week)
print(f"Max temperature: {temperatures_max}")
temperatures_min=np.min(temperatures_week)
print(f"Min temperature: {temperatures_min}")
temperatures_fahrenheit=np.round(temperatures_week * 9 / 5+32,1)
print("Temperatures in Fahrenheit:", [f"{t:.1f}" for t in temperatures_fahrenheit])
above_20_indexs=np.where(temperatures_week>20)[0]
print("Indexs with temperature > 20°C (by index):",above_20_indexs)
above_20_days=[days[i] for i in above_20_indexs ]
print("Days with temperature > 20°C:")
for i in above_20_indexs:
    print(f"-{days[i]}: {temperatures_week[i]}")
