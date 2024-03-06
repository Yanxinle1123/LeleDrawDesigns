from setuptools import setup, find_packages

setup(
    name="LeleDrawDesigns",
    version="1.2.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "scipy",
        "numpy",
    ],
    author="YanXinle",
    author_email="1020121123@qq.com",
    description="根据信息绘制折线图, 直方图, 可以把图片保存到当前目录",

    url="https://github.com/Yanxinle1123/LeleDrawDesigns",
)
