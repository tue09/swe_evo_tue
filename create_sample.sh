REPO="dask/dask"
NAME="dask__dask"
VERSION="2024_4_0"

python -m swebench.scripts.create_data \
    https://github.com/${REPO}/compare/2024.3.1..2024.4.0 \
    --end_release_note_txt ./_rl_note_v2/swe_gym/${NAME}/${VERSION}.txt \
    --output-dir output_v2


# python -m swebench.scripts.create_data \
#     https://github.com/SWE-bench-repos/astropy__astropy/compare/v5.3rc1..v6.0.dev \
#     --end_release_note_txt ./_release_note/swe_bench/astropy__astropy.txt \
#     --output-dir output