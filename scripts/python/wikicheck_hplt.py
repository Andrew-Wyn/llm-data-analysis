from datasets import load_dataset

from tqdm import tqdm

lang = "en"

d = load_dataset(f"/leonardo_work/IscrB_medit/hplt_res/reservoir_sample_10M_53M/{lang}", streaming=True)

check_counter = 0

for i, s in tqdm(enumerate(d["train"])):
    if "Informazioni su Wikipedia" in s["text"] or "About Wikipedia" in s["text"]: # check over structural threats of wikipedia pages
        with open(f"hplt_{lang}_web_wikipedia_{str(i)}.txt", "w") as f:
            f.write(s["url"] + "\n\n")
            f.write(s["text"])
        
        check_counter += 1

    if check_counter == 2:
        break
            
