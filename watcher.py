import time
import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from patterns import PATTERNS
from notifier import alert

class LogHandler(FileSystemEventHandler):
    def __init__(self, logfile):
        self.logfile = logfile
        # start at end of file
        self._fp = open(self.logfile, "r")
        self._fp.seek(0, 2)

    def on_modified(self, event):
        if event.src_path != self.logfile:
            return
        for line in self._fp:
            self.process_line(line)

    def process_line(self, line: str):
        for name, regex in PATTERNS.items():
            match = regex.search(line)
            if match:
                alert(name, f"{name} detected:\n{line.strip()}")
                # optionally break to avoid duplicate alerts
                break

def main():
    # load config
    cfg = yaml.safe_load(open("config.yaml"))
    path = cfg["log_path"]

    event_handler = LogHandler(path)
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()

    print(f"Watching {path} for suspicious events…")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
