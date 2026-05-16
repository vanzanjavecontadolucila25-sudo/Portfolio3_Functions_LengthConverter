##Read Me: Submitted in fulfillment of the subject BES 10a, this Python project is a length conversion tool that translates measurements between metric and standard systems. The program relies primarily on user-defined functions (def) to split the code into organized, reusable blocks for managing each menu and calculation. Inside these functions, if-elif-else conditional statements direct the user through the different conversion choices, while try-except blocks provide basic error handling by catching non-numeric inputs before they can cause a system crash. Finally, print statements are used throughout the script to display the final conversion results and format the console interface for a cleaner layout. 

#The conversion data are acquired from Civil Engineering Help in Facebook
#source link: https://www.facebook.com/share/p/1NB6s1u7pZ/

##This is the title section##
print ('=========================Metric and Standard Conversions for Length=========================')

##For any section in the page containing "print ('')", expect it to be a page break/space##
print ('')        

#The following are the users' choices for conversion
def ChooseConversion ():
      print ('Choose which  conversions you would like to perform')
      print ('(1) Metric to Metric')
      print ('(2) Metric to Standard')
      print ('(3) Standard to Metric')
      conversion=input('Conversion from:')
      #try statement accepts only int values
      try:
          val=int(conversion)
      #if try is false, except will assign the value of val to be "-1"
      except: 
          val=-1
      #if the inputted value is int and is equals to "1", "ChooseMetric ()" def will be called
      if conversion=="1":
          ChooseMetric ()
      #if the inputted value is int and is equals to "2", "ChooseMet2Stand ()" def will be called
      elif conversion=="2":
          ChooseMet2Stand ()
      #if the inputted value is int and is equals to "3", "ChooseStand2Met ()" def will be called
      elif conversion=="3":
          ChooseStand2Met ()
      #if try is false, val will be equals to "-1" (not int) and the elif function below will execute
      elif val==-1:
          print ('')
          print ('ERR0R: The input must contain numbers only.')
      #if the value is neither a string or int value in the choices, the error below will be displayed
      else:
          print ('')
          print ('ERROR: Choice for conversion does not exist.')
#If the user pick Metric to Metric conversions, the def "ChooseMetric ()" will be called
def ChooseMetric ():
      #The following are the users' choices for conversion
      print ('')
      print ('Choose which Metric unit you want to conver to another.') 
      print ('(1) Centimeter to Millimeter')
      print ('(2) Millimeter to Centimeter')
      print ('(3) Meter to Centimeter')
      print ('(4) Centimeter to Meter')
      print ('(5) Kilometer to Meter')
      print ('(6) Meter to Kilometer')
      convert=input('Convert from:')
      #This section is the same with "ChooseConversion ()" def
      #This try/except statements is the same as the previous def to ensure that the value is not  string and is included
      #in the choices
      try:
          val=int(convert)
          print ('')
      except:
          val=-1
      if convert=="1": 
          print ('Note: Input only non-negative values only.')
          cm1=input('Centimeters:')
          #but since after choosing a conversion option, the value of the unit of measurement the users' want to convert
          #therefore we need to set another try/except statements to ensure that the value is valid (not a string nor a negative)
          try:
                cm2=float(cm1)
                print ('')
          
          except:
                cm2=-0            
          if cm2>0:
                z=cm2*10  
                print ('Millimeters:', z)
          elif cm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.') 
          else:
                print ('ERROR: Invalid value! Please try again!')
      #the same code logic is applied to the next set of "elif" statements
      elif convert=="2":
          print ('Note: Input only non-negative values only.')
          mm1=input('Millimeters:')
          try:
                mm2=float(mm1)
                print ('')
          
          except:
                mm2=-0  
          if mm2>0:
                z=mm2/10  
                print ('Centimeters:', z)
          elif mm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="3":
          print ('Note: Input only non-negative values only.')
          m1=input('Meters:')
          try:
                m2=float(m1)
                print ('')
          
          except:
                mm2=-0 
          if m2>0:
                z=m2*100  
                print ('Centimeters:', z)
          elif m2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="4":
          print ('Note: Input only non-negative values only.')
          cm1=input('Centimeters:')
          try:
                cm2=float(cm1)
                print ('')
          
          except:
                cm2=-0 
          if cm2>0:
                z=cm2/100  
                print ('Meters:', z)
          elif cm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="5":
          print ('Note: Input only non-negative values only.')
          km1=input('Kilometers:')
          try:
                km2=float(km1)
                print ('')
          
          except:
                km2=-0  
          if km2>0:
                z=km2*1000  
                print ('Meters:', z)
          elif km2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="6":
          print ('Note: Input only non-negative values only.')
          m1=input('Meters:')
          try:
                m2=float(m1)
                print ('')
          
          except:
                m2=-0 
          if m2>0:
                z=m2/1000  
                print ('Kilometers:', z)
          elif m2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      #part of the try/except statements that are responsible in displaying errors (same as "ChoooseConversion ()" def)
      elif val==-1:
          print ('')
          print ('ERR0R: The input must contain numbers only.')
      else:
          print ('ERROR: Choice for conversion does not exist.')     
      #after the conversion results are shown, if the user wish to convert again they can convert again 
      #"ChooseConversion ()" def is called again
      print ('')
      print (' SYSTEM NOTICE: Conversion success! If you wish to convert again enter a number, if not')
      print ('                                       exit the app')
      print ('')
      ChooseConversion ()
