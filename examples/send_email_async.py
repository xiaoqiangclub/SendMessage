# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-12T00:13:04.377Z
# 文件描述：异步发送邮件的示例
# 文件路径：examples/send_email_async.py

import asyncio
import os
from xqcsendmessage import send_email_async # 导入新的顶层函数

# --- 配置 ---
SMTP_SERVER = "YOUR_SMTP_SERVER"  # 请替换为您的 SMTP 服务器
SMTP_PORT = 465                   # 请替换为您的 SMTP 端口
SENDER_EMAIL = "YOUR_SENDER_EMAIL"  # 请替换为您的邮箱
SENDER_PASSWORD = "YOUR_SENDER_PASSWORD"    # 请替换为您的邮箱密码或授权码
RECIPIENTS = ["YOUR_RECIPIENT_EMAIL"] # 请替换为收件人邮箱列表

# 附件文件路径，请确保文件存在
ATTACHMENT_FILE = os.path.join(os.path.dirname(__file__), "test_attachment_async.txt")


async def main():
    """主函数"""
    print("\n--- 直接函数调用模式 ---")
    # 模式二：直接函数调用模式
    try:
        # 直接发送不带附件的邮件
        result_direct_no_attachment = await send_email_async(
            message="这是一封通过 sendmessage 直接发送的异步测试邮件，不带附件。",
            email_subject="Hello from xqcsendmessage! (Direct Call No Attachment)",
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            email_recipients=RECIPIENTS,
            email_subtype="plain"
        )
        print(f"✅ 直接调用邮件发送成功 (无附件): {result_direct_no_attachment}")

        # 直接发送带附件的邮件
        result_direct_with_attachment = await send_email_async(
            message="这是一封通过 sendmessage 直接发送的异步测试邮件，带附件。",
            email_subject="Hello from xqcsendmessage! (Direct Call With Attachment)",
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            email_recipients=RECIPIENTS,
            email_subtype="plain",
            email_attachments=[ATTACHMENT_FILE] # 添加附件
        )
        print(f"✅ 直接调用邮件发送成功 (带附件): {result_direct_with_attachment}")

    except Exception as e:
        print(f"🔥 直接调用邮件发送失败: {e}")

if __name__ == "__main__":
    # 创建一个用于测试的附件文件
    with open(ATTACHMENT_FILE, "w") as f:
        f.write("This is a test attachment file for asynchronous email example.")
    
    asyncio.run(main())

    # 清理测试附件文件
    os.remove(ATTACHMENT_FILE)