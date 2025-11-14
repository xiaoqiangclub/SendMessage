# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-14
# 文件描述：测试发送企业微信应用图片消息

import os
from xqcsendmessage import send_wecom_app

# --- 配置 ---
# --- 配置 ---
# 从环境变量中获取企业微信凭据
# 强烈建议使用环境变量来管理敏感信息
CORP_ID = os.getenv("WECOM_CORPID")
CORP_SECRET = os.getenv("WECOM_CORPSECRET")
AGENT_ID = int(os.getenv("WECOM_AGENTID", 100002))

# 接收者，@all 表示所有
TO_USER = "@all"

# 要发送的图片路径 (请确保此图片存在)
# 为了方便测试，我们使用项目中的示例图片
IMAGE_PATH = "images/SendMessage.jpeg"

def test_send_image():
    """
    测试发送企业微信应用图片消息。
    """
    if not all([CORP_ID, CORP_SECRET, AGENT_ID]):
        print("🔥 请设置 WECOM_CORPID, WECOM_CORPSECRET, 和 WECOM_AGENTID 环境变量。")
        return

    try:
        print("🚀 准备发送企业微信应用图片消息...")
        result = send_wecom_app(
            corpid=CORP_ID,
            corpsecret=CORP_SECRET,
            agentid=AGENT_ID,
            touser=TO_USER,
            image_path=IMAGE_PATH
        )
        print(f"✅ 图片消息发送成功: {result}")
    except Exception as e:
        print(f"🔥 发送失败: {e}")

if __name__ == "__main__":
    test_send_image()