import sqlite3
import numpy as np


index_hplt_it = "/leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/hplt_it_50m.db"
index_hplt_en = "/leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/hplt_en_50m.db"
index_culturax_it = "/leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/culturax_it_100m.db"
index_culturax_en = "/leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/culturax_en_100m.db"


def print_stats(db, data):
    con = sqlite3.connect(db)
    
    print(f"************** {data} **************")

    query_res = con.execute("SELECT count(url) FROM corpora GROUP BY url HAVING (COUNT(url) > 1);")
    print(f"{data} mean duplicated {np.mean(query_res.fetchall())}")

    query_res = con.execute("SELECT count(url) FROM corpora GROUP BY url HAVING (COUNT(url) > 1);")
    print(f"{data} std duplicated {np.std(query_res.fetchall())}")

    query_res = con.execute("SELECT count(url) FROM corpora GROUP BY url HAVING (COUNT(url) > 1);")
    print(f"{data} num duplicated {len(query_res.fetchall())}")

    query_res = con.execute("SELECT count(url) FROM corpora GROUP BY url HAVING (COUNT(url) > 1);")
    print(f"{data} total number of duplicated {np.sum(query_res.fetchall())}")

    query_res = con.execute("SELECT url FROM corpora GROUP BY url;")
    print(f"{data} num different urls {len(query_res.fetchall())}")

    query_res = con.execute("SELECT url FROM corpora;")
    print(f"{data} num total urls {len(query_res.fetchall())}")

def main():
    print_stats(index_hplt_it, "hplt it")
    print_stats(index_hplt_en, "hplt en")
    print_stats(index_culturax_it, "culturax it")
    print_stats(index_culturax_en, "culturax en")

if __name__ == "__main__":
    main()
