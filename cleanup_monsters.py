import os
import xml.etree.ElementTree as ET

# Paths
BASE_DIR = "/home/ubuntu/forgottenserver-10.98"
MONSTER_DIR = os.path.join(BASE_DIR, "data/monster")
MONSTERS_XML = os.path.join(MONSTER_DIR, "monsters.xml")
SPAWN_XML = os.path.join(BASE_DIR, "data/world/Shinobi Online Map-spawn.xml")

def cleanup():
    if not os.path.exists(MONSTERS_XML):
        print(f"Error: {MONSTERS_XML} not found.")
        return

    # 1. Parse monsters.xml
    print(f"Parsing {MONSTERS_XML}...")
    tree = ET.parse(MONSTERS_XML)
    root = tree.getroot()
    
    referenced_files = set()
    referenced_names = set()
    
    for monster in root.findall('monster'):
        file_path = monster.get('file')
        name = monster.get('name')
        
        if file_path:
            # Normalize path (handling slashes)
            norm_path = os.path.normpath(file_path)
            referenced_files.add(norm_path)
            
        if name:
            referenced_names.add(name)

    print(f"Found {len(referenced_files)} referenced monster files.")
    print(f"Found {len(referenced_names)} referenced monster names.")

    # 2. Delete orphaned monster files
    print("\nCleaning up data/monster/ directory...")
    deleted_files_count = 0
    for root_dir, dirs, files in os.walk(MONSTER_DIR):
        for file in files:
            if file == "monsters.xml":
                continue
                
            full_path = os.path.join(root_dir, file)
            rel_path = os.path.relpath(full_path, MONSTER_DIR)
            
            # Normalize for comparison
            norm_rel_path = os.path.normpath(rel_path)
            
            if norm_rel_path not in referenced_files:
                print(f"Deleting unreferenced file: {rel_path}")
                os.remove(full_path)
                deleted_files_count += 1

    # Cleanup empty directories
    for root_dir, dirs, files in os.walk(MONSTER_DIR, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root_dir, d)
            if not os.listdir(dir_path):
                print(f"Deleting empty directory: {dir_path}")
                os.rmdir(dir_path)

    print(f"Deleted {deleted_files_count} files.")

    # 3. Clean spawn XML
    if os.path.exists(SPAWN_XML):
        print(f"\nCleaning up {SPAWN_XML}...")
        spawn_tree = ET.parse(SPAWN_XML)
        spawn_root = spawn_tree.getroot()
        
        monsters_removed = 0
        
        # Iterate spawns
        for spawn in spawn_root.findall('spawn'):
            # Find all monster tags within this spawn
            for monster in spawn.findall('monster'):
                m_name = monster.get('name')
                if m_name not in referenced_names:
                    print(f"Removing unreferenced monster spawn: {m_name}")
                    spawn.remove(monster)
                    monsters_removed += 1
            
            # Optionally remove empty spawns if the user wants, 
            # but usually they are left as markers or contain NPCs.
            # Looking at the requirement: "delete all lines... of monsters that are not referenced".
            # This implies the monster entries.
            
        spawn_tree.write(SPAWN_XML, encoding="UTF-8", xml_declaration=True)
        print(f"Removed {monsters_removed} monster spawn entries.")
    else:
        print(f"Warning: {SPAWN_XML} not found.")

if __name__ == "__main__":
    cleanup()
