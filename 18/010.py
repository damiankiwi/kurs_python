import platform

system_info = {
    "System": platform.system(),
    "Release": platform.release(),
    "Version": platform.version(),
    "Machine": platform.machine(),
    "Processor": platform.processor()
}

print("Informacje o systemie operacyjnym:")
for key, value in system_info.items():
    print(f"{key}: {value}")
