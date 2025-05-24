from utilies import *
import warnings
warnings.filterwarnings('ignore')
def mainui():
  print("Hi and welcome to lung cancer predictions , byMS20")
  inp = input("Please enter the following with only numbers  like this : 1 to start \ 0 to stop")
  if inp == "1" :
    agin = int(input("The age of the person")) 
    age = agin
    smoking = int(input("is he smoking yes 1 \ or no 0"))
    chronic_cough = int(input("does he have chronic cough yes 1 \ or no 0"))
    shortness_of_breath = int(input("does he have shortness of breath yes 1 \ or no 0"))
    fatiuge = int(input("does he have fatiuge yes 1 \ or no"))
    weight_loss = int(input("does he have weight loss yes 1 \ or no"))
    inpx = [[age,smoking,chronic_cough,shortness_of_breath,fatiuge,weight_loss]]
    inpx2 = [[smoking,chronic_cough,shortness_of_breath,fatiuge,weight_loss]]
    inpx2 = scaler.transform(inpx2)
    
    predin = model.predict(inpx)
    predin2 = model2.predict(inpx2)
    if predin[0]  == 1 and predin2[0] == 1:
      print("Lung cancer Detected.")
    
    elif predin[0] == 0 and predin2[0] == 0: 
      print("Lung cancer Undetected.")
    elif predin[0] == 1 and predin2[0] == 0:
      print("Lung cancer Detected by the first model and Undetected by the second model.")
    elif predin[0] == 0 and predin2[0] == 1:
      print("Lung cancer Undetected by the first model and Detected by the second model.")
  else:
    print("bye")
    


mainui()
