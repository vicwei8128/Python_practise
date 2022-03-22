score_chi = float(input("Please enter chinese score:"))
score_eng = float(input("Please enter english score:"))
score_chi = int(score_chi) if score_chi == int(score_chi) else score_chi
score_eng = int(score_eng) if score_eng == int(score_eng) else score_eng
print("chinese score:", score_chi, "English score:", score_eng)

if score_chi >= 60:
    if score_eng >= 60:
        print("合格")
    else:
        print("中文合格,英文不合格")
else:
    if score_eng >= 60:
        print("盈文合格,中文不合格")
    else:
        print("都不及格")
