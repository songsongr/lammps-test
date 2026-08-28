"""pytest 公共配置: 将项目根加入 sys.path, 使 `import common` 可用。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
