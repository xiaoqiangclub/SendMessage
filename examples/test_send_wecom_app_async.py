# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-13T05:06:11.730Z
# 文件描述：测试异步发送企业微信应用消息功能
# 文件路径：examples/test_send_wecom_app_async.py

import asyncio
from xqcsendmessage import send_wecom_app_async

# --- 配置 ---
CORP_ID = "YOUR_CORP_ID"
CORP_SECRET = "YOUR_CORP_SECRET"
AGENT_ID = 1000004  # 替换为你的 AgentId

# --- 测试函数 ---

async def test_text_message_to_all_async():
    """测试异步发送纯文本消息给所有人"""
    try:
        result = await send_wecom_app_async(
            "【XQCSendMessage 异步测试】\n功能点: send_wecom_app_async\n消息类型: Text\n接收者: @all",
            corpid=CORP_ID,
            corpsecret=CORP_SECRET,
            agentid=AGENT_ID,
            touser="@all"
        )
        print(f"✅ [test_text_message_to_all_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_text_message_to_all_async] 发送失败: {e}")

async def test_markdown_message_to_all_async():
    """测试异步发送 Markdown 消息给所有人"""
    try:
        result = await send_wecom_app_async(
            "### 【XQCSendMessage 异步测试】\n- **功能点**: send_wecom_app_async\n- **消息类型**: Markdown\n- **接收者**: @all",
            corpid=CORP_ID,
            corpsecret=CORP_SECRET,
            agentid=AGENT_ID,
            send_md=True,
            touser="@all"
        )
        print(f"✅ [test_markdown_message_to_all_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_markdown_message_to_all_async] 发送失败: {e}")

async def test_message_to_user_async():
    """测试异步发送消息给指定用户 (需要将 'USER_ID' 替换为真实用户 ID)"""
    try:
        result = await send_wecom_app_async(
            "【XQCSendMessage 异步测试】\n功能点: send_wecom_app_async\n接收者: 指定用户 (USER_ID)",
            corpid=CORP_ID,
            corpsecret=CORP_SECRET,
            agentid=AGENT_ID,
            touser="Xiaoqiang"  # 替换为真实用户 ID
        )
        print(f"✅ [test_message_to_user_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_message_to_user_async] 发送失败: {e}")

async def main():
    print("--- 开始测试 send_wecom_app_async ---")
    await test_text_message_to_all_async()
    print("-" * 20)
    await test_markdown_message_to_all_async()
    print("-" * 20)
    # 注意：测试发送给指定用户需要一个有效的 USER_ID
    # await test_message_to_user_async()
    print("--- 测试结束 ---")

if __name__ == "__main__":
    asyncio.run(main())