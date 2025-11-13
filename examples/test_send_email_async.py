# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-13T05:04:51.262Z
# 文件描述：测试异步发送邮件功能
# 文件路径：examples/test_send_email_async.py

import asyncio
import os
from xqcsendmessage import send_email_async

# --- 配置 ---
SMTP_SERVER = "YOUR_SMTP_SERVER"
SMTP_PORT = 465
SENDER_EMAIL = "YOUR_SENDER_EMAIL"
SENDER_PASSWORD = "YOUR_SENDER_PASSWORD"
RECIPIENTS = ["YOUR_RECIPIENT_EMAIL"]

# --- 测试函数 ---

async def test_plain_email_async():
    """测试异步发送纯文本邮件"""
    try:
        result = await send_email_async(
            message="【XQCSendMessage 异步测试】\n功能点: send_email_async\n消息类型: 纯文本 (plain)",
            email_subject="【异步测试】纯文本邮件",
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            email_recipients=RECIPIENTS,
        )
        print(f"✅ [test_plain_email_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_plain_email_async] 发送失败: {e}")

async def test_html_email_async():
    """测试异步发送 HTML 邮件"""
    try:
        result = await send_email_async(
            message="""
            <h3>【XQCSendMessage 异步测试】</h3>
            <ul>
                <li><b>功能点</b>: send_email_async</li>
                <li><b>消息类型</b>: HTML</li>
            </ul>
            """,
            email_subject="【异步测试】HTML 邮件",
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            email_recipients=RECIPIENTS,
            email_subtype="html"
        )
        print(f"✅ [test_html_email_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_html_email_async] 发送失败: {e}")

async def test_email_with_attachment_async():
    """测试异步发送带附件的邮件"""
    # 创建一个临时附件
    attachment_file = "temp_attachment_async.txt"
    with open(attachment_file, "w", encoding="utf-8") as f:
        f.write("这是异步邮件附件的测试内容。")

    try:
        result = await send_email_async(
            message="【XQCSendMessage 异步测试】\n功能点: send_email_async\n消息类型: 带附件",
            email_subject="【异步测试】带附件的邮件",
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            email_recipients=RECIPIENTS,
            email_attachments=[attachment_file]
        )
        print(f"✅ [test_email_with_attachment_async] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_email_with_attachment_async] 发送失败: {e}")
    finally:
        # 清理临时附件
        if os.path.exists(attachment_file):
            os.remove(attachment_file)

async def main():
    print("--- 开始测试 send_email_async ---")
    await test_plain_email_async()
    print("-" * 20)
    await test_html_email_async()
    print("-" * 20)
    await test_email_with_attachment_async()
    print("--- 测试结束 ---")

if __name__ == "__main__":
    asyncio.run(main())