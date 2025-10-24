import os
import json

# --- CONFIGURAZIONE ---
github_user = "open-cobralibero"    # tuo username GitHub
repo = "cobra_plugins"               # nome del repository
branch = "main"                      # branch (di solito main)
images_path = "images"                # cartella immagini nel repo
default_image = "default.png"         # immagine di default se non esiste

# --- FINE CONFIGURAZIONE ---

plugins = []

# Leggi tutti i file .ipk nella cartella corrente
for filename in os.listdir("."):
    if filename.endswith(".ipk"):
        # Nome plugin (senza estensione)
        name = filename.replace(".ipk", "")
        
        # Percorso immagine
        img_file = f"{images_path}/{name}.png"
        if not os.path.exists(img_file):
            img_file = f"{images_path}/{default_image}"  # usa default se non esiste
        
        plugin = {
            "name": name,
            "description": f"Plugin {name}.",   # puoi aggiungere descrizioni personalizzate
            "image": f"https://raw.githubusercontent.com/{github_user}/{repo}/{branch}/{img_file}",
            "file": f"https://raw.githubusercontent.com/{github_user}/{repo}/{branch}/{filename}"
        }
        plugins.append(plugin)

# Salva pluginlist.json
with open("pluginlist.json", "w") as f:
    json.dump(plugins, f, indent=2)

print("pluginlist.json creato con successo! ✅")

