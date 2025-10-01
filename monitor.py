# monitor.py

from flask import Blueprint, jsonify, render_template
import psutil, platform, datetime

monitor_bp = Blueprint("monitor", __name__, template_folder="templates")

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    return {
        "hostname": platform.node(),
        "system": platform.system(),
        "release": platform.release(),
        "cpu_usage": cpu_usage,
        "ram_usage": memory.percent,
        "disk_usage": disk.percent,
        "uptime": str(uptime).split('.')[0]
    }

@monitor_bp.route("/status")
def status():
    return jsonify(get_system_info())

# === Endpoint 2 : Health check ===
@monitor_bp.route("/health")
def health():
    info = get_system_info()
    if info["cpu_usage"] < 80 and info["ram_usage"] < 80:
        return jsonify({"status": "OK"})
    else:
        return jsonify({"status": "WARNING"})

# === Endpoint 3 : Top 5 processus ===
@monitor_bp.route("/processes")
def processes():
    processes = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(p.info)
        except psutil.NoSuchProcess:
            continue
    top = sorted(processes, key=lambda x: (x['cpu_percent'], x['memory_percent']), reverse=True)[:5]
    return jsonify(top)

@monitor_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
