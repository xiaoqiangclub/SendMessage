# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-12T00:13:13.929Z
# 文件描述：同步发送钉钉消息的示例
# 文件路径：examples/send_dingtalk_sync.py

from xqcsendmessage import send_dingtalk  # 导入新的顶层函数

# --- 配置 ---
# 你的钉钉机器人的 Webhook 和密钥
WEBHOOK_URL = "YOUR_DINGTALK_WEBHOOK_URL"  # 请替换为您的钉钉机器人 Webhook URL
SECRET = "YOUR_DINGTALK_SECRET"  # 请替换为您的钉钉机器人密钥，如果没有则为 None


def main():
    """主函数"""
    print("\n--- 直接函数调用模式 ---")
    try:
        # 发送字符串消息，消息类型和 @ 人相关的参数通过 kwargs 传递
        result_direct_str = send_dingtalk(
            "这是一条来自 sendmessage 直接发送的同步测试消息 (字符串)。",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            msg_type="text",  # 消息类型为文本
            is_at_all=True  # 发送给所有人
        )
        print(f"✅ 钉钉消息发送成功 (字符串): {result_direct_str}")

        # 发送字符串消息，消息类型和 @ 人相关的参数通过 kwargs 传递
        result_direct_str_at = send_dingtalk(
            "这是一条来自 sendmessage 直接发送的同步测试消息 (覆盖 @ 人，指定手机号，markdown 类型)。",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            msg_type="markdown",
            at_mobiles=["YOUR_MOBILE_NUMBER"],
            is_at_all=False
        )
        print(f"✅ 钉钉消息发送成功 (覆盖 @ 人): {result_direct_str_at}")


        # 发送字典消息，消息类型和 @ 人相关的参数通过 kwargs 传递
        result_direct_dict = send_dingtalk(
            {
                "msgtype": "markdown",
                "markdown": {
                    "title": "测试标题",
                    "text": "### 【XQCSendMessage】这是一条通过 sendmessage 直接发送的同步测试消息 (字典，指定手机号，markdown 类型)。"
                }
            },
            webhook=WEBHOOK_URL,
            secret=SECRET,
            msg_type="markdown",
            at_mobiles=["YOUR_MOBILE_NUMBER"],
            is_at_all=False
        )
        print(f"✅ 直接调用钉钉发送成功 (字典): {result_direct_dict}")
    except Exception as e:
        print(f"🔥 直接调用钉钉发送失败: {e}")


if __name__ == "__main__":
    main()
