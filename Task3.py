swimming_time = int(input("swimming time (in minutes): "))
cycling_time = int(input("cycling time (in minutes): "))
running_time = int(input("running time (in minutes): "))
# total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time
# Determine the award 
if total_time <= 100:
    print("Award: Provincial Colours")
elif total_time <= 105:
    print("Award: Provincial Half Colours")
elif total_time <= 110:
    print("Award: Provincial Scroll")
else:
    print("Award: No award")