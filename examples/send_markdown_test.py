import asyncio
from xqcsendmessage.api import (
    send_dingtalk,
    send_dingtalk_async,
    send_wecom_webhook,
    send_wecom_webhook_async,
    send_wecom_app,
    send_wecom_app_async,
)

# 从 test_markdown.md 读取 Markdown 内容
with open("examples/test_markdown.md", "r", encoding="utf-8") as f:
    markdown_content = f.read()

# 钉钉机器人配置
DINGTALK_WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send?access_token=b5142d02f0a5dee6937f049961cf47bf046a46b9ed4dcd193cf2a6ababfd71bd"
DINGTALK_SECRET = "L9TpC5CAg2Xu6vlbuDKRaG0cMxZA6uENqymnw5eyQv61sY8Vq-aqsmtBH-iJUxCH"

# 企业微信配置
WECOM_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=23c2cfd8-c8b2-44e8-a67b-f732db251a8a"
WECOM_CORP_ID = "ww04df62e2c859b771"
WECOM_CORP_SECRET = "y88b58_-eX7-1LXMW9vIV1L3DJbOQ3-XQC3c1CdQi1I"
WECOM_AGENT_ID = 1000004

async def send_sync_messages():
    print("\n--- 正在发送同步 Markdown 消息 ---")

    print("正在发送钉钉同步 Markdown 消息...")
    try:
        response = send_dingtalk(
            message=markdown_content,
            webhook=DINGTALK_WEBHOOK_URL,
            secret=DINGTALK_SECRET,
            msg_type="markdown",
            title="Markdown 同步测试"
        )
        print(f"钉钉同步 Markdown 消息发送成功: {response}")
    except Exception as e:
        print(f"钉钉同步 Markdown 消息发送失败: {e}")

    print("正在发送企业微信 Webhook 同步 Markdown 消息...")
    try:
        response = send_wecom_webhook(
            message=markdown_content,
            webhook=WECOM_WEBHOOK_URL,
            msg_type="markdown"
        )
        print(f"企业微信 Webhook 同步 Markdown 消息发送成功: {response}")
    except Exception as e:
        print(f"企业微信 Webhook 同步 Markdown 消息发送失败: {e}")

    print("正在发送企业微信应用同步 Markdown 消息...")
    try:
        response = send_wecom_app(
            message=markdown_content,
            corpid=WECOM_CORP_ID,
            corpsecret=WECOM_CORP_SECRET,
            agentid=WECOM_AGENT_ID,
            msg_type="markdown",
            touser="@all"
        )
        print(f"企业微信应用同步 Markdown 消息发送成功: {response}")
    except Exception as e:
        print(f"企业微信应用同步 Markdown 消息发送失败: {e}")

async def send_async_messages():
    print("\n--- 正在发送异步 Markdown 消息 ---")

    print("正在发送钉钉异步 Markdown 消息...")
    try:
        response = await send_dingtalk_async(
            message=markdown_content,
            webhook=DINGTALK_WEBHOOK_URL,
            secret=DINGTALK_SECRET,
            msg_type="markdown",
            title="Markdown 异步测试"
        )
        print(f"钉钉异步 Markdown 消息发送成功: {response}")
    except Exception as e:
        print(f"钉钉异步 Markdown 消息发送失败: {e}")

    print("正在发送企业微信 Webhook 异步 Markdown 消息...")
    try:
        response = await send_wecom_webhook_async(
            message=markdown_content,
            webhook=WECOM_WEBHOOK_URL,
            msg_type="markdown"
        )
        print(f"企业微信 Webhook 异步 Markdown 消息发送成功: {response}")
    except Exception as e:
        print(f"企业微信 Webhook 异步 Markdown 消息发送失败: {e}")

    print("正在发送企业微信应用异步 Markdown 消息...")
    try:
        response = await send_wecom_app_async(
            message=markdown_content,
            corpid=WECOM_CORP_ID,
            corpsecret=WECOM_CORP_SECRET,
            agentid=WECOM_AGENT_ID,
            msg_type="markdown",
            touser="@all"
        )
        print(f"企业微信应用异步 Markdown 消息发送成功: {response}")
    except Exception as e:
        print(f"企业微信应用异步 Markdown 消息发送失败: {e}")

async def main():
    await send_sync_messages() # 调用同步发送函数
    await send_async_messages() # 调用异步发送函数

if __name__ == "__main__":
    asyncio.run(main())