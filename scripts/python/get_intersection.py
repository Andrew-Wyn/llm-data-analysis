import argparse
from datasets import load_dataset
import json
from tqdm import tqdm

def main(args):
    ds1 = load_dataset(args.ds1, num_proc=20, split="train")
    ds2 = load_dataset(args.ds2, num_proc=20, split="train")
   
    print(ds1)
    print(ds2)

    with open(args.intersection, "r") as intf, open(args.outputfile, "w") as outf:
        for intersection in tqdm(intf):
            url, idx1, idx2 = intersection.split("\t")
            
            sample_1 = ds1[int(idx1)]
            sample_2 = ds2[int(idx2)]

            text_1 = sample_1["text"]
            text_2 = sample_2["text"]
            
            collection_1 = sample_1["source"]
            collection_2 = sample_2["collection"] # TODO: to be fixed, parametrize

            outf.write(json.dumps(
                    {
                        "url": url,
                        f"text_{args.source1}": text_1,
                        f"collection_{args.source1}": collection_1,
                        f"text_{args.source2}": text_2,
                        f"collection_{args.source2}": collection_2,
                        }
                )+"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='From list of intersection construct the intersection dataset, in a Jsonl')
    parser.add_argument("--intersection", type=str, help="intersection film")
    parser.add_argument("--ds1", type=str, help="first dataset")
    parser.add_argument("--ds2", type=str, help="second dataset")
    parser.add_argument("--source1", type=str, help="first source")
    parser.add_argument("--source2", type=str, help="second source")
    parser.add_argument("--outputfile", type=str, help="output file")

    args = parser.parse_args()

    main(args)
