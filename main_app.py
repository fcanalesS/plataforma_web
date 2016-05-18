# coding=utf-8
import base64, zipfile
from mpi4py import MPI

import cv2
import numpy as np
import os

import web

p = 4 # procesadores a utilizar

urls = (
    '/', 'SubirImagen',
    '/editar-imagen', 'EditarImagen',
    '/editar-imagen2', 'EditarImagen2',
    '/editar-imagen3', 'EditarImagen3',
    '/editar-imagen4', 'EditarImagen4',
    '/hdr', 'HDR',
    '/time-lapse', 'TimeLapse',
    '/bullet-time', 'BulletTime',
    '/enhanced', 'Enhanced',
    '/negative', 'Negative',
    '/sepia', 'Sepia',
    '/bgr', 'BGR',
    '/brillo-contraste', 'BrilloContraste',
    '/rotate', 'Rotate',
    '/mirror', 'Mirror',
    '/blur', 'Blur',
    '/sharp', 'Sharp',
    '/convolucion', 'Convolucion',
    '/fourier', 'Fourier',
    '/disp-gaussian', 'DispGaussian',
    '/border', 'Border',
    '/pruebas', 'Test',
    '/pruebas-ajax', 'Test_ajax'

)

app = web.application(urls, locals())

static_dir = os.path.abspath(os.path.dirname(__file__)) + '/static'
template_dir = os.path.abspath(os.path.dirname(__file__)) + '/template'
htmlout = web.template.render(template_dir, base='layout')
htmlout2 = web.template.render(template_dir, base='layout2')
render_plain = web.template.render('template/')
global message
message = ''


def variables_globales():
    web.config.debug = True

    web.template.Template.globals['render'] = render_plain
    web.template.Template.globals['msg'] = message


app.add_processor(web.loadhook(variables_globales))


class SubirImagen:
    def GET(self):
        filedir = os.getcwd() + '/images'
        return htmlout.subir_imagen()

    def POST(self):
        x = web.input(upload_file={})
        filedir = os.getcwd() + '/images'  # change this to the directory you want to store the file in.
        if 'upload_file' in x:  # to check if the file-object is created
            filepath = x.upload_file.filename.replace('\\', '/')  # replaces the windows-style slashes with linux ones.
            filename = filepath.split('/')[-1]  # splits the and chooses the last part (the filename with extension)
            fout = open(filedir + '/' + filename, 'w')  # creates the file where the uploaded file should be stored
            fout.write(x.upload_file.file.read())  # writes the uploaded file to the newly created file.
            fout.close()  # closes the file, upload complete.

        raise web.seeother('editar-imagen')


class EditarImagen:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return htmlout.editar_imagen(jpeg_base64)


class EditarImagen2:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return htmlout.editar_imagen2(jpeg_base64)


class EditarImagen3:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return htmlout.editar_imagen3(jpeg_base64)


class EditarImagen4:
    def GET(self):
        os.system('rm ' + os.getcwd() + '/static/video/' + '*.mp4')

        return htmlout.editar_imagen4()

    def POST(self):
        x = web.input(images_hdr={})
        print x['images_hdr'].filename
        if x.images == 'hdr':
            filedir = os.getcwd() + '/hdr'
            if 'images_hdr' in x:
                filepath = x.images_hdr.filename.replace('\\', '/')
                filename = filepath.split('/')[-1]
                fout = open(filedir + '/' + filename, 'w')
                fout.write(x.images_hdr.file.read())
                fout.close()
            os.system('unzip ' + filedir + '/' + x['images_hdr'].filename + ' -d ' + filedir + '/')
            os.system('rm ' + filedir + '/' + x['images_hdr'].filename)
            global message
            message = 'HDR'
            raise web.seeother('/hdr')
        elif x.images == 'timelapse':
            filedir = os.getcwd() + '/timelapse'
            if 'images_hdr' in x:
                filepath = x.images_hdr.filename.replace('\\',
                                                         '/')
                filename = filepath.split('/')[-1]
                fout = open(filedir + '/' + filename, 'w')
                fout.write(x.images_hdr.file.read())
                fout.close()
            os.system('unzip ' + filedir + '/' + x['images_hdr'].filename + ' -d ' + filedir + '/')
            os.system('rm ' + filedir + '/' + x['images_hdr'].filename)
            raise web.seeother('/time-lapse')
        elif x.images == 'bullettime':
            filedir = os.getcwd() + '/bulletTime'
            if 'images_hdr' in x:
                filepath = x.images_hdr.filename.replace('\\',
                                                         '/')
                filename = filepath.split('/')[-1]
                fout = open(filedir + '/' + filename, 'w')
                fout.write(x.images_hdr.file.read())
                fout.close()
            os.system('unzip ' + filedir + '/' + x['images_hdr'].filename + ' -d ' + filedir + '/')
            os.system('rm ' + filedir + '/' + x['images_hdr'].filename)
            raise web.seeother('/bullet-time')


