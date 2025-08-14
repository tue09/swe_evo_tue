python -m swebench.harness.run_evaluation \
    --dataset_name /bigdisk/minhpvt/sweworld/sweworld-v3/SWE-bench/output/exported_dataset \
    --cache_level instance \
    --namespace none \
    --predictions_path gold \
    --max_workers 1 \
    --run_id test

    # use --predictions_path 'gold' to verify the gold patches
    # use --run_id to name the evaluation run
    # use --modal true to run on Modal