from asyncio.windows_events import NULL
import pandas as pd
import openai
import random
import time
import csv

few_shot = """Write a google meta description for a buyer's guide about the keyword: 
"""

with open('output.csv', 'w', newline='', encoding="utf-8") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(["record_id","term","headline"])

url = '2023-09-02-product_tag-42ba260d-d07d-2e93-a25e-714286931075.csv'
df = pd.read_csv(url)

for record_id,term in zip(df["record_id"],df["Name"]):
   
    setup = f"{few_shot} {term}" 
    MAX_RETRY = 100000
    retries = 0
    while retries < MAX_RETRY:
        try:
            openai.api_key = random.choice(["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","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","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","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","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","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","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","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"])
            response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= setup,
            temperature=0.7,
            max_tokens=1000,    
            top_p=1,
            frequency_penalty= 0.1,
            presence_penalty=0.1,
            stop = "###",
            #bad_words = "-The"
            )

            output = response.choices[0].text
            #output = output.replace("\n","")
            #output = f"The{output}"#
    
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


