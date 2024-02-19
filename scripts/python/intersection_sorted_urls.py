import argparse
from tqdm import tqdm

def main(args):
    with open(args.file1, "r") as f1, open(args.file2, "r") as f2, open(args.outputfile, "w") as outputf:
        item_2 = next(f2)
        url2 = item_2.split("\t")[0]

        for item_1 in tqdm(f1):
            url1 = item_1.split("\t")[0]
            
            if url1 == url2:
                idx_1 = int(item_1.split('\t')[1])
                idx_2 = int(item_2.split('\t')[1])
                outputf.write(f"{url1}\t{idx_1}\t{idx_2}\n")
            elif url1 < url2:
                continue
            
            while url1 > url2:
                try:
                    item_2 = next(f2)
                    url2 = item_2.split("\t")[0]
                except StopIteration:
                    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Intersect two url files, have to be sorted")
    parser.add_argument("--file1", type=str, help="first file")
    parser.add_argument("--file2", type=str, help="second file")
    parser.add_argument("--outputfile", type=str, help="output file")
    args = parser.parse_args()
    main(args)

