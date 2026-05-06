import os
import glob

def fix_npc_scripts():
    scripts_dir = "/home/ubuntu/forgottenserver-10.98/data/npc/scripts/"
    lua_files = glob.glob(os.path.join(scripts_dir, "*.lua"))
    
    include_line = "dofile('data/npc/lib/npcsystem/npcsystem.lua')\n"
    
    fixed_count = 0
    for file_path in lua_files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if it uses KeywordHandler or NpcHandler and doesn't have the include
        if ("KeywordHandler" in content or "NpcHandler" in content) and "npcsystem.lua" not in content:
            print(f"Fixing {os.path.basename(file_path)}...")
            new_content = include_line + content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_count += 1
            
    print(f"Finished. Fixed {fixed_count} scripts.")

if __name__ == "__main__":
    fix_npc_scripts()
