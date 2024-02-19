from datasets import load_dataset
from tqdm import tqdm

ds = load_dataset("/leonardo/prod/data/ai/hplt-datasets/1.2/en", streaming=True)

# check two identic documents

id_1 = 40617
id_2 = 127196

for i, sample in tqdm(enumerate(ds["train"])):
    if i == id_1:
        print(sample["text"])
        print("-"*30)
        with open(f"hplt_en_{str(id_1)}.txt", "w") as f:
            f.write(sample["url"]+"\n\n")
            f.write(sample["text"])
    if i == id_2:
        print(sample["text"])
        with open(f"hplt_en_{str(id_2)}.txt", "w") as f:
            f.write(sample["url"]+"\n\n")
            f.write(sample["text"])
        break
