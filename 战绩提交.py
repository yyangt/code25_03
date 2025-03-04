import argparse
import json
from datetime import datetime

# 解析命令行参数
parser = argparse.ArgumentParser(description="记录游戏战绩")
parser.add_argument("--game", type=str, help="游戏名称")
parser.add_argument("--kda", type=str, help="击杀/死亡/助攻，格式为 X/Y/Z")
args = parser.parse_args()

# 解析 KDA 数据
kills, deaths, assists = map(int, args.kda.split('/'))

# 创建数据记录
data = {
    "game": args.game,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "stats": {
        "kills": kills,
        "deaths": deaths,
        "assists": assists
    }
}

# 保存到 JSON 文件
filename = f"stats_{args.game}.json"
with open(filename, "a") as file:
    json.dump(data, file)
    file.write("\n")  # 每条记录占一行

print(f"战绩已记录到 {filename}")