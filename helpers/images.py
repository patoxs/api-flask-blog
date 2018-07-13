from __future__ import print_function
import os, sys, uuid
import io

from PIL import Image, ImageOps

from werkzeug.utils import secure_filename

SIZES = [(960, 960),(960,480),(480,480),(460,272),(460,752),(60,60),(1260,680),(380,320)]
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = ROOT_DIR+'/../files'
IMAGE_FOLDER = ROOT_DIR+'/../static/image/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

class ImageProcessing:

	def create_images(self, type_img, image):
		outfile = uuid.uuid4()
		try:
			for idx, size in enumerate(SIZES):
				folder = idx+1
				if type_img == 'thumb':
					self.thumb_img(image,outfile,size,folder)
				else:
					self.crop_img(image,outfile,size,folder)
			return str(outfile)+'.jpg'
		except IOError:
			print("cannot create thumbnail for", image)

	def thumb_img(self, infile, outfile, size, folder):
		try:
			modified_path = IMAGE_FOLDER+str(folder)+'/'+str(outfile)+'.jpg'
			im = Image.open(UPLOAD_FOLDER+'/'+infile)
			im.thumbnail(size)
			im.save(modified_path, "JPEG")
		except IOError:
			print("cannot create thumbnail for", infile)

	def crop_img(self, infile, outfile, size, folder):
		try:
			modified_path = IMAGE_FOLDER+str(folder)+'/'+str(outfile)+'.jpg'
			im = Image.open(UPLOAD_FOLDER+'/'+infile)
			method = Image.NEAREST if im.size == size else Image.ANTIALIAS
			formatted_im = ImageOps.fit(im, size, method = method, centering = (0.5,0.5))
			formatted_im.save(modified_path, "JPEG", quality=90)
		except IOError:
			print("cannot create thumbnail for", infile)

	def allowed_file(self, filename):
		return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	def upload_file(self, infile):
		if self.allowed_file(infile.filename):
			print(UPLOAD_FOLDER+'/'+infile.filename)
			infile.save(UPLOAD_FOLDER+'/'+infile.filename)
			infile.close()
			return infile.filename
		else:
			return {"massage":"invalid file format"}
