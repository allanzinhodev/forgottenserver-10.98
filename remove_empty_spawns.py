import xml.etree.ElementTree as ET
import os

def remove_empty_spawns(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    print(f"Parsing {file_path}...")
    # Preserve comments is hard with ElementTree, but we'll try to be clean.
    # For a simple cleanup, ET is fine.
    tree = ET.parse(file_path)
    root = tree.getroot()

    spawns_removed = 0
    total_spawns = 0
    
    # We need to iterate backwards or collect to remove
    to_remove = []
    
    for spawn in root.findall('spawn'):
        total_spawns += 1
        monsters = spawn.findall('monster')
        npcs = spawn.findall('npc')
        
        # Only remove if it has NO monsters AND NO NPCs
        if len(monsters) == 0 and len(npcs) == 0:
            to_remove.append(spawn)
            spawns_removed += 1
        elif len(monsters) == 0:
            print(f"Skipping spawn at {spawn.get('centerx')}, {spawn.get('centery')} because it contains NPCs.")


    for spawn in to_remove:
        root.remove(spawn)

    # Save the modified XML
    tree.write(file_path, encoding="UTF-8", xml_declaration=True)
    
    print(f"Finished. Total spawns: {total_spawns}. Spawns removed: {spawns_removed}.")
    print(f"Remaining spawns: {total_spawns - spawns_removed}.")

if __name__ == "__main__":
    file_path = "/home/ubuntu/forgottenserver-10.98/data/world/Shinobi Online Map-spawn.xml"
    remove_empty_spawns(file_path)
