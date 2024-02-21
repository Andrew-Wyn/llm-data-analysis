#SBATCH --job-name=extract_data_from_hf_reservoir_en    # Job name
#SBATCH -o extract_data_from_hf_en-job.out              # Name of stdout output file
#SBATCH -e extract_data_from_hf_en-job.err              # Name of stderr error file
#SBATCH --nodes=1               # number of nodes
#SBATCH --ntasks-per-node=1     # number of tasks per node
#SBATCH --cpus-per-task=4       # number of threads per task
#SBATCH --time 4:00:00          # format: HH:MM:SS
#SBATCH --mem 30GB

#SBATCH -A IscrB_medit

# export HF_DATASETS_CACHE=$WORK/hf_cache_lm
export HF_DATASETS_CACHE=$HOME/.cache/huggingface
source ~/__Work/llm-data-analysis/.env/bin/activate

~/__Work/llm-data-analysis/.env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/get_intersection.py \
    --intersection /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_web_cx_hplt_en.tsv \
    --ds1 /leonardo_work/IscrB_medit/culturax_res/reservoir_sample_10M_100M/en/web\
    --ds2 /leonardo_work/IscrB_medit/hplt_res/reservoir_sample_10M_53M/en/web \
    --source1 cultura_x \
    --source2 hplt \
    --outputfile /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_web_cx_hplt_en.json

~/__Work/llm-data-analysis/.env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/get_intersection.py \
   --intersection /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_web_cx_hplt_it.tsv \
   --ds1 /leonardo_work/IscrB_medit/culturax_res/reservoir_sample_10M_100M/it/web\
   --ds2 /leonardo_work/IscrB_medit/hplt_res/reservoir_sample_10M_53M/it/web \
   --source1 cultura_x \
   --source2 hplt \
   --outputfile /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_web_cx_hplt_it.json

~/__Work/llm-data-analysis/.env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/get_intersection.py \
   --intersection /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_hq_cx_hplt_en.tsv \
   --ds1 /leonardo_work/IscrB_medit/culturax_res/reservoir_hq_85M/en \
   --ds2 /leonardo_work/IscrB_medit/hplt_res/reservoir_hq_53M/en \
   --source1 cultura_x \
   --source2 hplt \
   --outputfile /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_hq_cx_hplt_en.json

~/__Work/llm-data-analysis/.env/bin/python /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/scripts/data_prep/get_intersection.py \
   --intersection /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_hq_cx_hplt_it.tsv \
   --ds1 /leonardo_work/IscrB_medit/culturax_res/reservoir_hq_85M/it \
   --ds2 /leonardo_work/IscrB_medit/hplt_res/reservoir_hq_53M/it \
   --source1 cultura_x \
   --source2 hplt \
   --outputfile /leonardo/home/userexternal/lmoroni0/__Work/llm-foundry/intersection_hq_cx_hplt_it.json
