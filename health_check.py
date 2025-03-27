import psutil
import platform
import datetime

def get_system_info():
    print("System Info")
    print("-----------")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Uptime: {datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())}")
    print()

def get_usage_stats():
    print("Usage Stats")
    print("-----------")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    print()

if __name__ == "__main__":
    get_system_info()
    get_usage_stats()