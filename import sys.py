temperatures_week=[18.5,19,20,25.0,2,30,13.9]
week_days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temperatures_ave=sum(temperatures_week)/len(temperatures_week)
temperatures_max=max(temperatures_week)
temperatures_min=min(temperatures_week)
temperatures_Fahrenheit=[round(c * 9 /5 , 1 )for c in temperatures_week]
temperatures_above_20 =[(week_days[i],temperatures_week[i]) for i in range(len(temperatures_week)) if temperatures_week[i]>20 ]
print("The average temperature in a week is : " + temperatures_week)
print("The highest temperature is: "+ temperatures_max)
print("The lowest temperature is: "+ temperatures_min)
print("The Fahrenheit temperature : ")
