import subprocess
import schedule
import time

# 配置项
REPO_PATH = r"E:\Git\github"  # 替换为你的代码仓库路径
GITHUB_REPO = "origin"        # 远程仓库名称
COMMIT_MESSAGE = "Auto backup"  # 提交信息
TIME_INTERVAL = "17:14"       # 定时时间（每天的 22:00）

def git_push():
    """提交并推送代码到 GitHub"""
    try:
        # 添加所有文件到暂存区
        result = subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)
        print("Git add completed")
        
        # 提交代码
        result = subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], cwd=REPO_PATH, check=True)
        print("Git commit completed")
        
        # 推送代码到 GitHub
        result = subprocess.run(["git", "push", GITHUB_REPO], cwd=REPO_PATH, check=True)
        print("Git push completed")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during Git operation: {e}")

def schedule_backup():
    schedule.every().day.at(TIME_INTERVAL).do(git_push)  # 每天 22:00 执行备份
    print(f"Backup scheduled at {TIME_INTERVAL} daily")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_backup()