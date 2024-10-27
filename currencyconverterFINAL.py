# practice run 
    # :list
    # :convert
            #base currency: usd
            #...amount in USD: 1000
            #....currency to convert to: GBP
                #RESULT:
    # :rate
            # usd
            # gbp
                #RESULT:

#----------------------------------------# --> MAIN
#interum api key: https://app.exchangerate-api.com
# https://app.exchangerate-api.com/dashboard/confirmed

#----------------------------------------# --> MAIN
from requests import get

BASE_URL = "https://v6.exchangerate-api.com/v6/"
API_KEY = " "


# hardcoded currencies so I could print the full name and symobls of each (...just makes it easier since the api doesnt give these)
currency_info = {
    "USD": {"name": "United States Dollar", "symbol": "$"},
    "AED": {"name": "United Arab Emirates Dirham", "symbol": "د.إ"},
    "AFN": {"name": "Afghan Afghani", "symbol": "؋"},
    "ALL": {"name": "Albanian Lek", "symbol": "L"},
    "AMD": {"name": "Armenian Dram", "symbol": "֏"},
    "ANG": {"name": "Netherlands Antillean Guilder", "symbol": "ƒ"},
    "AOA": {"name": "Angolan Kwanza", "symbol": "Kz"},
    "ARS": {"name": "Argentine Peso", "symbol": "$"},
    "AUD": {"name": "Australian Dollar", "symbol": "A$"},
    "AWG": {"name": "Aruban Florin", "symbol": "ƒ"},
    "AZN": {"name": "Azerbaijani Manat", "symbol": "₼"},
    "BAM": {"name": "Bosnia-Herzegovina Convertible Mark", "symbol": "KM"},
    "BBD": {"name": "Barbadian Dollar", "symbol": "Bds$"},
    "BDT": {"name": "Bangladeshi Taka", "symbol": "৳"},
    "BGN": {"name": "Bulgarian Lev", "symbol": "лв"},
    "BHD": {"name": "Bahraini Dinar", "symbol": ".د.ب"},
    "BIF": {"name": "Burundian Franc", "symbol": "FBu"},
    "BMD": {"name": "Bermudian Dollar", "symbol": "$"},
    "BND": {"name": "Brunei Dollar", "symbol": "B$"},
    "BOB": {"name": "Bolivian Boliviano", "symbol": "Bs."},
    "BRL": {"name": "Brazilian Real", "symbol": "R$"},
    "BSD": {"name": "Bahamian Dollar", "symbol": "$"},
    "BTN": {"name": "Bhutanese Ngultrum", "symbol": "Nu."},
    "BWP": {"name": "Botswana Pula", "symbol": "P"},
    "BYN": {"name": "Belarusian Ruble", "symbol": "Br"},
    "BZD": {"name": "Belize Dollar", "symbol": "BZ$"},
    "CAD": {"name": "Canadian Dollar", "symbol": "C$"},
    "CDF": {"name": "Congolese Franc", "symbol": "FC"},
    "CHF": {"name": "Swiss Franc", "symbol": "CHF"},
    "CLP": {"name": "Chilean Peso", "symbol": "$"},
    "CNY": {"name": "Chinese Yuan", "symbol": "¥"},
    "COP": {"name": "Colombian Peso", "symbol": "$"},
    "CRC": {"name": "Costa Rican Colón", "symbol": "₡"},
    "CUP": {"name": "Cuban Peso", "symbol": "$"},
    "CVE": {"name": "Cape Verdean Escudo", "symbol": "$"},
    "CZK": {"name": "Czech Koruna", "symbol": "Kč"},
    "DJF": {"name": "Djiboutian Franc", "symbol": "Fdj"},
    "DKK": {"name": "Danish Krone", "symbol": "kr"},
    "DOP": {"name": "Dominican Peso", "symbol": "RD$"},
    "DZD": {"name": "Algerian Dinar", "symbol": "د.ج"},
    "EGP": {"name": "Egyptian Pound", "symbol": "£"},
    "ERN": {"name": "Eritrean Nakfa", "symbol": "Nfk"},
    "ETB": {"name": "Ethiopian Birr", "symbol": "Br"},
    "EUR": {"name": "Euro", "symbol": "€"},
    "FJD": {"name": "Fijian Dollar", "symbol": "FJ$"},
    "FKP": {"name": "Falkland Islands Pound", "symbol": "£"},
    "FOK": {"name": "Faroese Króna", "symbol": "kr"},
    "GBP": {"name": "British Pound Sterling", "symbol": "£"},
    "GEL": {"name": "Georgian Lari", "symbol": "₾"},
    "GGP": {"name": "Guernsey Pound", "symbol": "£"},
    "GHS": {"name": "Ghanaian Cedi", "symbol": "₵"},
    "GIP": {"name": "Gibraltar Pound", "symbol": "£"},
    "GMD": {"name": "Gambian Dalasi", "symbol": "D"},
    "GNF": {"name": "Guinean Franc", "symbol": "FG"},
    "GTQ": {"name": "Guatemalan Quetzal", "symbol": "Q"},
    "GYD": {"name": "Guyanese Dollar", "symbol": "$"},
    "HKD": {"name": "Hong Kong Dollar", "symbol": "HK$"},
    "HNL": {"name": "Honduran Lempira", "symbol": "L"},
    "HRK": {"name": "Croatian Kuna", "symbol": "kn"},
    "HTG": {"name": "Haitian Gourde", "symbol": "G"},
    "HUF": {"name": "Hungarian Forint", "symbol": "Ft"},
    "IDR": {"name": "Indonesian Rupiah", "symbol": "Rp"},
    "ILS": {"name": "Israeli New Shekel", "symbol": "₪"},
    "IMP": {"name": "Isle of Man Pound", "symbol": "£"},
    "INR": {"name": "Indian Rupee", "symbol": "₹"},
    "IQD": {"name": "Iraqi Dinar", "symbol": "ع.د"},
    "IRR": {"name": "Iranian Rial", "symbol": "﷼"},
    "ISK": {"name": "Icelandic Króna", "symbol": "kr"},
    "JEP": {"name": "Jersey Pound", "symbol": "£"},
    "JMD": {"name": "Jamaican Dollar", "symbol": "J$"},
    "JOD": {"name": "Jordanian Dinar", "symbol": "د.ا"},
    "JPY": {"name": "Japanese Yen", "symbol": "¥"},
    "KES": {"name": "Kenyan Shilling", "symbol": "KSh"},
    "KGS": {"name": "Kyrgyzstani Som", "symbol": "лв"},
    "KHR": {"name": "Cambodian Riel", "symbol": "៛"},
    "KID": {"name": "Kiribati Dollar", "symbol": "$"},
    "KMF": {"name": "Comorian Franc", "symbol": "CF"},
    "KRW": {"name": "South Korean Won", "symbol": "₩"},
    "KWD": {"name": "Kuwaiti Dinar", "symbol": "د.ك"},
    "KYD": {"name": "Cayman Islands Dollar", "symbol": "$"},
    "KZT": {"name": "Kazakhstani Tenge", "symbol": "₸"},
    "LAK": {"name": "Lao Kip", "symbol": "₭"},
    "LBP": {"name": "Lebanese Pound", "symbol": "ل.ل"},
    "LKR": {"name": "Sri Lankan Rupee", "symbol": "Rs"},
    "LRD": {"name": "Liberian Dollar", "symbol": "$"},
    "LSL": {"name": "Lesotho Loti", "symbol": "L"},
    "LYD": {"name": "Libyan Dinar", "symbol": "ل.د"},
    "MAD": {"name": "Moroccan Dirham", "symbol": "د.م."},
    "MDL": {"name": "Moldovan Leu", "symbol": "L"},
    "MGA": {"name": "Malagasy Ariary", "symbol": "Ar"},
    "MKD": {"name": "Macedonian Denar", "symbol": "ден"},
    "MMK": {"name": "Myanmar Kyat", "symbol": "K"},
    "MNT": {"name": "Mongolian Tögrög", "symbol": "₮"},
    "MOP": {"name": "Macanese Pataca", "symbol": "MOP$"},
    "MRU": {"name": "Mauritanian Ouguiya", "symbol": "UM"},
    "MUR": {"name": "Mauritian Rupee", "symbol": "₨"},
    "MVR": {"name": "Maldivian Rufiyaa", "symbol": "Rf"},
    "MWK": {"name": "Malawian Kwacha", "symbol": "MK"},
    "MXN": {"name": "Mexican Peso", "symbol": "$"},
    "MYR": {"name": "Malaysian Ringgit", "symbol": "RM"},
    "MZN": {"name": "Mozambican Metical", "symbol": "MT"},
    "NAD": {"name": "Namibian Dollar", "symbol": "$"},
    "NGN": {"name": "Nigerian Naira", "symbol": "₦"},
    "NIO": {"name": "Nicaraguan Córdoba", "symbol": "C$"},
    "NOK": {"name": "Norwegian Krone", "symbol": "kr"},
    "NPR": {"name": "Nepalese Rupee", "symbol": "₨"},
    "NZD": {"name": "New Zealand Dollar", "symbol": "NZ$"},
    "OMR": {"name": "Omani Rial", "symbol": "﷼"},
    "PAB": {"name": "Panamanian Balboa", "symbol": "B/."},
    "PEN": {"name": "Peruvian Sol", "symbol": "S/."},
    "PGK": {"name": "Papua New Guinean Kina", "symbol": "K"},
    "PHP": {"name": "Philippine Peso", "symbol": "₱"},
    "PKR": {"name": "Pakistani Rupee", "symbol": "₨"},
    "PLN": {"name": "Polish Złoty", "symbol": "zł"},
    "PYG": {"name": "Paraguayan Guaraní", "symbol": "₲"},
    "QAR": {"name": "Qatari Riyal", "symbol": "﷼"},
    "RON": {"name": "Romanian Leu", "symbol": "lei"},
    "RSD": {"name": "Serbian Dinar", "symbol": "дин."},
    "RUB": {"name": "Russian Ruble", "symbol": "₽"},
    "RWF": {"name": "Rwandan Franc", "symbol": "FRw"},
    "SAR": {"name": "Saudi Riyal", "symbol": "﷼"},
    "SBD": {"name": "Solomon Islands Dollar", "symbol": "$"},
    "SCR": {"name": "Seychellois Rupee", "symbol": "₨"},
    "SDG": {"name": "Sudanese Pound", "symbol": "ج.س."},
    "SEK": {"name": "Swedish Krona", "symbol": "kr"},
    "SGD": {"name": "Singapore Dollar", "symbol": "S$"},
    "SHP": {"name": "Saint Helena Pound", "symbol": "£"},
    "SLE": {"name": "Sierra Leonean Leone", "symbol": "Le"},
    "SLL": {"name": "Sierra Leonean Leone", "symbol": "Le"},
    "SOS": {"name": "Somali Shilling", "symbol": "Sh"},
    "SRD": {"name": "Surinamese Dollar", "symbol": "$"},
    "SSP": {"name": "South Sudanese Pound", "symbol": "£"},
    "STN": {"name": "São Tomé and Príncipe Dobra", "symbol": "Db"},
    "SYP": {"name": "Syrian Pound", "symbol": "£"},
    "SZL": {"name": "Eswatini Lilangeni", "symbol": "E"},
    "THB": {"name": "Thai Baht", "symbol": "฿"},
    "TJS": {"name": "Tajikistani Somoni", "symbol": "ЅМ"},
    "TMT": {"name": "Turkmenistani Manat", "symbol": "m"},
    "TND": {"name": "Tunisian Dinar", "symbol": "د.ت"},
    "TOP": {"name": "Tongan Paʻanga", "symbol": "T$"},
    "TRY": {"name": "Turkish Lira", "symbol": "₺"},
    "TTD": {"name": "Trinidad and Tobago Dollar", "symbol": "TT$"},
    "TVD": {"name": "Tuvaluan Dollar", "symbol": "$"},
    "TWD": {"name": "New Taiwan Dollar", "symbol": "NT$"},
    "TZS": {"name": "Tanzanian Shilling", "symbol": "Sh"},
    "UAH": {"name": "Ukrainian Hryvnia", "symbol": "₴"},
    "UGX": {"name": "Ugandan Shilling", "symbol": "USh"},
    "UYU": {"name": "Uruguayan Peso", "symbol": "$U"},
    "UZS": {"name": "Uzbekistani Som", "symbol": "лв"},
    "VES": {"name": "Venezuelan Bolívar", "symbol": "Bs.S"},
    "VND": {"name": "Vietnamese Dong", "symbol": "₫"},
    "VUV": {"name": "Vanuatu Vatu", "symbol": "VT"},
    "WST": {"name": "Samoan Tala", "symbol": "T"},
    "XAF": {"name": "Central African CFA Franc", "symbol": "FCFA"},
    "XCD": {"name": "East Caribbean Dollar", "symbol": "$"},
    "XDR": {"name": "Special Drawing Rights", "symbol": "XDR"},
    "XOF": {"name": "West African CFA Franc", "symbol": "CFA"},
    "XPF": {"name": "CFP Franc", "symbol": "₣"},
    "YER": {"name": "Yemeni Rial", "symbol": "﷼"},
    "ZAR": {"name": "South African Rand", "symbol": "R"},
    "ZMW": {"name": "Zambian Kwacha", "symbol": "ZK"},
    "ZWL": {"name": "Zimbabwean Dollar", "symbol": "$"}
}

