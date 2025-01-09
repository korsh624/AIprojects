import pandas as pd
import pickle
import pandas as pd
from catboost import CatBoostClassifier
l=['21','мужской','Бакалавриат', '29', '0',"да" , 'умеренная']
# [14, 1, 2, 4, 40, 0, 1, 2, 1, 1, 0, 0, 4.6]
def coder(l):
    newl=[]
    #Возраст
    newl.append(int(l[0]))
    #Пол
    gender=l[1].lower()
    if gender==('мужской'):
        newl.append(0)
    else:
        newl.append(1)
    #Образование родителей
    patedu= l[2].lower()
    if patedu==('нет'):
        newl.append(0)
    if patedu==('средняя школа'):
        newl.append(1)
    if patedu==('немного колледжа'):
        newl.append(2)
    if patedu==('бакалавриат'):
        newl.append(3)
    if patedu==('высшее'):
        newl.append(4)  
    #Учебные часы в неделю
    newl.append(int(l[3]))
    #Количество пропусков
    newl.append(int(l[4]))
    #Репетиторство
    tutoring=l[5].lower()
    if tutoring==('да'):
        newl.append(1)
    else:
        newl.append(0)
    #Поддержка родителей
    ptsupport=l[6]
    if ptsupport==('низкая'):
        newl.append(1)
    if ptsupport==('умеренная'):
        newl.append(2)
    if ptsupport==('высокая'):
        newl.append(3)
    if ptsupport==('очень высокая'):
        newl.append(4)
#GPA    
    newl.append(l[7])
    return newl

        
def getDF(data:list):
    df=pd.DataFrame()
    col=['Age',
 'Gender',
 'ParentalEducation',
 'StudyTimeWeekly',
 'Absences',
 'Tutoring',
 'ParentalSupport',
 'GPA']
    df=pd.DataFrame(columns=col)
    df.loc[len(df)] = data
    return df
# l=[18, 'мужской', 'высшее', 30, 10, 'да', 'высокая']
# l=coder(l)
# print(l)


def getRatingSt(df:pd.DataFrame):
    with open('modelnogpa.pkl', 'rb') as f:
        model = pickle.load(f)
        rating = model.predict(df)
        return rating
