# 🧠 Základy terminálu a Linuxového prostředí – část 2

## 🔁 Co se stane, když napíšeš příkaz do terminálu?

1. Napíšeš příkaz – třeba `ls`
2. Terminál ho předá tzv. shellu (např. Bash)
3. Shell ten příkaz vyhledá jako program
4. Program se spustí a vypíše výsledek
5. Výstup se zobrazí zpátky v terminálu

> Každý příkaz je vlastně program (soubor), který se spustí

---

## 🧰 Co je shell a proč Bash?

- Shell je rozhraní mezi tebou a systémem – něco jako „překladač“
- Na Macu i Linuxu je to často Bash (Bourne Again SHell)
- Alternativy: `zsh`, `fish`, `sh`

---

## 🧭 Co znamenají některé speciální znaky?

| Znak | Význam |
|------|--------|
| `~` | Domácí složka (např. `/Users/lukasfrantisak`) |
| `.` | Aktuální složka |
| `..` | O jednu složku výš |
| `/` | Oddělovač složek |
| `>` | Přesměrování výstupu (přepíše) |
| `>>` | Přesměrování výstupu (připojí) |
| `|` | Roura – propojí dva příkazy |
| `*` | Zástupný znak (např. `*.txt`) |

---

## 💬 Co je argument a co je přepínač?

Příklad:

```bash
ls -l /Users/lukasfrantisak
```

- `ls` je příkaz
- `-l` je přepínač (option), např. „zobraz to detailně“
- `/Users/lukasfrantisak` je argument = složka, na kterou se má `ls` podívat

Další příklady:
```bash
ls -a          # zobrazí i skryté soubory
rm -r slozka   # smaže složku i s obsahem
```

---

## 📂 Jak vypadá souborová struktura systému?

| Složka | Popis |
|--------|-------|
| `/` | Root – úplný začátek všeho |
| `/home/` nebo `/Users/` | Domácí složky uživatelů |
| `/bin/` | Spustitelné programy |
| `/etc/` | Konfigurační soubory |
| `/var/` | Logy a data služeb |
| `/tmp/` | Dočasné soubory |

---

## 🛡️ Oprávnění a přístup

Každý soubor má vlastníka a oprávnění. Např. výpis `ls -l`:

```
-rw-r--r--  1 lukasfrantisak staff  1234 Mar 29 13:00 linux_cheatsheet.txt
```

- `-rw-r--r--` = oprávnění
- `lukasfrantisak` = vlastník
- `staff` = skupina
- `1234` = velikost v bajtech

---

## ✅ Shrnutí

- Terminál = přímá kontrola nad systémem
- Každý příkaz = program
- Shell = prostředník mezi tebou a systémem
- Základy terminálu jsou důležité pro DevOps, cloud i automatizaci
