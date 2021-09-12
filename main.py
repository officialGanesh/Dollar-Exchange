# Import the required modules
import requests, json, os


base_url = "http://apilayer.net/api/live?"
access_key = os.getenv('currencyAPI')

end_point = f"{base_url}access_key={access_key}"

def main_function():
    
    '''This function is used to get the json data and convert into python dictionary'''
    try:
        r = requests.get(end_point)
        r.raise_for_status()
        # print(r.status_code)

        # load the json data
        with open('CurrencyData.json','w') as f:
            source = r.json()
            f.write(json.dumps(source,indent=2))

        # python dictionary
        with open('CurrencyData.json','r') as f:
            python_file = json.load(f)
            
        def Display_data():
            '''This function is used to display the required data'''
            USD_INR = python_file['quotes']['USDINR']
            # Rate of usd to inr or 1 dollar to inr
            print(f"Current USDINR RATE --> {USD_INR}")
            print('-----------------------------------------------')

            def INR_USD():
                '''Converting INR to USD'''
                amount = eval(input('Enter the amount you like to convert into USD --> '))
                usd = (1 / USD_INR) * amount
                print(f'INR --> {amount}\n USD --> {usd}')

            INR_USD()

        Display_data()    

        

    except Exception as e:
        print("Something Went Wrong 💢 ",e)





if __name__ == "__main__":

    main_function()
    print("Code Completed 🔥")