from asyncio.windows_events import NULL
import pandas as pd
import openai
import random
import time
import csv

few_shot = """Write a catchy Article heading with a colon for the following keyword
"""

with open('output.csv', 'w', newline='', encoding="utf-8") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(["record_id","term","headline"])

url = 'input.csv'
df = pd.read_csv(url)

for record_id,term in zip(df["record_id"],df["Name"]):
    setup = f"{few_shot} {term}"  
    MAX_RETRY = 100000
    retries = 0
    while retries < MAX_RETRY:
        try:
            openai.api_key = random.choice(["YOUR_API_KEY_OR_KEYS_HERE"])
            response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= setup,
            temperature=0.7,
            max_tokens=1000,    
            top_p=1,
            frequency_penalty= 0.1,
            presence_penalty=0.1,
            stop = "###",
            )

            output = response.choices[0].text
    
            print(output)
            time.sleep(2.5)
            break
         
                          
        except Exception as i:
            retries += 1
            if retries >= MAX_RETRY:
                print("ERROR=Method failed after maximum number of retries.")
                break
            else:
                # time.sleep(60)
                
                print(f"ERROR=Method failed. Retrying ... #{retries}")
                print(openai.api_key)
                time.sleep(5)

    with open('output.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([record_id ,term, output])


