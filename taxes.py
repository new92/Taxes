"Germany" == 2575
"Switzerland" == 3892
"Sweden" == 1583
"USA" == 5115
"Russia" == 6179
"China" == 7229
"Australia" == 4408
"Canada" == 6028
"Austria" == 9481
"France" == 8305
"United_Kingdom" == 3873
"Japan" == 7592
"Italy" == 1047
"Belgium" == 5793
countries=["Germany","Switzerland","Sweden","USA","Russia","China","Australia","Canada","Austria","France","UK","Japan","Italy","Belgium"] 
countries_codes=["2575","3892","1583","3915","6179","7229","4408","6028","9481","8305","3873","7592","1047","5793"] 
for i in range(len(countries)): 
	print(countries[i],countries_codes[i])  
first_name=input("Please insert your first name: ")
last_name=input("Please insert your last name: ")
country_code=int(input("Please insert your country code: "))
incomes=int(input("Please insert your incomes: "))
#Germany
if country_code == 2575 and incomes <= 9984:
    tax_de_0 = 0
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_de_0)
elif country_code == 2575 and incomes <= 58596:
    tax_de_14=incomes*0.14
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_de_14)
elif country_code == 2575 and incomes <= 277825:
    tax_de_42=incomes*0.42
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_de_42)
elif country_code == 2575 and incomes >=277826:
    tax_de_45=incomes*0.45
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_de_45)
#Switzerland
elif country_code == 3892 and incomes <= 14500:
    tax_switz_0 = 0
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_switz_0)
elif country_code == 3892 and incomes <= 55200:
    tax_switz_2=incomes*0.2
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_switz_2)
elif country_code == 3892 and incomes <= 78100:
    tax_switz_5=incomes*0.5
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_switz_5)
elif country_code == 3892 and incomes <= 103600:
    tax_switz_6=incomes*0.6
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_switz_6)
elif country_code == 3892 and incomes <= 134600:
    tax_switz_8=incomes*0.8
    print(first_name,"The amount of money which you'll pay in taxes is this: ",tax_switz_8)
elif country_code == 3892 and incomes <= 176600:
    tax_switz_11=incomes*0.11
    print(first_name,"The amount of money which you'll pay in taxes is this: ",tax_switz_11)
elif country_code == 3892 and incomes <= 755200:
    tax_switz_13=incomes*0.13
    print(first_name,"The amount of money which you'll pay in taxes is this: ",tax_switz_13)
#Sweden
elif country_code == 1583 and incomes <= 19247:
    tax_sweden_0 = 0
    print(first_name,"The amount of money which you'll pay in taxes is this: ",tax_sweden_0)
elif country_code == 1583 and incomes <= 455300:
    tax_sweden_29=incomes*0.29
    print(first_name,"The amount of money which you'll pay in taxes is this: ",tax_sweden_29)
elif country_code == 1583 and incomes >= 662300:
    tax_sweden_35=incomes*0.35
    print(first_name,"The amount of money which you'll pay in taxes is this: ",tax_sweden_35)
