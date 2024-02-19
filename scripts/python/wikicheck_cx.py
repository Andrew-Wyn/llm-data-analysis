from datasets import load_dataset

from tqdm import tqdm

lang = "it"

d = load_dataset(f"/leonardo_scratch/large/userexternal/lmoroni0/datasets/culturax_res/reservoir_sample_10M_100M/{lang}/web", streaming=True)

check_counter = 0

for i, s in tqdm(enumerate(d["train"])):
    if s["text"].count("[") > 5 and s["text"].count("[") == s["text"].count("]") and "Wikipedia" in s["text"]:
        print("checked!!!")
        with open(f"cx_{lang}_web_wikipedia_{str(i)}.txt", "w") as f:
            f.write(s["url"] + "\n\n")
            f.write(s["text"])
        
        check_counter += 1

    if check_counter == 2:
        break
            