def get_currencies(base_key="USD"): # need a base keep bc thats how this qebsite formats it: 
    endpoint = f"{API_KEY}/latest/{base_key}"   # embedding the api key directly in here: if you dont have the api key then it wont send 
    url = BASE_URL + endpoint
    response = get(url)

    data = response.json().get('conversion_rates', {})
    
    currencies = [] # no longer using these whole list menthod things "data = list(data.items())"  "data.sort()" bc we are actually creating a list, and then mainly appending the values that are wanted on it 
    for code, rate in data.items(): # has to be (name, rate) bc the whole list sorting thing going on in the function above is giving a tuple, so bacially a tuple or two values that needs to be delt with as such in this for loop, so name and currency is listed (bc theres two values )
        # using the predefined dictionary (currency_info) to fetch name and symbol
        name = currency_info.get(code, {}).get("name", "Unknown Currency") # if the name key is not found (or the dictionary is empty ("{}" which is our saftey )) then "unknown currency will appear"
        symbol = currency_info.get(code, {}).get("symbol", "") 
        currencies.append((code, name, symbol, rate)) # creating a 4-tuple (quadruuple ), to this new list that was created
    
    currencies.sort()  # sorting by the currency abrevation, which is the first item in the tuple 
    return currencies # ruturning currencies is like returning data but with the nicelyformated list now

