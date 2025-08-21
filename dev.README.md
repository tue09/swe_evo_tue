```bash
export TMPDIR=/bigdisk/minhpvt/sweworld/sweworld-v3/tmp
mkdir -p output/new-data6
python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.1.3..v2.2.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/numpy/numpy/compare/v2.2.6..v2.3.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/graphql-python/graphene/compare/v3.2.2..v3.3.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/arrow-py/arrow/compare/1.2.0..1.2.1 --output-dir output/new-data6

python -m swebench.scripts.create_data https://github.com/qutip/qutip/compare/v5.0.4..v5.1.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/scipy/scipy/compare/v1.15.3..v1.16.0 --output-dir output/new-data6

python -m swebench.scripts.create_data https://github.com/django-oscar/django-oscar/compare/3.2.4..3.2.5 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/django-oscar/django-oscar/compare/3.2.6..4.0 --output-dir output/new-data6

python -m swebench.scripts.create_data https://github.com/benfred/implicit/compare/v0.4.8..v0.5.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/nedbat/coveragepy/compare/7.7.1..7.8.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/nedbat/coveragepy/compare/7.8.2..7.9.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/elastic/elasticsearch-py/compare/v8.19.0..v9.0.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/pydata/xarray/compare/v2025.06.1..v2025.07.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/Tribler/tribler/compare/v7.13.0-alpha.4..v7.13.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/joke2k/django-environ/compare/v0.11.2..v0.12.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/CamDavidsonPilon/lifelines/compare/v0.18.6..v0.19.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/google/timesketch/compare/20250408..20250521 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/google/timesketch/compare/20250521..20250708 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/google/timesketch/compare/20250112..20250408 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/pycontribs/jira/compare/3.9.4..3.10.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/napalm-automation/napalm/compare/4.1.0..5.0.0 --output-dir output/new-data6
python -m swebench.scripts.create_data https://github.com/RDFLib/rdflib/compare/6.3.1..6.3.2 --output-dir output/new-data6


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
    --force_rebuild true \
    --cache_level instance \
    --namespace none \
    --predictions_path gold \
    --max_workers 10 \
    --timeout 10000 \
    --run_id test

    # --force_rebuild true \
    # --cache_level instance --force_rebuild true \

python -m swebench.scripts.gather_data --input_dir output/new-data6 --output_dir output/exported_dataset




```