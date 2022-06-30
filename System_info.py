import psutil
import platform


class System_info:
    def get_size(self, bytes, suffix="B\n"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if int(bytes) < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes = int(bytes) / factor

    def print_title(self, title: str):
        return ("_" * 20 + title + "_" * 20+'\n')

    def system_info(self):
        uname = platform.uname()
        output = ''
        output += self.print_title("CPU Info")
        output += (f"System: {uname.system}\n")
        output += (f"Node Name: {uname.node}\n")
        output += (f"Release: {uname.release}\n")
        output += (f"Version: {uname.version}\n")
        output += (f"Machine: {uname.machine}\n")
        output += (f"Processor: {uname.processor}\n")
        return output

    def cpu_info(self):
        cpufreq = psutil.cpu_freq()
        output = ''
        output += self.print_title("CPU Info")
        output += ("Physical cores:" + str(psutil.cpu_count(logical=False)))
        output += ("Total cores:" + str(psutil.cpu_count(logical=True)))
        output += (f"Max Frequency: {cpufreq.max:.2f}Mhz\n")
        output += (f"Min Frequency: {cpufreq.min:.2f}Mhz\n")
        output += (f"Current Frequency: {cpufreq.current:.2f}Mhz\n")
        output += (f"Total CPU Usage: {psutil.cpu_percent()}%\n")
        return output

    def memory_info(self):
        output = ''
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        output += self.print_title("Memory Information")
        output += (f"Total: {self.get_size(svmem.total)}\n")
        output += (f"Available: {self.get_size(svmem.available)}\n")
        output += (f"Used: {self.get_size(svmem.used)}\n")
        output += (f"Percentage: {svmem.percent}%\n")
        output += ("_" * 20 + "SWAP" + "_" * 20)
        output += (f"Total: {self.get_size(str(swap.total))}\n")
        output += (f"Free: {self.get_size(str(swap.free))}\n")
        output += (f"Used: {self.get_size(str(swap.used))}\n")
        output += (f"Percentage: {swap.percent}%\n")
        return output

    def disk_info(self):
        output = ''
        output += self.print_title("Disk Information")
        disk_io = psutil.disk_io_counters()
        partitions = psutil.disk_partitions()
        output += ("Partitions and Usage:\n")
        for partition in partitions:
            output += (f"________Device: {partition.device}________\n")
            output += (f"        Mountpoint: {partition.mountpoint}\n")
            output += (f"        File system type: {partition.fstype}\n")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            output += (f"   Total Size: {self.get_size(partition_usage.total)}\n")
            output += (f"   Used: {self.get_size(partition_usage.used)}\n")
            output += (f"   Free: {self.get_size(partition_usage.free)}\n")
            output += (f"   Percentage: {partition_usage.percent}%\n")
        output += (f"Total read: {self.get_size(disk_io.read_bytes)}\n")
        output += (f"Total write: {self.get_size(disk_io.write_bytes)}\n")
        return output
