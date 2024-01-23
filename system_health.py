import psutil
import datetime

# Define threshold values (adjust as needed)
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100

# Function to check CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"High CPU Usage Alert: {cpu_usage}%")

# Function to check memory usage
def check_memory():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"High Memory Usage Alert: {memory_usage}%")

# Function to check disk space
def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"High Disk Usage Alert: {disk_usage}%")

# Function to check running processes
def check_processes():
    process_count = len(list(psutil.process_iter()))
    if process_count > PROCESS_THRESHOLD:
        print(f"High Number of Running Processes Alert: {process_count}")

# Main function
def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nSystem Health Check - {timestamp}")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

# Execute the main function
if __name__ == "__main__":
    main()

