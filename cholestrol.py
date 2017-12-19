ldl = int(input("Please enter LDL: "))
print(ldl)
hdl = int(input("Please enter HDL: "))
print(hdl)
tri = int(input("Please enter triglycerides: "))
print(tri)
if (ldl < 100) and (hdl > 60) and (tri < 150):
   print("Cholesterol looks great!")
elif (ldl >130) or (hdl < 50) or (tri > 200):
   print("Warning: cholesterol looks bad!")
else:
   print("Borderline cholesterol problems.")
