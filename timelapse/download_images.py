import os
import os.path
import urllib.request

machinenames = ["control_pfc",
                "with_basil_pfc",
                "blue_night_pfc"]

machinename = machinenames[1]

inputfile = os.path.join("..", "data", machinename, "Camera-Top.csv")
outdir = os.path.join(".",machinename)

urls = []
with open(inputfile) as inf:
    print("reading input file")
    for line in inf.readlines():
        if "http" in line:
            urls.append(line.split(",")[3])
print(urls[0])

processed_images = 0
print("total files: {}".format(len(urls)))

if not os.path.exists(outdir):
    os.makedirs(outdir)

for image in urls:
    processed_images = processed_images + 1
    if processed_images % 100 == 0:
        print("{} of {}".format(processed_images, len(urls)))
    imagefile = os.path.join(".", machinename, image[image.rfind("/") + 1:])
    if not os.path.exists(imagefile):
        urllib.request.urlretrieve(image, imagefile)
        # print(os.path.abspath(imagefile))
