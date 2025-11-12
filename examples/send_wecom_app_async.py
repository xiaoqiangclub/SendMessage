# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-12T00:14:04.625Z
# 文件描述：异步发送企业微信应用消息的示例
# 文件路径：examples/send_wecom_app_async.py

import asyncio
from xqcsendmessage import send_wecom_app_async  # 导入新的顶层函数

# --- 配置 ---
# 你的企业微信应用配置
CORP_ID = "YOUR_CORP_ID"  # 请替换为您的企业 ID
CORP_SECRET = "YOUR_CORP_SECRET"  # 请替换为您的应用 Secret
AGENT_ID = 1000004  # 请替换为您的应用 AgentId


async def main():
    """主函数"""
    print("\n--- 直接函数调用模式 ---")
    try:
        # 发送字符串消息
        result_direct_str = await send_wecom_app_async(
            "【XQCSendMessage】这是一条通过企业微信应用直接发送的异步测试消息 (字符串)。",
            corpid=CORP_ID,
            corpsecret=CORP_SECRET,
            agentid=AGENT_ID,
            msg_type="text",  # 消息类型为文本
            touser="@all"  # 默认 @所有人
        )
        print(f"✅ 直接调用企业微信应用消息发送成功 (字符串): {result_direct_str}")

        # 发送字符串消息，并覆盖默认参数（例如，指定不同的内容）
        result_override_str = await send_wecom_app_async(
            "【XQCSendMessage】这是一条通过企业微信应用发送的异步测试消息 (覆盖字符串内容，指定用户)。",
            corpid=CORP_ID,
            corpsecret=CORP_SECRET,
            agentid=AGENT_ID,
            touser="@all"  # 覆盖为指定用户
        )
        print(f"✅ 企业微信应用消息发送成功 (覆盖字符串): {result_override_str}")

        # 发送字典消息
        result_direct_dict = await send_wecom_app_async(
            {
                "msgtype": "markdown",
                "markdown": {"content": "【XQCSendMessage】这是一条通过企业微信应用直接发送的异步测试消息 (字典，指定用户)。"}
            },
            corpid=CORP_ID,
            corpsecret=CORP_SECRET,
            agentid=AGENT_ID,
            msg_type="markdown",  # 消息类型为 markdown
            touser="@all"  # 可以在这里覆盖 touser
        )
        print(f"✅ 直接调用企业微信应用消息发送成功 (字典): {result_direct_dict}")

    except Exception as e:
        print(f"🔥 直接调用企业微信应用消息发送失败: {e}")

if __name__ == "__main__":
    asyncio.run(main())
