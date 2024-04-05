import os
import imageio.v3 as iio
import glob
from rrg_db import DatabaseManager

png_dir = "src/plots"
gif_dir = "src/gifs"
config = DatabaseManager().get_config()

images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith(".png"):
        file_path = os.path.join(png_dir, file_name)
        images.append(iio.imread(file_path))
iio.imwrite(
    "src/gifs/" + config["filename"] + "_" + str(len(os.listdir(gif_dir)) + 1) + ".gif",
    images,
    duration=config["gif_frame_time_delay"],
)

if config["remove_files_after_gif"]:
    files = glob.glob(png_dir + "/*")
    for f in files:
        os.remove(f)
