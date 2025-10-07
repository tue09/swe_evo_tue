# import json

# with open("/mnt/data/swe_world_2/SWE-EVO/output_v4/conan-io__conan_2.0.2_2.0.3.json", "r", encoding="utf-8") as f:
#     json_data = json.load(f)
# for key in json_data.keys():
#     print(f'keys = {key} has type = {type(json_data[key])}')

# jsonl_data = []
# with open("/mnt/data/swe_world_2/SWE-EVO/full_commit.jsonl", "r", encoding="utf-8") as f:
#     for line in f:
#         jsonl_data.append(json.loads(line))
# print("Nội dung JSONL:", type(jsonl_data[0]))

###################################

# import os
# import json
# from datasets import load_dataset

# full_data = []
# with open("full_commit.jsonl", "r", encoding="utf-8") as f:
#     for line in f:
#         full_data.append(json.loads(line))
# # print("Nội dung JSONL:", type(jsonl_data[0]))

# swe_bench_repo = []
# swe_gym_repo = []

# ds = load_dataset('SWE-bench/SWE-bench', split='test') # SWE-Gym/SWE-Gym
# repos = sorted(set(ds['repo']))
# for r in repos:
#     o, n = r.split('/')
#     swe_bench_repo.append(n)

# ds = load_dataset('SWE-Gym/SWE-Gym', split='train') # SWE-Gym/SWE-Gym
# repos = sorted(set(ds['repo']))
# for r in repos:
#     o, n = r.split('/')
#     swe_gym_repo.append(n)

# input_dir = "output_v2"
# output_dir = "output_v3"

# os.makedirs(output_dir, exist_ok=True)

# for filename in os.listdir(input_dir):
#     if filename.endswith(".json"):
#         input_path = os.path.join(input_dir, filename)
#         output_path = os.path.join(output_dir, filename)

#         with open(input_path, "r", encoding="utf-8") as f:
#             data = json.load(f)

#         for instance in full_data:
#             if instance["base_commit"] == data["base_commit"]:
#                 data["instance_id_swe"] = instance["instance_id"]
        
#         for repo in swe_bench_repo:
#             if repo in data["instance_id"]:
#                 data["bench"] = "swe_bench"
#         for repo in swe_gym_repo:
#             if repo in data["instance_id"]:
#                 data["bench"] = "swe_gym"

#         # if isinstance(data, dict):
#         #     data["tue"] = 1
#         # elif isinstance(data, list):
#         #     data = [{**item, "tue": 1} if isinstance(item, dict) else item for item in data]

#         # ghi ra output_dir với tên như cũ
#         with open(output_path, "w", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False, indent=2)

# print("Done process file JSON.")

################

# import os
# import json
# from datasets import load_dataset

# def docker_image_from_instance(instance_id_swe: str, bench: str) -> str:
#     b = bench.strip().lower().replace("-", "_")
#     if b == "swe_gym":
#         return f"xingyaoww/sweb.eval.x86_64.{instance_id_swe.replace('__', '_s_')}"
#     elif b == "swe_bench":
#         return f"ghcr.io/epoch-research/swe-bench.eval.x86_64.{instance_id_swe}"
#     else:
#         raise ValueError(f"Unknown bench: {bench!r}")

# import subprocess

# def get_commit_of_tag(repo_path: str, tag: str) -> str:
#     # Lấy SHA commit mà tag trỏ tới (support cả annotated/lightweight)
#     cmd = ["git", "-C", repo_path, "rev-parse", f"{tag}^{{commit}}"]
#     try:
#         out = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
#         return out.stdout.strip()
#     except subprocess.CalledProcessError:
#         # Nếu tag chưa có local, fetch tags rồi thử lại
#         subprocess.run(["git", "-C", repo_path, "fetch", "--tags", "--force", "origin"],
#                        check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
#         out = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
#         return out.stdout.strip()

# # # Ví dụ:
# # print(docker_image_from_instance("conan-io__conan-13450", "swe_gym"))
# # # -> xingyaoww/sweb.eval.x86_64.conan-io_s_conan-13450

# input_dir = "output_v5"
# output_dir = "output_v7"
# output_txt = "image_list.txt"

# os.makedirs(output_dir, exist_ok=True)

# with open(output_txt, "w", encoding="utf-8") as out_f:
#     for id, filename in enumerate(os.listdir(input_dir)):
#         # print(f'[filename] = {filename}')
#         if filename.endswith(".json"):
#             input_path = os.path.join(input_dir, filename)
#             output_path = os.path.join(output_dir, filename)

#             with open(input_path, "r", encoding="utf-8") as f:
#                 data = json.load(f)
#             repo_ = data["repo"].strip().replace("/", "__")

#             repo_path = f"/mnt/data/swe_world_2/{data['bench']}/{repo_}/"
#             end_version = data["end_version"]
#             # print(f'[repo_path] = {repo_path}')
#             # print(f'[end_version] = {end_version}')
#             end_commit = get_commit_of_tag(repo_path, end_version)
#             print(f'end_commit = {end_commit}')
#             data["end_version_commit"] = end_commit
#             data["environment_setup_commit"] = end_commit
#             data["PASS_TO_PASS"] = "..."
#             data["FAIL_TO_PASS"] = "..."
#             # break
#             with open(output_path, "w", encoding="utf-8") as f:
#                 json.dump(data, f, ensure_ascii=False, indent=2)

# docker buildx imagetools inspect IMAGE
# echo $?

# docker buildx imagetools inspect xingyaoww/sweb.eval.x86_64.modin-project_s_modin-7193



import json
import os

input_dir = "output_v5"
output_dir = "output_v8"
output_txt = "fake_test.txt"

os.makedirs(output_dir, exist_ok=True)

with open(output_txt, "w", encoding="utf-8") as out_f:
    for id, filename in enumerate(os.listdir(input_dir)):
        # if id > 0: break
        if "iterative__dvc_1.0.0a1_1.0.0a2" in filename:
            if filename.endswith(".json"):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)

                with open(input_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                out_f.write(data["test_patch"] + "\n")

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)