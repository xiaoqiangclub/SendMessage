# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-13T05:05:44.652Z
# 文件描述：测试异步发送企业微信 Webhook 消息功能
# 文件路径：examples/test_send_wecom_webhook_async.py

import asyncio
from xqcsendmessage import send_wecom_webhook_async

# --- 配置 ---
WEBHOOK_URL = "YOUR_WECOM_WEBHOOK_URL"

# --- 测试函数 ---

async def test_text_message_async():
    """测试异步发送纯文本消息"""
    try:
        result = await send_wecom_webhook_async(
            "【XQCSendMessage 异步测试】\n功能点: send_wecom_webhook_async\n消息类型: Text",
            webhook=WEBHOOK_URL
        )
        print(f"✅ [test_text_message_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_text_message_async] 发送失败: {e}")

async def test_markdown_message_async():
    """测试异步发送 Markdown 消息"""
    try:
        result = await send_wecom_webhook_async(
            "### 【XQCSendMessage 异步测试】\n- **功能点**: send_wecom_webhook_async\n- **消息类型**: Markdown",
            webhook=WEBHOOK_URL,
            send_md=True
        )
        print(f"✅ [test_markdown_message_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_markdown_message_async] 发送失败: {e}")

async def main():
    print("--- 开始测试 send_wecom_webhook_async ---")
    await test_text_message_async()
    print("-" * 20)
    await test_markdown_message_async()
    print("--- 测试结束 ---")

if __name__ == "__main__":
    asyncio.run(main())