##If the user pick Metric to Standard conversions, the def "ChooseMetric ()" will be called
#The logic structure of this section is the same as "ChooseMetric ()"
def ChooseMet2Stand ():
      print ()
      print ('Choose which Metric unit you want to conver to Standard.') 
      print ('(1) Millimeter to Inch')
      print ('(2) Centimeter to Inch')
      print ('(3) Meter to Inch')
      print ('(4) Kilometer to Inch')
      print ('(5) Millimeter to Feet')
      print ('(6) Centimeter to Feet')
      print ('(7) Meter to Feet')
      print ('(8) Kilometer to Feet')
      print ('(9) Millimeter to Yard')
      print ('(10) Centimeter to Yard')
      print ('(11) Meter to Yard')
      print ('(12) Kilometer to Yard')
      print ('(13) Millimeter to Mile ')
      print ('(14) Centimeter to Mile')
      print ('(15) Meter to Mile')
      print ('(16) Kilometer to Mile')
      convert=input('Convert from:')
      try:
          val=int(convert)
          print ('')
      except:
          val=-1
      if convert=="1": 
          print ('Note: Input only non-negative values only.')
          mm1=input('Millimeters:')
          try:
                mm2=float(mm1)
                print ('')
          
          except:
                mm2=-0 
          if mm2>0:
                z=mm2*0.039 
                print ('Inches:', z)
          elif mm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="2":
          print ('Note: Input only non-negative values only.')
          cm1=input('Centimeters:')
          try:
                cm2=float(cm1)
                print ('')
          
          except:
                cm2=-0 
          if cm2>0:
                z=cm2*0.394
                print ('Inches:', z)
          elif cm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="3":
          print ('Note: Input only non-negative values only.')
          m1=input('Meters:')
          try:
                m2=float(m1)
                print ('')
          
          except:
                m2=-0  
          if m2>0:
                z=m2*39.47
                print ('Inches:', z)
          elif m2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')   
      elif convert=="4":
          print ('Note: Input only non-negative values only.')
          km1=input('Kilometers:')
          try:
                km2=float(km1)
                print ('')
          
          except:
                km2=-0  
          if km2>0:
                z=(km2*1000)*39.45
                print ('Inches:', z)
          elif km2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')  
      elif convert=="5":
          print ('Note: Input only non-negative values only.')
          mm1=input('Millimeters:')
          try:
                mm2=float(mm1)
                print ('')
          
          except:
                mm2=-0  
          if mm2>0:
                z=((mm2/10)/100)*3.281
                print ('Feet:', z)
          elif mm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')     
      elif convert=="6":
          print ('Note: Input only non-negative values only.')
          cm1=input('Centimeters:')
          try:
                cm2=float(cm1)
                print ('')
          
          except:
                cm2=-0  
          if cm2>0:
                z=(cm2/100)*3.281
                print ('Feet:', z)
          elif cm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="7":
          print ('Note: Input only non-negative values only.')
          m1=input('Meters:')
          try:
                m2=float(m1)
                print ('')
          
          except:
                m2=-0 
          if m2>0:
                z=m2*3.281
                print ('Feet:', z)
          elif m2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="8":
          print ('Note: Input only non-negative values only.')
          km1=input('Kilometers:')
          try:
                km2=float(km1)
                print ('')
          
          except:
                km2=-0  
          if km2>0:
                z=(km2*1000)*3.281
                print ('Feet:', z)
          elif km2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="9":
          print ('Note: Input only non-negative values only.')
          mm1=input('Millimeters:')
          try:
                mm2=float(mm1)
                print ('')
          
          except:
                mm2=-0 
          if mm2>0:
                z=((mm2/10)/100)*1.094
                print ('Yards:', z)
          elif mm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')     
      elif convert=="10":
          print ('Note: Input only non-negative values only.')
          cm1=input('Centimeters:')
          try:
                cm2=float(cm1)
                print ('')
          
          except:
                cm2=-0 
          if cm2>0:
                z=(cm2/100)*1.094
                print ('Yards:', z)
          elif cm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="11":
          print ('Note: Input only non-negative values only.')
          m1=input('Meters:')
          try:
                m2=float(m1)
                print ('')
          
          except:
                m2=-0  
          if m2>0:
                z=m2*1.094
                print ('Yards:', z)
          elif m2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="12":
          print ('Note: Input only non-negative values only.')
          km1=input('Kilometers:')
          try:
                km2=float(km1)
                print ('')
          
          except:
                km2=-0  
          if km2>0:
                z=(km2*1000)*1.094
                print ('Yards:', z)
          elif km2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="13":
          print ('Note: Input only non-negative values only.')
          mm1=input('Millimeters:')
          try:
                mm2=float(mm1)
                print ('')
          
          except:
                mm2=-0  
          if mm2>0:
                z=(((mm2/10)/100)/1000)*0.621
                print ('Miles:', z)
          elif mm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="14":
          print ('Note: Input only non-negative values only.')
          cm1=input('Centimeters:')
          try:
                cm2=float(cm1)
                print ('')
          
          except:
                cm2=-0  
          if cm2>0:
                z=((cm2/100)/1000)*0.621
                print ('Miles:', z)
          elif cm2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="15":
          print ('Note: Input only non-negative values only.')
          m1=input('Meters:')
          try:
                mm2=float(m1)
                print ('')
          
          except:
                m2=-0  
          if m2>0:
                z=(m2/1000)*0.621
                print ('Miles:', z)
          elif m2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="16":
          print ('Note: Input only non-negative values only.')
          km1=input('Kilometers:')
          try:
                km2=float(km1)
                print ('')
          
          except:
                km2=-0  
          if km2>0:
                z=km2*0.621
                print ('Miles:', z)
          elif km2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif val==-1:
          print ('')
          print ('ERR0R: The input must contain numbers only.')
      else:
          print ('ERROR: Choice for conversion does not exist.')     
      print ('')
      print (' SYSTEM NOTICE: Conversion success! If you wish to convert again enter a number, if not')
      print ('                                       exit the app')
      print ('')
      ChooseConversion ()
