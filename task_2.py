import psutil


def system_monitor():
    cpu_percent = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    mem_used_percent = mem.percent
    mem_used_mb = mem.used / (1024 * 1024)
    mem_total_mb = mem.total / (1024 * 1024)

    disk = psutil.disk_usage('/')
    disk_percent = disk.percent

    print(f"Загрузка CPU: {cpu_percent}%")
    print(f"Использование памяти: {mem_used_mb:.2f} MB / {mem_total_mb:.2f} MB ({mem_used_percent}%)")
    print(f"Загрузка диска: {disk_percent}%")


if __name__ == "__main__":
    system_monitor()