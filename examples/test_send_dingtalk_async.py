# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-13T05:05:15.555Z
# 文件描述：测试异步发送钉钉消息功能
# 文件路径：examples/test_send_dingtalk_async.py

import asyncio
from xqcsendmessage import send_dingtalk_async

# --- 配置 ---
WEBHOOK_URL = "YOUR_DINGTALK_WEBHOOK_URL"
SECRET = "YOUR_DINGTALK_SECRET"

# --- 测试函数 ---

async def test_text_message_async():
    """测试异步发送纯文本消息"""
    try:
        result = await send_dingtalk_async(
            "【XQCSendMessage 异步测试】\n功能点: send_dingtalk_async\n消息类型: Text",
            webhook=WEBHOOK_URL,
            secret=SECRET
        )
        print(f"✅ [test_text_message_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_text_message_async] 发送失败: {e}")

async def test_markdown_message_async():
    """测试异步发送 Markdown 消息"""
    try:
        result = await send_dingtalk_async(
            "### 【XQCSendMessage 异步测试】\n- **功能点**: send_dingtalk_async\n- **消息类型**: Markdown",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            send_md=True,
            title="【异步测试】Markdown 消息"
        )
        print(f"✅ [test_markdown_message_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_markdown_message_async] 发送失败: {e}")

async def test_at_all_async():
    """测试异步 @所有人"""
    try:
        result = await send_dingtalk_async(
            "【XQCSendMessage 异步测试】\n功能点: send_dingtalk_async\n@类型: @所有人",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            is_at_all=True
        )
        print(f"✅ [test_at_all_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_at_all_async] 发送失败: {e}")

async def test_at_mobiles_async():
    """测试异步 @指定手机号"""
    try:
        result = await send_dingtalk_async(
            "【XQCSendMessage 异步测试】\n功能点: send_dingtalk_async\n@类型: @指定手机号",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            at_mobiles=["YOUR_MOBILE_NUMBER"] # 替换为需要@的手机号
        )
        print(f"✅ [test_at_mobiles_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_at_mobiles_async] 发送失败: {e}")

async def test_at_mobiles_override_at_all_async():
    """测试异步 @指定手机号时，is_at_all 会被忽略"""
    try:
        result = await send_dingtalk_async(
            "【XQCSendMessage 异步测试】\n功能点: send_dingtalk_async\n逻辑: at_mobiles 覆盖 is_at_all\n预期: 只@手机号，不@所有人",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            at_mobiles=["YOUR_MOBILE_NUMBER"],
            is_at_all=True # 此参数应被忽略
        )
        print(f"✅ [test_at_mobiles_override_at_all_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_at_mobiles_override_at_all_async] 发送失败: {e}")

async def main():
    print("--- 开始测试 send_dingtalk_async ---")
    await test_text_message_async()
    print("-" * 20)
    await test_markdown_message_async()
    print("-" * 20)
    await test_at_all_async()
    print("-" * 20)
    await test_at_mobiles_async()
    print("-" * 20)
    await test_at_mobiles_override_at_all_async()
    print("--- 测试结束 ---")

if __name__ == "__main__":
    asyncio.run(main())