# 作者：Xiaoqiang
# 微信公众号：XiaoqiangClub
# 创建时间：2025-11-13T05:03:42.610Z
# 文件描述：测试同步发送钉钉消息功能
# 文件路径：examples/test_send_dingtalk.py

from xqcsendmessage import send_dingtalk

# --- 配置 ---
WEBHOOK_URL = "YOUR_DINGTALK_WEBHOOK_URL"
SECRET = "YOUR_DINGTALK_SECRET"

# --- 测试函数 ---

def test_text_message():
    """测试发送纯文本消息"""
    try:
        result = send_dingtalk(
            "【XQCSendMessage 同步测试】\n功能点: send_dingtalk\n消息类型: Text",
            webhook=WEBHOOK_URL,
            secret=SECRET
        )
        print(f"✅ [test_text_message] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_text_message] 发送失败: {e}")

def test_markdown_message():
    """测试发送 Markdown 消息"""
    try:
        result = send_dingtalk(
            "### 【XQCSendMessage 同步测试】\n- **功能点**: send_dingtalk\n- **消息类型**: Markdown",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            send_md=True,
            title="【同步测试】Markdown 消息"
        )
        print(f"✅ [test_markdown_message] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_markdown_message] 发送失败: {e}")

def test_at_all():
    """测试 @所有人"""
    try:
        result = send_dingtalk(
            "【XQCSendMessage 同步测试】\n功能点: send_dingtalk\n@类型: @所有人",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            is_at_all=True
        )
        print(f"✅ [test_at_all] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_at_all] 发送失败: {e}")

def test_at_mobiles():
    """测试 @指定手机号"""
    try:
        result = send_dingtalk(
            "【XQCSendMessage 同步测试】\n功能点: send_dingtalk\n@类型: @指定手机号",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            at_mobiles=["YOUR_MOBILE_NUMBER"] # 替换为需要@的手机号
        )
        print(f"✅ [test_at_mobiles] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_at_mobiles] 发送失败: {e}")

def test_at_mobiles_override_at_all():
    """测试 @指定手机号时，is_at_all 会被忽略"""
    try:
        result = send_dingtalk(
            "【XQCSendMessage 同步测试】\n功能点: send_dingtalk\n逻辑: at_mobiles 覆盖 is_at_all\n预期: 只@手机号，不@所有人",
            webhook=WEBHOOK_URL,
            secret=SECRET,
            at_mobiles=["YOUR_MOBILE_NUMBER"],
            is_at_all=True # 此参数应被忽略
        )
        print(f"✅ [test_at_mobiles_override_at_all] 发送成功: {result}")
    except Exception as e:
        print(f"🔥 [test_at_mobiles_override_at_all] 发送失败: {e}")

if __name__ == "__main__":
    print("--- 开始测试 send_dingtalk ---")
    test_text_message()
    print("-" * 20)
    test_markdown_message()
    print("-" * 20)
    test_at_all()
    print("-" * 20)
    test_at_mobiles()
    print("-" * 20)
    test_at_mobiles_override_at_all()
    print("--- 测试结束 ---")