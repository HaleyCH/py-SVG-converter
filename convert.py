import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import potrace
import svgwrite
import argparse

def create_svg_with_center(img, centers, fp):
    mh,mw = img.shape[:2]
    dwg = svgwrite.Drawing(fp, profile='tiny', viewBox=f"0 0 {mw} {mh}")
    for i in range(centers.shape[0]):
        bmp = potrace.Bitmap(img[:, :, i])

        # Trace the bitmap to a path
        path = bmp.trace()

        # Iterate over path curves
        path_data = ''
        for curve in path:
            start_x, start_y = curve.start_point
            path_data += f'M {start_x} {start_y}'
            for segment in curve:
                # Get the end point of the segment
                end_x, end_y = segment.end_point

                # Check if the segment is a corner or a Bezier curve
                if segment.is_corner:
                    # If it's a corner, add a line to the path data
                    path_data += f' L {end_x} {end_y}'
                else:
                    # If it's a Bezier curve, add a cubic Bezier curve
                    # to the path data
                    c1_x, c1_y = segment.c1
                    c2_x, c2_y = segment.c2
                    path_data += f' C {c1_x} {c1_y} {c2_x} {c2_y} {end_x} {end_y}'

        path = dwg.path(d=path_data)
        path.fill(color=f'rgb({int(centers[i][0])}, {int(centers[i][1])}, {int(centers[i][2])})')  # Set the fill color of the path
        dwg.add(path)
    
    dwg.save(fp)

def kmeans(img, n_clusters):

    im_array = np.array(img)[:, :, :3]
    iw,ih = im_array.shape[:2]

    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(im_array.reshape(-1, im_array.shape[-1]))

    labels = kmeans.predict(im_array.reshape(-1, im_array.shape[-1]))
    centers = kmeans.cluster_centers_

    centers_tile = np.tile(centers, (im_array.shape[0], im_array.shape[1], 1, 1)).transpose([0, 1, 3, 2])

    r_im = im_array.reshape((iw, ih, 3, 1))

    dists = np.sum((r_im - centers_tile) ** 2, axis=2)

    min_idx = np.argmin(dists, axis=2)

    new_img = np.zeros(list(list(im_array.shape[:2]) + [n_clusters]))
    rows, cols = np.indices(new_img.shape[:2])
    new_img[rows, cols, min_idx] = 1

    return new_img, centers

def convert(i, c, o):
    img, rgbs = kmeans(i, c)
    create_svg_with_center(img, rgbs, o)

def get_parse(p:argparse.ArgumentParser):
    p.add_argument('-i','--input', default='./input.png', help="input file path, default: ./input.png")
    p.add_argument('-o','--output', default='./output.svg', help="output file path, default: ./output.svg")
    p.add_argument('-n','--n_color', default=5, type=int, help="color number to cluster, default: 5")
    return p

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="python convert.py [--input path/to/input]  [--output path/to/output] [--n_color cluster center color number]")
    parser = get_parse(parser)
    args = parser.parse_args()

    im = Image.open(args.input)
    ia = np.array(im)
    convert(ia,args.n_color,args.output)
