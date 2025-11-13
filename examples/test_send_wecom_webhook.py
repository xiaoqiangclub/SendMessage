# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-13T05:04:06.962Z
# 文件描述：测试同步发送企业微信 Webhook 消息功能
# 文件路径：examples/test_send_wecom_webhook.py

from xqcsendmessage import send_wecom_webhook

# --- 配置 ---
WEBHOOK_URL = "YOUR_WECOM_WEBHOOK_URL"

# --- 测试函数 ---

def test_text_message():
    """测试发送纯文本消息"""
    try:
        result = send_wecom_webhook(
            "【XQCSendMessage 同步测试】\n功能点: send_wecom_webhook\n消息类型: Text",
            webhook=WEBHOOK_URL
        )
        print(f"✅ [test_text_message] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_text_message] 发送失败: {e}")

def test_markdown_message():
    """测试发送 Markdown 消息"""
    try:
        result = send_wecom_webhook(
            "### 【XQCSendMessage 同步测试】\n- **功能点**: send_wecom_webhook\n- **消息类型**: Markdown",
            webhook=WEBHOOK_URL,
            send_md=True
        )
        print(f"✅ [test_markdown_message] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_markdown_message] 发送失败: {e}")

if __name__ == "__main__":
    print("--- 开始测试 send_wecom_webhook ---")
    test_text_message()
    print("-" * 20)
    test_markdown_message()
    print("--- 测试结束 ---")