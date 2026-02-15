
"""
Entry point of the application
"""
import sys
import os

# Ensure proper import resolution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gesture.core.system import SystemController

if __name__ == "__main__":
    app = SystemController()
    app.run()
