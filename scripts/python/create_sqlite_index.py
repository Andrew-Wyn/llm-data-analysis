import argparse
import sqlite3
from datasets import load_dataset
from tqdm import tqdm
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main(args):
    
    ds_stream = load_dataset(args.dataset, streaming=True)

    max_samples = args.max_samples
    buffer_size = args.buffer_size

    insert_buffer = []

    # connect to sql db
    conn = sqlite3.connect(args.database)
    
    # faster execution
    conn.execute("PRAGMA synchronous = OFF")

    # create sql table
    create_table_query = f"CREATE TABLE corpora (idx PRIMARY KEY, {', '.join(args.columns)})"
    
    create_index_query = f"CREATE INDEX IF NOT EXISTS {args.index_column}_idx ON corpora ({args.index_column})"
   
    logger.info("creating table...")
  
    print(create_table_query)
    print(create_index_query)

    conn.execute(create_table_query)

    logger.info("created table!!!")

    for idx, sample in tqdm(enumerate(ds_stream["train"]), total=max_samples):
       
        if idx == args.max_samples:
            break

        if not args.sources is None and not sample["source"] in args.sources:
            continue

        row = (idx, ) + tuple(sample[c] for c in args.columns)
        
        insert_buffer.append(row)

        if len(insert_buffer) == buffer_size:
            c = conn.cursor() # cursor
            c.executemany(f'''INSERT INTO corpora VALUES (?{", ?"*len(args.columns)})''', insert_buffer)
            
            insert_buffer = []
            
    if len(insert_buffer) > 0:
        c = conn.cursor()
        c.executemany(f'''INSERT INTO corpora VALUES (?{", ?"*len(args.columns)})''', insert_buffer)
            
        insert_buffer = []

    logger.info("creating index...") 
   
    c = conn.cursor()
    c.execute(create_index_query)
    conn.commit()
    
    logger.info("created index!!!") 

    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, help='dataset path')
    parser.add_argument('--database', type=str, help='database path')
    parser.add_argument('--max_samples', type=int, help='max samples')
    parser.add_argument('--buffer_size', type=int, help='max buffer size')
    parser.add_argument("--columns", nargs="*", help="column over which the database will be constructed")
    parser.add_argument("--index_column", type=str, help="index column")
    parser.add_argument("--sources", nargs="*", default=None, help="source to filter")
    args = parser.parse_args()

    main(args)

