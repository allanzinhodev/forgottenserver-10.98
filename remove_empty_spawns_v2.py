import xml.etree.ElementTree as ET

def remove_empty_spawns(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    initial_count = len(root.findall('spawn'))
    spawns_to_remove = []
    
    for spawn in root.findall('spawn'):
        # If the spawn has no children (monsters or npcs), it's empty
        if len(spawn) == 0:
            spawns_to_remove.append(spawn)
            
    for spawn in spawns_to_remove:
        root.remove(spawn)
        
    removed_count = len(spawns_to_remove)
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    
    print(f"Removed {removed_count} empty spawns. Initial count: {initial_count}. Final count: {len(root.findall('spawn'))}.")

if __name__ == "__main__":
    remove_empty_spawns("/home/ubuntu/forgottenserver-10.98/data/world/Shinobi Online Map-spawn.xml")
