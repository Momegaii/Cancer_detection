from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

Cncr = pd.read_csv(r'E:\py.proj-20250522T154056Z-1-001\py.proj\Lung_cancer\data\Lng_cncr.csv')
le = LabelEncoder()

Cncrx = Cncr.drop(columns='islngcncr_notlngcncr', axis=1)
Cncry = Cncr['islngcncr_notlngcncr']


x_train, x_test, y_train, y_test = train_test_split(Cncrx, Cncry, test_size=0.2, stratify=Cncry, random_state=2)

model = LogisticRegression()

model.fit(x_train, y_train)
pred = model.predict(x_test)

print("Fitting the model")

model2 = LogisticRegression()

cncrx2 = Cncr.copy()

cncrxc2 = cncrx2.drop(columns=['islngcncr_notlngcncr','age'] , axis=1)
cncryc2 = cncrx2['islngcncr_notlngcncr']

x_trainc2, x_testc2, y_trainc2, y_testc2 = train_test_split(cncrxc2, cncryc2, test_size=0.2, stratify=cncryc2, random_state=2)
scaler = StandardScaler()
x_trainc2 = scaler.fit_transform(x_trainc2)
x_testc2 = scaler.transform(x_testc2)
model2.fit(x_trainc2, y_trainc2)
predc2 = model2.predict(x_testc2)

print(predc2)
print("Fitting the model")

model3 = LogisticRegression()

