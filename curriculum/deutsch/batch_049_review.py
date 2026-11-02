"""Review DE-UZ-049 and separate the bounded GS4 word-level connection."""
from pathlib import Path
import json

def append(T):
 T("wortebene-regelmaessigkeiten4","Wortschreibungen sicher nutzen: Doppelkonsonanten und Auslautverhärtung","186879","40226","Bekannte zweisilbige Wörter mit Doppelkonsonanten sowie verwandte Wortformen mit Auslautverhärtung","","Erste Unterschiede zwischen Sprech- und Schreibweise bei Doppelkonsonanten und Auslautverhärtung wahrnehmen.","Begrenzter Wortebenen-Anschluss mit FSP-Einblick; keine vollständige Regelanwendung.",["186881"])

def refine(cards):
 patches=json.loads((Path(__file__).parent/"batch_049_cards.json").read_text())
 assert set(patches).issubset({c["id"] for c in cards})
 for c in cards:
  if c["id"] in patches:
   cid=c["id"]
   c.clear()
   c.update(patches[cid])
