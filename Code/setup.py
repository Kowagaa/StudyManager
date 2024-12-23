import pandas as pd

def inputRecord():
    subject = input("Input subject for this topic\n")
    topic = input("Input Topic\n")
    weight_mod = input("Input weight mod (or 1 to keep same)")
    df = pd.DataFrame({
        "SUBJECT" : subject, 
        "TOPIC" : topic,
        "TIMES STUDIE" : 0,
        "AVG PERFORMANCE" : 0.5,
        "WEIGHT MOD" : weight_mod, 
        "WEIGHT" : 2 * weight_mod
    })
    df.to_csv('startingdf.csv', mode='a', index=False, header=False)


flag = True
while flag:
    cont = input("Continue? \n[y/n]\n")
    if cont in ["Y", "y"]:
        flag = False
    elif cont in ["N", "n"]:
        inputRecord()
    else:
        print("Invalid Input")
    print("Setup Exited")
