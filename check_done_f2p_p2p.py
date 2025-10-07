import json
import pathlib

input_dir = pathlib.Path("/mnt/data/swe_world_2/SWE-EVO/output_v4")
output_file = input_dir / "not_done.txt"

with open(output_file, "w") as fout:
    for json_file in input_dir.glob("*.json"):
        try:
            data = json.loads(json_file.read_text())
            if isinstance(data.get("FAIL_TO_PASS"), str):
                fout.write(str(json_file) + "\n")
        except Exception as e:
            print(f"⚠️ Lỗi khi đọc {json_file}: {e}")

print(f"✅ Đã ghi danh sách file chưa done vào: {output_file}")

from pathlib import Path

txt_file = Path("/mnt/data/swe_world_2/SWE-EVO/output_v4/not_done.txt")

with open(txt_file, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

print(lines) 
