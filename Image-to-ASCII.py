def ASCIIify(image_url, max_columns=80, background_is_dark=False):
    from PIL import Image, ImageOps
    import csv
    from bisect import bisect_left
    import urllib2
    import cStringIO

    ##brightness_list = csv.reader(open('brightnesslist.csv', 'rb'), delimiter=',', quotechar='"')
    ##char_wt = []
    ##for row in brightness_list:
    ##    if row[1]!='':
    ##        char_wt.append({'char': int(row[1]), 'brightness': float(row[3])})
    char_wt = [ {'char': 32, 'brightness': 0.0},\
               {'char': 32, 'brightness': 0.0}, {'char': 96, 'brightness': 1.29}, \
               {'char': 46, 'brightness': 2.44}, {'char': 94, 'brightness': 2.96}, \
               {'char': 126, 'brightness': 2.96}, {'char': 95, 'brightness': 3.73}, \
               {'char': 45, 'brightness': 3.86}, {'char': 39, 'brightness': 4.24}, \
               {'char': 44, 'brightness': 4.43}, {'char': 124, 'brightness': 4.5}, \
               {'char': 40, 'brightness': 4.63}, {'char': 41, 'brightness': 4.63}, \
               {'char': 58, 'brightness': 4.88}, {'char': 42, 'brightness': 5.27}, \
               {'char': 33, 'brightness': 5.4}, {'char': 62, 'brightness': 5.46}, \
               {'char': 60, 'brightness': 5.53}, {'char': 37, 'brightness': 5.66}, \
               {'char': 43, 'brightness': 5.66}, {'char': 47, 'brightness': 5.66}, \
               {'char': 92, 'brightness': 5.66}, {'char': 123, 'brightness': 5.66},\
               {'char': 125, 'brightness': 5.66}, {'char': 59, 'brightness': 6.04},\
               {'char': 61, 'brightness': 6.17}, {'char': 91, 'brightness': 6.17},\
               {'char': 93, 'brightness': 6.17}, {'char': 55, 'brightness': 6.43},\
               {'char': 105, 'brightness': 6.88}, {'char': 49, 'brightness': 7.07},\
               {'char': 63, 'brightness': 7.07}, {'char': 108, 'brightness': 7.07},\
               {'char': 34, 'brightness': 7.33}, {'char': 114, 'brightness': 7.45},\
               {'char': 99, 'brightness': 7.65}, {'char': 73, 'brightness': 7.71},\
               {'char': 106, 'brightness': 7.71}, {'char': 116, 'brightness': 7.71},\
               {'char': 122, 'brightness': 7.84}, {'char': 118, 'brightness': 7.97},\
               {'char': 50, 'brightness': 8.1}, {'char': 111, 'brightness': 8.23},\
               {'char': 74, 'brightness': 8.35}, {'char': 51, 'brightness': 8.55},\
               {'char': 38, 'brightness': 8.74}, {'char': 67, 'brightness': 8.74},\
               {'char': 117, 'brightness': 8.74}, {'char': 120, 'brightness': 8.8},\
               {'char': 89, 'brightness': 8.87}, {'char': 48, 'brightness': 8.93},\
               {'char': 53, 'brightness': 8.93}, {'char': 76, 'brightness': 9.0},\
               {'char': 115, 'brightness': 9.19}, {'char': 121, 'brightness': 9.25},\
               {'char': 52, 'brightness': 9.38}, {'char': 110, 'brightness': 9.38},\
               {'char': 57, 'brightness': 9.51}, {'char': 86, 'brightness': 9.51},\
               {'char': 102, 'brightness': 9.58}, {'char': 84, 'brightness': 9.77},\
               {'char': 107, 'brightness': 9.77}, {'char': 54, 'brightness': 9.83},\
               {'char': 79, 'brightness': 9.9}, {'char': 119, 'brightness': 9.96},\
               {'char': 56, 'brightness': 10.03}, {'char': 101, 'brightness': 10.03},\
               {'char': 97, 'brightness': 10.15}, {'char': 90, 'brightness': 10.35},\
               {'char': 36, 'brightness': 10.41}, {'char': 80, 'brightness': 10.41},\
               {'char': 83, 'brightness': 10.47}, {'char': 71, 'brightness': 10.67},\
               {'char': 68, 'brightness': 10.73}, {'char': 88, 'brightness': 10.73},\
               {'char': 104, 'brightness': 10.73}, {'char': 70, 'brightness': 10.8},\
               {'char': 85, 'brightness': 10.8}, {'char': 103, 'brightness': 11.5},\
               {'char': 100, 'brightness': 11.82}, {'char': 98, 'brightness': 11.95},\
               {'char': 82, 'brightness': 12.08}, {'char': 65, 'brightness': 12.15},\
               {'char': 75, 'brightness': 12.15}, {'char': 109, 'brightness': 12.47},\
               {'char': 112, 'brightness': 12.53}, {'char': 113, 'brightness': 12.53},\
               {'char': 64, 'brightness': 12.6}, {'char': 69, 'brightness': 12.72},\
               {'char': 81, 'brightness': 12.79}, {'char': 72, 'brightness': 12.98},\
               {'char': 35, 'brightness': 13.37}, {'char': 66, 'brightness': 13.37},\
               {'char': 78, 'brightness': 13.5}, {'char': 87, 'brightness': 14.91},\
               {'char': 77, 'brightness': 15.36}]
    imfile = urllib2.urlopen(image_url)
    img = cStringIO.StringIO(imfile.read())
    im = Image.open(img)
    max_rows = int(0.3 * max_columns);  # as a result of the 8x5 dimensions of the character bounding box
    ascii_size = (max_columns, max_rows)
    im = im.resize(ascii_size)
    im_bright = ImageOps.grayscale(im)
    (num_columns, num_rows) = im.size
    bright_pixels = list(im_bright.getdata())
    (min_bright_thumb, max_bright_thumb) = im_bright.getextrema()

    # ASCII brightness values, should be sorted with lowest at index 0 and highest at index -1
    abv = [char['brightness'] for char in char_wt]
    min_bright_char = char_wt[0]
    max_bright_char = char_wt[-1]
    delta_error = 0
    ascii_art = ''
    for row in range(num_rows):
        row_string = ''
        for column in range(num_columns):
            pixel = bright_pixels[row * num_columns + column]
            # Take the pixel brightness value and convert to scale of ASCII brightness
            calibrated_pixel = (float(pixel) / (max_bright_thumb - min_bright_thumb)) * \
                               (max_bright_char['brightness'] - min_bright_char['brightness']) + \
                               min_bright_char['brightness']
            # Find where this brightness value would be inserted into the ASCII brightness values list
            abv_index = bisect_left(abv, calibrated_pixel)
            # This special line below if we want to mirror the brightness scale
            if not background_is_dark:
                abv_index = len(abv) - abv_index
            # Cleaning up after bisect_left, I don't want your shitty numbers
            if (abv_index == 0):
                abv_index = 1
            if (abv_index == len(abv)):
                abv_index = len(abv) - 1
            # how close is the pixel to the previous ASCII character's brightness value?
            delta_lower = abs(abv[abv_index - 1] - calibrated_pixel)
            # how close is the pixel to the character's brightness value at the insertion point?
            delta_upper = abs(abv[abv_index] - calibrated_pixel)
            closest_char = ''
            # By using delta_error on the other side of the comparison, it encourages
            # choice of character that results in the lowest delta_error overall (without
            # looking ahead)
            if (delta_lower < delta_upper + delta_error):
                closest_char = chr(char_wt[abv_index - 1]['char'])
                # Since we chose something with a lower brightness value than existing, this will
                # add to the deficit in my error term (get more negative/less positive)
                delta_error = delta_error + (delta_lower - calibrated_pixel)
            else:
                closest_char = chr(char_wt[abv_index]['char'])
                delta_error = delta_error + (delta_upper - calibrated_pixel)
            row_string += closest_char
        ascii_art += row_string + "\r\n";
    return ascii_art

if __name__ == '__main__':
    # This picture looks horrible both ways
    print "Dark Background:"
    print ASCIIify('http://www.tothebe.at/files/saxbig.gif', 120, True)
    print "Light Background:"
    print ASCIIify('http://www.tothebe.at/files/saxbig.gif', 120, False)