#USA
elif country_code == 5115 and incomes <= 9700:
    tax_usa_10=incomes*0.10
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_usa_10)
elif country_code == 5115 and incomes <= 39475:
    tax_usa_12=incomes*0.12
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_usa_12)
elif country_code == 5115 and incomes <= 84200:
    tax_usa_22=incomes*0.22
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_usa_22)
elif country_code == 5115 and incomes <= 160725:
    tax_usa_24=incomes*0.24
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_usa_24)
elif country_code == 5115 and incomes <= 200000:
    tax_usa_32=incomes*0.32
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_usa_32)
elif country_code == 5115 and incomes <= 500000:
    tax_usa_35=incomes*0.35
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_usa_35)
elif country_code == 5115 and incomes > 500001:
    tax_usa_35=incomes*0.37
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_usa_37)
#Russia
elif country_code == 6179 and incomes <= 300000:
    tax_russia_1=incomes*0.1
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_russia_1)
elif country_code == 6179 and incomes <= 500000:
    tax_russia_2=incomes*0.2
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_russia_2)
elif country_code == 6179 and incomes > 500000:
    tax_russia_3=incomes*0.3
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_russia_3) 
#China
elif country_code == 7229 and incomes <= 12000:
    tax_china_10=incomes*0.10
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_china_10)
elif country_code == 7229 and incomes <= 25000:
    tax_china_20=incomes*0.20
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_china_20)
elif country_code == 7229 and incomes <= 35000:
    tax_china_25=incomes*0.35
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_china_25)
elif country_code == 7229 and incomes <= 55000:
    tax_china_30=incomes*0.30
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_china_30)
elif country_code == 7229 and incomes <= 80000:
    tax_china_35=incomes*0.35
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_china_35)
elif country_code == 7229 and incomes > 80000:
    tax_china_45=incomes*0.45
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_china_45)
#Australia
elif country_code == 4408 and incomes <= 18200:
    tax_austr_0 = 0
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austr_0)
elif country_code == 4408 and incomes <= 37000:
    tax_austr_19=incomes*0.19
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austr_19)
elif country_code == 4408 and incomes <= 90000:
    tax_austr_32=incomes*0.32
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austr_32)
elif country_code == 4408 and incomes <= 180000:
    tax_austr_37=incomes*0.37
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austr_37)
#Canada
elif country_code == 6028 and incomes <= 49020:
    tax_can_20=incomes*0.20
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_can_20)
elif country_code == 6208 and incomes <= 53939:
    tax_can_26=incomes*0.26
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_can_26)
elif country_code == 6208 and incomes <= 64533:
    tax_can_29=incomes*0.29
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_can_29)
elif country_code == 6208 and incomes <= 216511:
    tax_can_33=incomes*0.33
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_can_33)
elif country_code == 6208 and incomes > 216512:
    tax_can_34=incomes*0.34
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_can_34) 
#Austria
elif country_code == 9481 and incomes <=11000:
    tax_austria_0 = 0
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austria_0)
elif country_code == 9481 and incomes <=18000:
    tax_austria_25=incomes*0.25
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austria_25)
elif country_code == 9481 and incomes <= 31000:
    tax_austria_35=incomes*0.35
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austria_35)
elif country_code == 9481 and incomes <= 60000:
    tax_austria_42=incomes*0.42
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_austria_42)
#France
elif country_code == 8305 and incomes <= 9964:
    tax_fr_0 = 0
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_fr_0)
elif country_code == 8305 and incomes <= 27519:
    tax_fr_14=incomes*0.14
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_fr_14)
elif country_code == 8305 and incomes <= 73779:
    tax_fr_30=incomes*0.30
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_fr_30)
elif country_code == 8305 and incomes <= 156244:
    tax_fr_41=incomes*0.41
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_fr_41)
elif country_code == 8305 and incomes > 156245:
    tax_fr_45=incomes*0.45
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_fr_4)
#United_Kingdom
elif country_code == 3873 and incomes <= 12570:
    tax_uk_0 = 0
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_uk_0)
elif country_code == 3873 and incomes <= 50270:
    tax_uk_20=incomes*0.20
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_uk_20)
elif country_code == 3873 and incomes <= 150000:
    tax_uk_40=incomes*0.40
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_uk_40)
elif country_code == 3873 and incomes > 150001:
    tax_uk_45=incomes*0.45
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_uk_45)
#Japan
elif country_code == 7592 and incomes <= 14853:
    tax_jp_5=incomes*0.5
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_jp_5)
elif country_code == 7592 and incomes <= 25136:
    tax_jp_10=incomes*0.10
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_jp_10)
elif country_code == 7592 and incomes <= 52938:
    tax_jp_20=incomes*0.20
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_jp_20)
elif country_code == 7592 and incomes <= 68553:
    tax_jp_23=incomes*0.23
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_jp_23)
elif country_code == 7592 and incomes <= 137106:
    tax_jp_33=incomes*0.33
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_jp_33)
elif country_code == 7592 and incomes <= 304680:
    tax_jp_40=incomes*0.40
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_jp_40)
elif country_code == 7592 and incomes > 304681:
    tax_jp_45=incomes*0.45
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_jp_45)
#Italy
elif country_code == 1047 and incomes <= 15000:
    tax_it_23=incomes*0.23
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_it_23)
elif country_code == 1047 and incomes <= 28000:
    tax_it_27=incomes*0.27
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_it_27)
elif country_code == 1047 and incomes <= 55000:
    tax_it_38=incomes*0.38
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_it_38)
elif country_code == 1047 and incomes <= 75000:
    tax_it_41=incomes*0.41
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_it_41)
elif country_code == 1047 and incomes > 75000:
    tax_it_43=incomes*0.43
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_it_43) 
#Belgium
elif country_code == 5793 and incomes <= 13540:
    tax_bel_25=incomes*0.25
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_bel_25)
elif country_code == 5793 and incomes <= 23900:
    tax_bel_40=incomes*0.40
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_bel_40)
elif country_code == 5793 and incomes <= 41360:
    tax_bel_45=incomes*45
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_bel_45)
elif country_code == 5793 and incomes > 41360:
    tax_bel_50=incomes*50
    print(first_name,"the amount of money which you'll pay in taxes is this: ",tax_bel_50)
