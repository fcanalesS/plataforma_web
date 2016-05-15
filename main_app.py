# coding=utf-8
import base64
from mpi4py import MPI

import cv2
import numpy as np
import os

import time
import web

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



urls = (
    '/', 'SubirImagen',
    '/editar-imagen', 'EditarImagen',
    '/editar-imagen2', 'EditarImagen2',
    '/editar-imagen3', 'EditarImagen3',
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
message = ''


def variables_globales():
    web.config.debug = True

    web.template.Template.globals['render'] = render_plain
    # web.template.Template.globals['data_bgr'] = Procesar_bgr().data_bgr
    # web.template.Template.globals['css'] = Layout_main().main_css
    # web.template.Template.globals['header'] = Layout_main().main_header
    # web.template.Template.globals['footer'] = Layout_main().main_footer
    # web.template.Template.globals['arregla_fecha'] = Layout_main().arregla_fecha
    # web.template.Template.globals['arregla_link'] = Layout_main().arregla_link
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


class Enhanced:
    def GET(self):
        ######
        os.system('mpiexec -np 4 python automejora.py')  # Corta y aplica efecto
        os.system('python limpieza.py')  # Pega y borra fotos restantes
        ########################################################################

        ######

        image_path = os.getcwd() + '/images/'
        img = cv2.imread(image_path + 'imagenLista.jpg', cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Negative:
    def GET(self):
        ######
        os.system('mpiexec -np 4 python negativo.py')
        # os.system('mpiexec -np 4 python negativo2.py')
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())
        return jpeg_base64


class Sepia:
    def GET(self):
        ######
        os.system('mpiexec -np 4 python sepia.py')
        # os.system('mpiexec -np 4 python sepia2.py')
        ######
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class BGR:
    def GET(self):
        blue = (float(web.input().blue) + 100) / 100
        green = (float(web.input().green) + 100) / 100
        red = (float(web.input().red) + 100) / 100

        ######
        os.system('mpiexec -np 4 python bgr.py %s %s %s' % (blue, green, red))
        # os.system('mpiexec -np 4 python bgr.py') # Limpiar imagenes bgr :D
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)


        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())
        return jpeg_base64


class BrilloContraste:
    def GET(self):
        brillo = (float(web.input().brillo) + 100) / 100
        contraste = (float(web.input().contraste) + 100) / 100

        ######
        os.system('mpiexec -np 4 python bc.py %s %s' % (brillo, contraste))
        # os.system('mpiexec -np 4 python bc.py')  # limpiar imágenes y dejar la buena
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Rotate:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        angle = float(web.input().angle)

        ######
        os.system('mpiexec -np 4 python rotar.py %s' % angle)
        # os.system('mpiexec -np 4 python rotar.py %s' % angle)  # Limpieza
        ######

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Mirror:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        ######
        os.system('mpiexec -np 4 python espejo.py')
        # os.system('mpiexec -np 4 python espejo.py')  # Limpieza
        ######

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Blur:
    def GET(self):
        blur = int(web.input().blur)
        ######
        os.system('mpiexec -np 4 python blur.py %s' % blur)
        # os.system('mpiexec -np 4 python espejo.py')  #Limpieza
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Sharp:
    def GET(self):
        sharp = int(web.input().sharp)

        ######
        os.system('mpiexec -np 4 python sharp.py %s' % sharp)
        # os.system('mpiexec -np 4 python sharp.py %s' % sharp)  # Limpieza
        ######

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        _, data = cv2.imencode('.jpg', img)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Convolucion:
    def GET(self):
        ######
        os.system('mpiexec -np 4 python convolucion.py')
        # os.system('mpiexec -np 4 python sharp.py %s' % sharp)  # Limpieza
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


class DispGaussian: # Pendiente
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
        os.system('mpiexec -np 4 python border.py %s %s' % (int(web.input().val1), int(web.input().val2)))
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


if __name__ == '__main__' and rank == 0:
    app.run()
else:
    application = app.wsgifunc()
