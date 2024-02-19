#!/bin/bash
#SBATCH --job-name=extract_urls_hplt    # Job name
#SBATCH -o extract_urls_hplt-job.out              # Name of stdout output file
#SBATCH -e extract_urls_hplt-job.err              # Name of stderr error file
#SBATCH --nodes=1               # number of nodes
#SBATCH --ntasks-per-node=1     # number of tasks per node
#SBATCH --cpus-per-task=4       # number of threads per task
#SBATCH --time 4:00:00          # format: HH:MM:SS
#SBATCH --mem 30GB

#SBATCH -A IscrB_medit

module load profile/deeplrn hplt-datasets/1.2

# export OMP_PROC_BIND=true
export HF_DATASETS_CACHE=$WORK/hf_cache_lm

source ~/__Work/llmfoundry-cuda-flash-attn2-env/bin/activate

#~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/extract_urls.py \
#    --dataset_path /leonardo_work/IscrB_medit/hplt_res/reservoir_sample_10M_53M/en/web \
#    --max_iterations 10

# ~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/extract_urls.py \
#     --dataset_path /leonardo_work/IscrB_medit/hplt_res/reservoir_sample_10M_53M/it/web \
#     --max_iterations 10

~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/extract_urls.py \
    --dataset_path /leonardo_work/IscrB_medit/hplt_res/reservoir_hq_53M/en \
#    --max_iterations 10

#~/__Work/llmfoundry-cuda-flash-attn2-env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/extract_urls.py \
#     --dataset_path /leonardo_work/IscrB_medit/hplt_res/reservoir_hq_53M/it \
#     --max_iterations 10