##If the user pick Standard to Metric conversions, the def "ChooseMetric ()" will be called
#The logic structure of this section is the same as "ChooseMetric ()"
def ChooseStand2Met ():
      print ()
      print ('Choose which Metric unit you want to conver to Standard.') 
      print ('(1) Inch to Millimeter')
      print ('(2) Feet to Millimeter')
      print ('(3) Yard to Millimeter')
      print ('(4) Mile to Millimeter')
      print ('(5) Inch to Centimeter')
      print ('(6) Feet to Centimeter')
      print ('(7) Yard to Centimeter')
      print ('(8) Mile to Centimeter')
      print ('(9) Inch to Meter')
      print ('(10) Feet to Meter')
      print ('(11) Yard to Meter')
      print ('(12) Mile to Meter')
      print ('(13) Inch to Kilometer ')
      print ('(14) Feet to Kilometer')
      print ('(15) Yard to Kilometer')
      print ('(16) Mile to Kilometer')
      convert=input('Convert from:')
      try:
          val=int(convert)
          print ('')
      except:
          val=-1
      if convert=="1": 
          print ('Note: Input only non-negative values only.')
          in1=input('Inches:')
          try:
                in2=float(in1)
                print ('')
          
          except:
                in2=-0 
          if in2>0:
                z=(in2*2.54)*10
                print ('Millimeters:', z)
          elif in2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="2": 
          print ('Note: Input only non-negative values only.')
          ft1=input('Feet:')
          try:
                ft2=float(ft1)
                print ('')
          
          except:
                ft2=-0  
          if ft2>0:
                z=(ft2*30.48)*10
                print ('Millimeters:', z)
          elif ft2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="3": 
          print ('Note: Input only non-negative values only.')
          yd1=input('Yards:')
          try:
                yd2=float(yd1)
                print ('')
          
          except:
                yd2=-0 
          if yd2>0:
                z=(yd2*91.44)*10
                print ('Millimeters:', z)
          elif yd2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="4": 
          print ('Note: Input only non-negative values only.')
          mi1=input('Feet:')
          try:
                mi2=float(mi1)
                print ('')
          
          except:
                mi2=-0  
          if mi2>0:
                z=(((mi2*1609.3)*100)*10)
                print ('Millimeters:', z)
          elif mi2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      if convert=="5": 
          print ('Note: Input only non-negative values only.')
          in1=input('Inches:')
          try:
                in2=float(in1)
                print ('')
          
          except:
                in2=-0 
          if in2>0:
                z=(in2*2.54)
                print ('Centimeters:', z)
          elif in2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="6": 
          print ('Note: Input only non-negative values only.')
          ft1=input('Feet:')
          try:
                ft2=float(ft1)
                print ('')
          
          except:
                ft2=-0 
          if ft2>0:
                z=(ft2*30.48)
                print ('Centimeters:', z)
          elif ft2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="7": 
          print ('Note: Input only non-negative values only.')
          yd1=input('Yards:')
          try:
                yd2=float(yd1)
                print ('')
          
          except:
                yd2=-0  
          if yd2>0:
                z=(yd2*91.44)
                print ('Centimeters:', z)
          elif yd2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="8": 
          print ('Note: Input only non-negative values only.')
          mi1=input('Miles:')
          try:
                mi2=float(mi1)
                print ('')
          
          except:
                mi2=-0  
          if mi2>0:
                z=((mi2*1609.3)*100)
                print ('Centimeters:', z)
          elif mi2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      if convert=="9": 
          print ('Note: Input only non-negative values only.')
          in1=input('Inches:')
          try:
                in2=float(in1)
                print ('')
          
          except:
                in2=-0  
          if in2>0:
                z=(in2*2.54)*100
                print ('Centimeters:', z)
          elif in2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="10": 
          print ('Note: Input only non-negative values only.')
          ft1=input('Feet:')
          try:
                ft2=float(ft1)
                print ('')
          
          except:
                ft2=-0 
          if ft2>0:
                z=(ft2*30.48)*100
                print ('Centimeters:', z)
          elif ft2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="11": 
          print ('Note: Input only non-negative values only.')
          yd1=input('Yards:')
          try:
                yd2=float(yd1)
                print ('')
          
          except:
                yd2=-0  
          if yd2>0:
                z=yd2*0.914
                print ('Centimeters:', z)
          elif yd2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="12": 
          print ('Note: Input only non-negative values only.')
          mi1=input('Miles:')
          try:
                mi2=float(mi1)
                print ('')
          
          except:
                mi2=-0  
          if mi2>0:
                z=(mi2*1609.3)
                print ('Meters:', z)
          elif mi2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      if convert=="13": 
          print ('Note: Input only non-negative values only.')
          in1=input('Inches:')
          try:
                in2=float(in1)
                print ('')
          
          except:
                in2=-0  
          if in2>0:
                z=((in2*2.54)*100)*1000
                print ('Kilometers:', z)
          elif in2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="14": 
          print ('Note: Input only non-negative values only.')
          ft1=input('Feet:')
          try:
                ft2=float(ft1)
                print ('')
          
          except:
                ft2=-0  
          if ft2>0:
                z=((ft2*30.48)*100)*1000
                print ('Kilometers:', z)
          elif ft2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="15": 
          print ('Note: Input only non-negative values only.')
          yd1=input('Yards:')
          try:
                yd2=float(yd1)
                print ('')
          
          except:
                yd2=-0 
          if yd2>0:
                z=((yd2*91.44)*100)*1000
                print ('Kilometers:', z)
          elif yd2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!')
      elif convert=="16": 
          print ('Note: Input only non-negative values only.')
          mi1=input('Miles:')
          try:
                mi2=float(mi1)
                print ('')
          
          except:
                mi2=-0 
          if mi2>0:
                z=mi2*1.609
                print ('Kilometers:', z)
          elif mi2==-0:
                print ("")
                print('ERROR: Input must contain numbers only.')
          else:
                print ('ERROR: Invalid value! Please try again!') 
      elif val==-1:
          print ('')
          print ('ERR0R: The input must contain numbers only.')
      else:
          print ('ERROR: Choice for conversion does not exist')     
      print ('')
      print (' SYSTEM NOTICE: Conversion success! If you wish to convert again enter a number, if not')
      print ('                                       exit the app')
      print ('')
      ChooseConversion ()
#The following code will retrive and run the 'ChooseConversion ()' def to start the whole program     
ChooseConversion ()




