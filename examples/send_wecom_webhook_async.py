# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-12T00:13:44.597Z
# 文件描述：异步发送企业微信 Webhook 消息的示例
# 文件路径：examples/send_wecom_webhook_async.py

import asyncio
from xqcsendmessage import send_wecom_webhook_async  # 导入新的顶层函数

# --- 配置 ---
# 你的企业微信机器人的 Webhook
WEBHOOK_URL = "YOUR_WECOM_WEBHOOK_URL"  # 请替换为您的企业微信机器人 Webhook URL


async def main():
    """主函数"""
    print("\n--- 直接函数调用模式 ---")
    try:
        # 发送字符串消息
        result_direct_str = await send_wecom_webhook_async(
            "【XQCSendMessage】这是一条来自 sendmessage 直接发送的异步 Webhook 测试消息 (字符串)。",
            webhook=WEBHOOK_URL,
            msg_type="text"  # 消息类型为文本
        )
        print(f"✅ 直接调用企业微信 Webhook 消息发送成功 (字符串): {result_direct_str}")

        # 发送字符串消息，并覆盖默认参数（例如，指定不同的内容）
        result_override_str = await send_wecom_webhook_async(
            {"markdown": {"content": "【XQCSendMessage】这是一条来自 sendmessage 的异步 Webhook 测试消息 (覆盖字符串内容，markdown 类型)。"}},
            webhook=WEBHOOK_URL,
            msg_type="markdown"  # 覆盖为 markdown 类型
        )
        print(f"✅ 企业微信 Webhook 消息发送成功 (覆盖字符串): {result_override_str}")

        # 发送字典消息
        result_direct_dict = await send_wecom_webhook_async(
            {
                "msgtype": "markdown",
                "markdown": {"content": "【XQCSendMessage】这是一条来自 sendmessage 直接发送的异步 Webhook 测试消息 (字典，markdown 类型)。"}
            },
            webhook=WEBHOOK_URL,
            msg_type="markdown"  # 消息类型为 markdown
        )
        print(f"✅ 直接调用企业微信 Webhook 消息发送成功 (字典): {result_direct_dict}")

    except Exception as e:
        print(f"🔥 直接调用企业微信 Webhook 消息发送失败: {e}")

if __name__ == "__main__":
    asyncio.run(main())
