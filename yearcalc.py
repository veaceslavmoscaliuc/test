

#  "baby"    "kid"    "teen"    "young"    "adult"     old"
#      1        4        10         16         19       51
#


#   Calculeaza varsta in ani si o afiseaza






######################################
year = input("Enter curent year: ")    
year_birth = float (input ("Year of birth: "))


baby_born    =  2021 
kid_born     =  2018 
teen_born    =  2011
young_born   =  2005 
adult_born   =  2002
old_born     =  1970

if year == "2022" and baby_born >= 2021 :
    varsta_baby =  baby_born - year_birth 
    print ("baby!")
    print ("Varsta baby: ",varsta_baby)
elif year == "2022":
    varsta_kid =  kid_born - year_birth 
    print ("kid!")
    print ("Varsta kid: ", varsta_kid )  
elif year == "2022":
    varsta_teen =  teen_born - year_birth 
    print ("teen!")
    print ("Varsta teen: ", varsta_teen ) 










   