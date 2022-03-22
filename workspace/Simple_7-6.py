score_chi = float(input("Please enter chinese score:"))
score_eng = float(input("Please enter english score:"))

print("chinese score:", score_chi, "English score:", score_eng)

if score_chi >= 60 and score_eng >= 60:
    print("合格")
elif score_chi >= 60 and score_eng <= 60:
    print("中文合格,英文不合格")
elif score_chi <= 60 and score_eng >= 60:
    print("中文不合格,英文合格")
elif score_chi >= 60 and score_eng <= 60:
    print("都不及格")
else:
    print("檢查合格原因")