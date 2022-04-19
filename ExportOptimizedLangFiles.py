import os
import sys

print("Hi!")

keep = '    "item.minecraft.', '    "entity.minecraft.', '    "enchantment.', '    "block.minecraft.'
     
try:
    os.makedirs("optimizedLangs", exist_ok=True)
except OSError as err:
    print("?" + err)
    sys.exit(1)

for lang_filename2 in os.listdir('originalLangs'):

    version_file2 = open("originalLangs/" + lang_filename2, 'r', encoding='UTF-8')
    simplified_version_file = open("optimizedLangs/" + lang_filename2.replace(".json", ".lang"), 'w', encoding='UTF-8')

    for line in version_file2:
        if line.startswith(keep):
            if not line.__contains__("entity.minecraft.tropical_fish.") or not line.__contains__("entity.minecraft.villager.") or not line.__contains__("item.minecraft.bundle."): 
                simplified_version_file.write(line.replace('    "', '').replace('": "','=').replace('",', '').replace("Bottleo'", "Bottleo"))
    print("Processed " + lang_filename2)
    version_file2.close()
    simplified_version_file.close()
