import threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from core.search import run_search
from core.export import save_csv
from dorks.default_dorks import DORKS

from engines.google import ENGINE as GOOGLE
from engines.duckduckgo import ENGINE as DUCK
from engines.bing import ENGINE as BING


ENGINES = {
    "Google": GOOGLE,
    "DuckDuckGo": DUCK,
    "Bing": BING
}


def launch():
    app = ttk.Window(
        title="Google Dorks GUI (Modular)",
        themename="darkly",
        size=(900, 650)
    )

    frame = ttk.Frame(app, padding=10)
    frame.pack(fill=BOTH, expand=True)

    # =====================
    # INPUTS
    # =====================
    ttk.Label(frame, text="Dominio").pack(anchor=W)
    entry_domain = ttk.Entry(frame)
    entry_domain.pack(fill=X, pady=5)

    ttk.Label(frame, text="Dork").pack(anchor=W)
    combo_dork = ttk.Combobox(
        frame,
        values=list(DORKS.keys()),
        state="readonly"
    )
    combo_dork.current(0)
    combo_dork.pack(fill=X, pady=5)

    ttk.Label(frame, text="Motor de búsqueda").pack(anchor=W)
    combo_engine = ttk.Combobox(
        frame,
        values=list(ENGINES.keys()),
        state="readonly"
    )
    combo_engine.current(0)
    combo_engine.pack(fill=X, pady=5)

    # =====================
    # BOTONES
    # =====================
    buttons = ttk.Frame(frame)
    buttons.pack(pady=10)

    btn_search = ttk.Button(
        buttons,
        text="Buscar (1 a la vez)",
        bootstyle=SUCCESS
    )
    btn_search.pack(side=LEFT, padx=5)

    btn_clear = ttk.Button(
        buttons,
        text="Limpiar / Regresar",
        bootstyle=SECONDARY
    )
    btn_clear.pack(side=LEFT, padx=5)

    # =====================
    # ESTADO
    # =====================
    status_label = ttk.Label(frame, text="Listo")
    status_label.pack(anchor=W, pady=5)

    # =====================
    # RESULTADOS
    # =====================
    output = ttk.Text(frame, height=22)
    output.pack(fill=BOTH, expand=True)

    # =====================
    # LÓGICA
    # =====================
    def limpiar():
        entry_domain.delete(0, END)
        output.delete("1.0", END)
        status_label.config(text="Listo")

    def buscar():
        btn_search.config(state=DISABLED)
        status_label.config(text="🔍 Buscando...")
        output.delete("1.0", END)

        domain = entry_domain.get().strip()
        if not domain:
            output.insert(END, "Ingresa un dominio válido\n")
            btn_search.config(state=NORMAL)
            status_label.config(text="Error")
            return

        dork = DORKS[combo_dork.get()].format(dominio=domain)
        engine = ENGINES[combo_engine.get()]

        output.insert(END, f"[{engine['name']}]\n{dork}\n\n")

        try:
            results = run_search(engine, dork)

            if not results:
                output.insert(END, "Sin resultados\n")

            for title, url in results:
                output.insert(END, f"{title}\n{url}\n\n")

            save_csv(engine["name"], dork, results)
            status_label.config(text="✅ Finalizado")

        except Exception as e:
            output.insert(END, f"Error: {e}\n")
            status_label.config(text="Error")

        btn_search.config(state=NORMAL)

    btn_search.config(
        command=lambda: threading.Thread(target=buscar, daemon=True).start()
    )
    btn_clear.config(command=limpiar)

    app.mainloop()
