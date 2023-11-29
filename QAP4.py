# Comment like a pro.
 
# Import required libraries.
import datetime
import FormatValues as FV

# Set up program constants.
NEXT_POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
ADDITIONAL_CAR_DISCOUNT = 0.25
EXTRA_LIABILITY_RATE = 130.00
COST_GLASS_COVERAGE = 86.00
COST_LOANER_CAR = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99


# Set up program functions.

def PremiumCalc(NumCars):
    # a function to comute the insurance premiums based on the number of cars and other options
    InsurancePremiums = BASIC_PREMIUM + (BASIC_PREMIUM * (1-ADDITIONAL_CAR_DISCOUNT) * (NumCars - 1))
    AdditionalLiabilityCost = 0
    GlassCoverageCost = 0
    LoanerCarCost = 0
    if ExtraLiability == "Y":
        AdditionalLiabilityCost = (EXTRA_LIABILITY_RATE * NumCars)
        InsurancePremiums += AdditionalLiabilityCost
    if GlassCoverage == "Y":
        GlassCoverageCost = (COST_GLASS_COVERAGE * NumCars)
        InsurancePremiums += GlassCoverageCost
    if LoanerCar == "Y":
        LoanerCarCost = (COST_LOANER_CAR * NumCars)
        InsurancePremiums += LoanerCarCost
    return InsurancePremiums, AdditionalLiabilityCost, GlassCoverageCost, LoanerCarCost

def MonthlyPaymentCalc(TotalCost):
    if PaymentType == "DOWNPAY":
        MonthlyInsPrem = (TotalCost - DownPayAMT + PROCESSING_FEE)/8
    else:
        MonthlyInsPrem = (TotalCost + PROCESSING_FEE)/8
    return MonthlyInsPrem




 
