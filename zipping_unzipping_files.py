# Zipping and unzipping files
import zipfile, shutil

f = open('fileone.txt', 'w')
f.write("FIRST FILE")
f.close()

f = open('filetwo.txt', 'w')
f.write("SECOND FILE")
f.close()

# Zipping/Compressing

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# Unzipping

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')


# shell util(shutil)
dir_to_zip = 'C:\\Users\\user\\Documents\\GitHub\\python\\extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')





