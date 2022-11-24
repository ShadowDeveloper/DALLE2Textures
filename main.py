import openai
import urllib.request
import os
import time
import PIL.Image
openai.api_key = "KEY"
MINECRAFT_TEXTURES_PATH = "TexturePack\\assets\\minecraft"

# ANIMATED BLOCKS TO NOT GENERATE
OVERRIDE_LIST = ['blast_furnace_front_on', 'campfire_fire', 'campfire_log_lit', 'chain_command_block_back', 'chain_command_block_conditional', 'chain_command_block_front', 'chain_command_block_side', 'command_block_back', 'command_block_conditional', 'command_block_front', 'command_block_side', 'crimson_stem', 'fire_0', 'fire_1', 'kelp', 'kelp_plant', 'lantern', 'lava_flow', 'lava_still', 'magma', 'nether_portal', 'prismarine', 'repeating_command_block_back', 'repeating_command_block_conditional', 'repeating_command_block_front', 'repeating_command_block_side', 'respawn_anchor_top', 'sculk', 'sculk_catalyst_side_bloom', 'sculk_catalyst_top_bloom', 'sculk_sensor_tendril_active', 'sculk_sensor_tendril_inactive', 'sculk_shrieker_can_summon_inner_top', 'sculk_shrieker_inner_top', 'sculk_vein', 'seagrass', 'sea_lantern', 'smoker_front_on', 'soul_campfire_fire', 'soul_campfire_log_lit', 'soul_fire_0', 'soul_fire_1', 'soul_lantern', 'stonecutter_saw', 'tall_seagrass_bottom', 'tall_seagrass_top', 'warped_stem', 'water_flow', 'water_still', 'wind', 'wind_vertical', 'butcher', 'farmer', 'fisherman', 'fletcher', 'librarian', 'shepherd', 'desert', 'snow', 'butcher', 'farmer', 'fisherman', 'fletcher', 'librarian', 'shepherd', 'enchanted_item_glint', 'pumpkinblur', 'shadow', 'vignette', 'vibration']
for (root, dirs, files) in os.walk(MINECRAFT_TEXTURES_PATH, topdown=True):
    if root == "TexturePack\\assets\\minecraft\\textures\\block":
        size = "1024x1024"
        imgCount = 1
        print("Block textures:")
        for file in files:
            # CHECK FOR OVERRIDE
            BAD = False
            for item in OVERRIDE_LIST:
                if item in file:
                    print(f"{file} : OVERRIDE")
                    BAD = True
            if BAD:
                continue
            # CHECK IF WE'VE ALREADY DONE IT
            image = PIL.Image.open(f"AIPack\\assets\\minecraft\\textures\\block\\{file}")
            if not(image.size[0] < 1024 or image.size[1] < 1024):
                print(f"Already done {file}")
                continue
            # CHECK FOR API LIMIT
            if imgCount >= 10:
                print("Reached max, sleeping for 65 secs.")
                time.sleep(65)
                imgCount=1

            name = file.replace(".png", '')
            name = name.replace('_', ' ')
            print(name)
            # GENERATE IMAGE
            response = openai.Image.create(
                prompt=name,
                n=1,
                size=size
            )
            # WRITE IMAGE FILE
            curUrl = 1
            for rawUrl in response["data"]:
                url = rawUrl["url"]
                print(url)
                image = urllib.request.urlretrieve(url, f"AIPack\\assets\\minecraft\\textures\\block\\{file}")
                curUrl += 1
            imgCount += 1
        print('--------------------------------')
    if root == "TexturePack\\assets\\minecraft\\textures\\item":
        size = "512x512"
        imgCount = 1
        print("Item textures:")
        for file in files:
            # CHECK FOR OVERRIDE
            for item in OVERRIDE_LIST:
                if item in file:
                    print(f"{file} : OVERRIDE")
                    continue
            # CHECK IF WE'VE ALREADY DONE IT
            image = PIL.Image.open(f"AIPack\\assets\\minecraft\\textures\\item\\{file}")
            if not (image.size[0] < 512 or image.size[1] < 512):
                print(f"Already done {file}")
                continue
            # CHECK FOR API LIMIT
            if imgCount >= 10:
                print("Reached max, sleeping for 65 secs.")
                time.sleep(65)
                imgCount=1
            name = file.replace(".png", '')
            name = name.replace('_', ' ')
            print(name)
            # GENERATE IMAGE
            response = openai.Image.create(
                prompt=name,
                n=1,
                size=size
            )
            # WRITE IMAGE FILE
            curUrl = 1
            for rawUrl in response["data"]:
                url = rawUrl["url"]
                print(url)
                image = urllib.request.urlretrieve(url, f"AIPack\\assets\\minecraft\\textures\\item\\{file}")
                curUrl += 1
            imgCount += 1
        print('--------------------------------')
    if root == "TexturePack\\assets\\minecraft\\textures\\mob_effect":
        size="256x256"
        imgCount = 1
        print("Effect textures:")
        for file in files:
            # CHECK FOR OVERRIDE
            for item in OVERRIDE_LIST:
                if item in file:
                    print(f"{file} : OVERRIDE")
                    continue
            # CHECK IF WE'VE ALREADY DONE IT
            image = PIL.Image.open(f"AIPack\\assets\\minecraft\\textures\\mob_effect\\{file}")
            if not (image.size[0] < 256 or image.size[1] < 256):
                print(f"Already done {file}")
                continue
            # CHECK FOR API LIMIT
            if imgCount >= 10:
                print("Reached max, sleeping for 65 secs.")
                time.sleep(65)
                imgCount=1
            name = file.replace(".png", '')
            name = name.replace('_', ' ')
            print(name)
            # GENERATE IMAGE
            response = openai.Image.create(
                prompt=name,
                n=1,
                size=size
            )
            # WRITE IMAGE FILE
            curUrl = 1
            for rawUrl in response["data"]:
                url = rawUrl["url"]
                print(url)
                image = urllib.request.urlretrieve(url, f"AIPack\\assets\\minecraft\\textures\\mob_effect\\{file}")
                curUrl += 1
            imgCount += 1
        print('--------------------------------')
