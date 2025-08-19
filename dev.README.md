```bash
export TMPDIR=/bigdisk/minhpvt/sweworld/sweworld-v3/tmp
mkdir -p output/new-data6
python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.1.3..v2.2.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.2.6..v2.3.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/graphql-python/graphene/compare/v3.2.2..v3.3.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/arrow-py/arrow/compare/1.2.0..1.2.1 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/qutip/qutip/compare/v5.0.4..v5.1.0 --output-dir output/new-data6


export TMPDIR=/bigdisk/minhpvt/sweworld/sweworld-v3/tmp
python -m swebench.scripts.create_data https://github.com/scipy/scipy/compare/v1.15.3..v1.16.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.1.3..v2.2.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.2.6..v2.3.0 --output-dir output/new-data6
python -m swebench.scripts.gather_data --input_dir output/new-data6 --output_dir output/exported_dataset

git diff --binary v1.15.3..v1.16.0 -- '*test*' > test.patch
git diff --binary v1.15.3..v1.16.0 -- ':(exclude)*test*' > code.patch


python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.1.3..v2.2.0 --output-dir output/new-data5
python -m swebench.scripts.create_data https://github.com/scipy/scipy/compare/v1.15.3..v1.16.0 --output-dir output/new-data5
python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.2.6..v2.3.0 --output-dir output/new-data5
python -m swebench.scripts.gather_data --input_dir output/new-data5 --output_dir output/exported_dataset

python -m swebench.harness.run_evaluation \
    --dataset_name /home/minhpvt/swe-world-v3/SWE-EVO/output/exported_dataset \
    --cache_level instance \
    --namespace none \
    --predictions_path gold \
    --max_workers 5 \
    --timeout 10000 \
    --run_id test

    # --cache_level instance --force_rebuild true \

```