import pytest


# 使用 fixture 装饰器创建一个测试 fixture
@pytest.fixture
def sample_data():
    data = {'key1': 'value1', 'key2': 'value2'}
    yield data  # 使用 yield 返回变量，在测试函数执行完毕后进行清理操作（可选）


# 编写测试函数，传入 fixture 作为参数
def test_using_fixture(sample_data):
    print("sample_data:", sample_data)  # 打印引用的变量
    # 继续进行其他操作
