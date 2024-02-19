import argparse
import json
import logging
import os
from pathlib import Path
import psutil
from datasets import load_dataset, load_from_disk
from tqdm import tqdm
from random import randrange
from pathlib import Path
import random
from urllib.parse import urlparse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

HF_CACHE = os.getenv("HF_DATASETS_CACHE", os.path.expanduser("~/.cache/huggingface"))

def save_urls(dataset, path_to_save, max_iterations):
    # now we can save the dataset in jsonl format, divided in multiple files
    # we would like to parallelize this step, we can use the multiprocessing library
    file_path = Path(path_to_save)
    file_path.mkdir(parents=True, exist_ok=True)
    
    with open(file_path / "web_urls.json", "w") as f:
        for i, sample in tqdm(enumerate(dataset)):
    
            if i != -1 and i == max_iterations:
                break

            f.write(f"{sample['url']}\t{str(i)}\n")
        

def main(args):
    dataset = load_dataset(
        args.dataset_path,
        split=args.ds_split,
        cache_dir=HF_CACHE,
        streaming=True
    )

    save_urls(dataset, args.dataset_path, args.max_iterations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download HF Dataset")
    parser.add_argument(
        "--dataset_path",
        type=str,
        help="Dataset to download.",
    )
    parser.add_argument(
        "--ds_split",
        type=str,
        default="train",
        help="dataset split to retrieve"
    )
    parser.add_argument(
        "--max_iterations",
        type=int,
        default=-1,
        help="maximum number of iterations"
    )
    args = parser.parse_args()

    main(args)
