#!/bin/bash
#SBATCH --job-name=extract_index    # Job name
#SBATCH -o extract_index_2-job.out              # Name of stdout output file
#SBATCH -e extract_index_2-job.err              # Name of stderr error file
#SBATCH --nodes=1               # number of nodes
#SBATCH --ntasks-per-node=1     # number of tasks per node
#SBATCH --cpus-per-task=4       # number of threads per task
#SBATCH --time 4:00:00          # format: HH:MM:SS
#SBATCH --mem 30GB

#SBATCH -A IscrB_medit

# export HF_DATASETS_CACHE=$WORK/hf_cache_lm

module load profile/deeplrn culturax/2309 hplt-datasets/1.2

export HF_DATASETS_CACHE=$HOME/.cache/huggingface
source ~/__Work/llmfoundry-cuda-flash-attn2-env/bin/activate

# /leonardo/prod/data/ai/culturax/2309/en

# /leonardo/prod/data/ai/hplt-datasets/1.2/en

# --database /leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/hplt_en_50m.db \

# ~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/create_sqlite_index.py \
# 	--dataset /leonardo/prod/data/ai/hplt-datasets/1.2/en \
#	--database /leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/hplt_en_50m.db \
#	--buffer_size 100_000 \
#	--max_samples 50_000_000 \
#	--columns "url" \
#	--index_column "url"

#~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/create_sqlite_index.py \
#	--dataset /leonardo/prod/data/ai/hplt-datasets/1.2/it \
#	--database /leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/hplt_it_50m.db \
#	--buffer_size 100_000 \
#	--max_samples 50_000_000 \
#	--columns "url" \
#	--index_column "url"

#~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/create_sqlite_index.py \
#	--dataset /leonardo/prod/data/ai/culturax/2309/en \
#	--database /leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/culturax_en_100m.db \
#	--buffer_size 100_000 \
#	--max_samples 100_000_000 \
#	--columns "url" \
#	--index_column "url" \
#	--sources mC4 OSCAR-2301 OSCAR-2201

~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/create_sqlite_index.py \
	--dataset /leonardo/prod/data/ai/culturax/2309/it \
	--database /leonardo_scratch/large/userexternal/lmoroni0/dataset_indexes/culturax_it_100m.db \
	--buffer_size 100_000 \
	--max_samples 100_000_000 \
	--columns "url" \
	--index_column "url" \
	--sources mC4 OSCAR-2301 OSCAR-2201