class HDR:
    def GET(self):
        ######
        os.system('mpiexec -np %s python hdr.py' % p)  # Corta y aplica efecto
        # os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        img = cv2.imread(os.getcwd() + '/hdr/hdr.jpg', cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return htmlout.result(jpeg_base64)


class TimeLapse:
    def GET(self):
        ######
        # os.system('mpiexec -np %s python timelapse.py' % p)  # Corta y aplica efecto
        ######

        video_path = os.getcwd() + '/static/video/hdrVideo.mp4'

        return htmlout.result2(video_path)


class BulletTime:
    def GET(self):
        ######
        os.system('mpiexec -np %s python bullettime.py' % p)  # Corta y aplica efecto
        # os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        video_path = os.getcwd() + '/static/video/hdrVideo.mp4'

        return htmlout.result3(video_path)


class Enhanced:
    def GET(self):
        ######
        os.system('mpiexec -np %s python automejora.py' % p)  # Corta y aplica efecto
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        image_path = os.getcwd() + '/images/'
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Negative:
    def GET(self):
        ######
        os.system('mpiexec -np %s python negativo.py' % p)
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())
        return jpeg_base64


class Sepia:
    def GET(self):
        ######
        os.system('mpiexec -np %s python sepia.py' % p)
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class BGR:
    def GET(self):
        blue = (float(web.input().blue) + 100) / 100
        green = (float(web.input().green) + 100) / 100
        red = (float(web.input().red) + 100) / 100

        ######
        os.system('mpiexec -np %s python bgr.py %s %s %s' % (p, blue, green, red))
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())
        return jpeg_base64


class BrilloContraste:
    def GET(self):
        brillo = (float(web.input().brillo) + 100) / 100
        contraste = (float(web.input().contraste) + 100) / 100

        ######
        os.system('mpiexec -np %s python bc.py %s %s' % (p, brillo, contraste))
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Rotate:
    def GET(self):
        angle = float(web.input().angle)
        ######
        os.system('mpiexec -np %s python rotar.py %s' % (p, angle))
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionRotada.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Mirror:
    def GET(self):
        ######
        os.system('mpiexec -np %s python espejo.py' % p)
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Blur:
    def GET(self):
        blur = int(web.input().blur)
        ######
        os.system('mpiexec -np %s python blur.py %s' % (p, blur))
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        image_path = os.getcwd() + '/images/'
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Sharp:
    def GET(self):
        sharp = int(web.input().sharp)

        ######
        os.system('mpiexec -np %s python sharp.py %s' % (p, sharp))
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionEditada_0.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Convolucion:
    def GET(self):
        ######
        os.system('mpiexec -np %s python convolucion.py' % p)
        # os.system('mpiexec -np %s python sharp.py %s' % sharp)  # Limpieza
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionConvolucion.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Fourier:  # Pendiente
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)

        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

        _, data = cv2.imencode('.jpg', magnitude_spectrum)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class DispGaussian:  # Pendiente
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        dst = cv2.GaussianBlur(img, (5, 5), 0)
        for i in xrange(1, 1000):  # Para aplicarl filtro n veces
            dst = cv2.GaussianBlur(dst, (5, 5), 0)

        _, data = cv2.imencode('.jpg', dst)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Border:
    def GET(self):
        ######
        os.system('mpiexec -np %s python border.py %s %s' % (p, int(web.input().val1), int(web.input().val2)))
        os.system('mpiexec -np %s python limpieza.py' % p)  # Pega y borra fotos restantes
        ######
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + 'regionBorder.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Test:
    def GET(self):
        return render_plain.test()


class Test_ajax:
    def GET(self):
        print web.input()


if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
