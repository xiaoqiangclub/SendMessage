# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-13T04:52:23.966Z
# 文件描述：演示如何使用 read_file 和 read_file_async 工具函数。
# 文件路径：examples/read_file_demo.py

import asyncio
import os
from xqcsendmessage import read_file, read_file_async, send_dingtalk

# --- 配置 ---
# 创建一个临时文件用于演示
TEST_FILE = "demo_file.txt"
FILE_CONTENT = "这是用于测试文件读取功能的演示内容。"

# 钉钉 Webhook 用于发送读取到的内容
WEBHOOK_URL = "YOUR_DINGTALK_WEBHOOK_URL"
SECRET = "YOUR_DINGTALK_SECRET"

def setup_test_file():
    """创建用于测试的临时文件"""
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write(FILE_CONTENT)
    print(f"--- 创建测试文件: {TEST_FILE} ---")

def cleanup_test_file():
    """删除测试文件"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
        print(f"--- 清理测试文件: {TEST_FILE} ---")

async def main():
    """主函数"""
    setup_test_file()
    
    try:
        # --- 同步读取 ---
        print("\n--- 1. 同步读取文件并发送 ---")
        try:
            content_sync = read_file(TEST_FILE)
            print(f"✅ 同步读取成功: '{content_sync}'")
            # 使用读取到的内容发送钉钉消息
            send_dingtalk(
                f"【同步读取测试】\n\n文件内容: {content_sync}",
                webhook=WEBHOOK_URL,
                secret=SECRET,
                send_md=True,
                title="文件读取同步测试"
            )
            print("✅ 同步发送钉钉消息成功")
        except Exception as e:
            print(f"🔥 同步读取或发送失败: {e}")

        # --- 异步读取 ---
        print("\n--- 2. 异步读取文件并发送 ---")
        try:
            content_async = await read_file_async(TEST_FILE)
            print(f"✅ 异步读取成功: '{content_async}'")
            # 使用读取到的内容发送钉钉消息 (这里为了简单，仍然使用同步发送)
            send_dingtalk(
                f"【异步读取测试】\n\n文件内容: {content_async}",
                webhook=WEBHOOK_URL,
                secret=SECRET,
                send_md=True,
                title="文件读取异步测试"
            )
            print("✅ 异步读取后发送钉钉消息成功")
        except Exception as e:
            print(f"🔥 异步读取或发送失败: {e}")

    finally:
        cleanup_test_file()

if __name__ == "__main__":
    asyncio.run(main())