# Inputs and validations
while True: 
    while True:
        FirstName = input("Please enter the customer's first name: ").title()
        if FirstName == "":
            print("The first name cannot be blank - please re-enter")
        else:
            break
    while True:
        LastName = input("Please enter the customer's last name: ").title()
        if LastName == "":
            print("The last name cannot be blank - please re-enter")
        else:
            break
    while True:
        StAdd = input("Please enter the clients street address: ")
        if StAdd == "":
            print("The street address cannot be blank - please re-enter")
        else:
            break
    while True:
        City = input("Please enter the customer's city: ").title()
        if City == "":
            print("The city name cannot be blank - please re-enter")
        else:
            break
    ProvList = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
    while True:
        Prov = input("Please enter the province of residence abbreviation for the client (XX): ").upper()
        if Prov not in ProvList:
            print("You have entered an invalid province code - please re-enter")
        else:
            break
    while True:
        PostCode = input("Please enter the postal code of the client: " ).upper()
        if PostCode == "":
            print("The postal code cannot be blank - please re-enter")
        elif PostCode.isalnum() != True:
            print("The postal code entered contains invalid characters - please re-enter")
        elif len(PostCode) != 6:
            print("The postal code must be 6 characters - please re-enter")
        else:
            break
    while True:
        PhoneNum = input("Please enter the phone number of the client: " )
        if PhoneNum == "":
            print("The phone number cannot be blank - please re-enter")
        elif PhoneNum.isdigit() != True:
            print("The phone number entered contains invalid characters - please re-enter")
        elif len(PhoneNum) != 10:
            print("The phone number must be 10 digits - please re-enter")
        else:
            break
    while True:
        try: 
            NumCars = int(input("Please enter the number of cars to be insured: "))
        except:
            print("You have entered an invalid character for the number of cars - please re-enter")
        else:
            if NumCars <= 0:
                print("The number of cars must be greater than 0 - please re-enter")
            else:
                break
    while True:
        ExtraLiability = input("Please enter Y or N to indicate if the client would like extra liability coverage: ").upper()
        if ExtraLiability == "":
            print("The extra liability field cannot be blank - please re-enter")
        elif ExtraLiability != "Y" and ExtraLiability != "N":
            print("You have made an invalid selection - please re-enter")
        else:
            break
    while True:
        GlassCoverage = input("Please enter Y or N to indicate if the client would like glass coverage: ").upper()
        if GlassCoverage == "":
            print("The glass coverage field cannot be blank - please re-enter")
        elif GlassCoverage != "Y" and GlassCoverage != "N":
            print("You have made an invalid selection - please re-enter")
        else:
            break
    while True:
        LoanerCar = input("Please enter Y or N to indicate if the client would like a loaner car option: ").upper()
        if LoanerCar == "":
            print("The loaner car field cannot be blank - please re-enter")
        elif LoanerCar != "Y" and LoanerCar != "N":
            print("You have made an invalid selection - please re-enter")
        else:
            break
    PaymentTypeLST = ["FULL", "MONTHLY", "DOWNPAY"]
    while True:
        PaymentType = input("Please enter the payment type (Full, Monthly, Downpay): ").upper()
        if PaymentType not in PaymentTypeLST:
            print("The payment type specified is invalid - please re-enter")
        else:
            break
    if PaymentType == "DOWNPAY":
        while True:       
            try:
                DownPayAMT = float(input("Please enter the amount of the downpayment to be applied to premium costs: "))
            except:
                print("you have indicated a downpayment that is invalid - please re-enter")
            else: 
                if DownPayAMT < 0:
                    print("you have specified an invalid downpayment amount - please re-enter")
                else: 
                    break
    ClaimLST = []
    ClaimDateLST = []
    IncrementVar = 0
    while True:
        ClaimAMT = input("Enter the prior claim amount price (ENTER to end): ")
        if ClaimAMT == "":
            break
        ClaimDate = input("Enter the priot claim date (YYYY-MM-DD): ")
        ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
        ClaimDateDSP = ClaimDate.strftime("%B %d, %Y")
        IncrementVar += 1
 
        ClaimLST.append(ClaimAMT)
        ClaimDateLST.append(ClaimDateDSP)

    #processing the inputs using functions

    #Calling main functions for processing:
    BasicCharge = BASIC_PREMIUM + (BASIC_PREMIUM * (1-ADDITIONAL_CAR_DISCOUNT) * (NumCars - 1))
    ChargeList = PremiumCalc(NumCars) #creating a tuple to work with
    HST = ChargeList[0] * HST_RATE
    TotalCost = ChargeList[0] + HST
    PaymentDue = MonthlyPaymentCalc(TotalCost)

   #printing out results
    print()
    print(f"                                One Stop Insurance Company")
    print(f"                                    Customer Reciept")
    print(f"------------------------------------------------------------------------------------")
    CustFullName = FirstName + " " + LastName
    CurDate = datetime.datetime.now()#fetching todays date
    CurYear = CurDate.year
    CurMonth = CurDate.month
    CurDay = CurDate.day
    CurDateDSP = datetime.date(CurYear, CurMonth , CurDay)
    print(f"Customer Name:  {CustFullName:<25s}                   Invoice Date: {CurDateDSP}")
    print(f"Customer Address:")
    print(f"Street Address: {StAdd:<20s}   Postal Code: {PostCode:<6s}")
    print(f"City: {City:<15s}     Province: {Prov:<2s}")
    FPhoneNum = FV.FPhoneNum(PhoneNum)#my third function is a format function for phonenumber
    print(f"Phone Number: {FPhoneNum:<13s}")
    print(f"------------------------------------------------------------------------------------")
    print(f"Coverage Information: ")
    print(f"---------------------")
    print(f"Number of vehicles:                                                               {NumCars:>2d}")
    if ExtraLiability == "Y":
        print(f"Extra Liability Coverage?                                                        Yes")
    else:
        print(f"Extra Liability Coverage?                                                         No")
    if GlassCoverage == "Y":
        print(f"Glass Coverage?                                                                  Yes")
    else:
        print(f"Glass Coverage?                                                                   No")
    if LoanerCar == "Y":
        print(f"Loaner Car Coverage?                                                             Yes")
    else:
        print(f"Loaner Car Coverage?                                                              No")
    print(f"Paymanet Information")
    print(f"--------------------")
    if PaymentType == "FULL":
        print(f"Payment type?                                                   One Time Full Payment")
    elif PaymentType == "MONTHLY":
        print(f"Payment type?                                     Monthly Payment Without Downpayment")
    else:
        print(f"Payment type?                                        Monthly Payment With Downpayment")
    print(f"-------------------------------------------------------------------------------------")
    BasicChargeDSP = FV.FComma2(BasicCharge)
    print(f"Basic charge for {NumCars:>2d} vehicles:                                               {BasicChargeDSP:>9s}")
    print(f"-------------------------------------------------------------------------------------")
    print(f"")
    print(f"Additional Costs:")
    print(f"-----------------")
    ExtraLiabilityDSP = FV.FDollar2(ChargeList[1])
    print(f"Extra Liability:                                                            {ExtraLiabilityDSP:>9s}")
    GlassCoverageDSP = FV.FDollar2(ChargeList[2])
    print(f"Extra Liability:                                                            {GlassCoverageDSP:>9s}")
    LoanerCarDSP = FV.FDollar2(ChargeList[3])
    print(f"Extra Liability:                                                            {LoanerCarDSP:>9s}")
    print(f"-------------------------------------------------------------------------------------")
    print(f"Addition of basic and additional Charges:")
    print(f"--------------")
    TotalPremiumDsp = FV.FComma2(ChargeList[0])
    print(f"Full cost of premium before taxes:                                          {TotalPremiumDsp:>9s}")
    HSTDSP = FV.FComma2(HST)
    print(f"Sales Tax (HST):                                                            {HSTDSP:>9s}")
    TotalCostDSP = FV.FComma2(TotalCost)
    print(f"Total cost of premium if paid in full:                                      {TotalCostDSP:>9s}")
    print(f"-------------------------------------------------------------------------------------")
    if PaymentType == "DOWNPAY":
        print(f"Downpayment:                                                                {FV.FComma2(DownPayAMT):>9s}")
    print(f"Monthly premium:                                                            {FV.FComma2(PaymentDue):>9s}")
    print(f"-------------------------------------------------------------------------------------")
    # New date first of next month
    CurDate = datetime.datetime.now()
    CurYear = CurDate.year
    CurMonth = CurDate.month
    FirstOfNextMonth = datetime.date(CurYear, CurMonth + 1, 1)
    print(FirstOfNextMonth)
    print(f"First Payment Due:                                                  {FirstOfNextMonth}")

    print()
    print(f"                          Prior Claim Information")
    print(f"           Claim Number             ClaimDate            Claim Amount")
    #prior claim information
    for i in range(0,IncrementVar):
        print(f"               {i+1}.                  {ClaimDateLST[i]}             {ClaimLST[i]}")

   #to end the program
   
   
    while True:
        Continue = input("Do you want to process another insurance client (Y / N): ").upper()
 
        if Continue == "":
            print("Continue cannot be blank - please re-enter.")
        elif Continue != "Y" and Continue != "N":
            print("Continue must be a Y or an N - please re-enter.")
        else:
            break
    
    if Continue == "N":
        break