def print_currencies(currencies):
    for code, name, symbol, rate in currencies: # just print the whole list, take each value
        print(f"{code} - {name} - {symbol} - Exchange Rate: {rate}")

def exchange_rate(currency1, currency2):
    endpoint = f"{API_KEY}/latest/{currency1}"
    url = BASE_URL + endpoint
    response = get(url)

    data = response.json().get('conversion_rates', {}) # get the json data (the data stored in the api) but only from the conversion_rates "dictionary/list"
    rate = data.get(currency2) # rate is the second value or the "value", not the key in the conversition rates dictionary
    symbol_currency1 = currency_info.get(currency1).get("symbol", "") # getting the currency one id, then getting the symbol associated to it
        # ^^ this is where it comes full circle bc "symbol" is the key associated to the value (which is the actual symbol)
            ## ^^ to avoid the currenceis without a symbol (this wont happen bc now i hardcoded) a blank string will appear so the code can continue to run 
    symbol_currency2 = currency_info.get(currency2).get("symbol", "")
    
    if not rate:
        print("INVALID CURRENCIES.")
        return None

    print(f"{symbol_currency1}{currency1} --> {symbol_currency2}{currency2} = {rate}")
    print(f"...so 1({symbol_currency1}){currency1} is worth {rate}{symbol_currency2} of {currency2}\n")
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None: # retur nothing ( if their is no rate (this like wont happen bc i hard coded but was a mesarue beforehand ))
        return

    try:
        amount = float(amount) # store as float bc run off numbers 
    except ValueError: # value error just to make sure 
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

if __name__ == '__main__':
    currencies = get_currencies() # run the whole get currencies function to get the list that we want 

    print("Welcome to the currency converter")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True: # to avoid spelling errors... etc.
        command = input("Enter a command (q to quit): ").lower() #.lowe just to avoid random capitals "user error"

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to (id - for example: USD,GBP,etc..): ").upper()
            convert(currency1, currency2, amount) # convert with the three amounts given * will run the function for this given the output the user wants*
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to id: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


