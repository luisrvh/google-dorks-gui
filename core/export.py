import csv
import os
from core.driver import base_dir


def save_csv(engine, dork, results):
    path = os.path.join(base_dir(), "resultados_dorks.csv")

    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ENGINE", engine])
        w.writerow(["DORK", dork])
        w.writerow(["TITLE", "URL"])
        w.writerows(results)
        w.writerow([])
