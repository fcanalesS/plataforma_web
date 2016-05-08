# coding=utf-8
import base64
from mpi4py import MPI
import web, os, sys, cv2, numpy as np
import efectos1

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def test():
    print rank
    print size



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
        test()

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
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        alt, ancho, channel = img.shape
        rank = comm.Get_rank()
        size = comm.Get_size()

        if alt < size:
            raise web.redirect('/editar-imagen')
        else:
            print "SIZE: ", size
            print "RANK: ", rank
            region = img[(alt / size) * rank:(alt / size) * (rank + 1), 0:ancho]
            # res_bgr = efectos1.Enhanced(region)
            cv2.imwrite(image_path + 'regionEditada_' + str(rank) + '.jpg', region)

            #_, data = cv2.imencode('.jpg', res_bgr)
            #jpeg_base64 = base64.b64encode(data.tostring())

            # Tomar tiempo hasta aquí
            #return jpeg_base64


class Negative:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        result = abs(255 - img)

        _, data = cv2.imencode('.jpg', result)
        jpeg_base64 = base64.b64encode(data.tostring())
        return jpeg_base64


class Sepia:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        kernel = np.array(
            ([0.272, 0.543, 0.131],
             [0.349, 0.686, 0.168],
             [0.393, 0.769, 0.189])
        )

        result = cv2.transform(img, kernel)

        _, data = cv2.imencode('.jpg', result)
        jpeg_base64 = base64.b64encode(data.tostring())
        return jpeg_base64


class BGR:
    def GET(self):
        blue = (float(web.input().blue) + 100) / 100
        green = (float(web.input().green) + 100) / 100
        red = (float(web.input().red) + 100) / 100

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        b, g, r = cv2.split(img)

        b = cv2.multiply(b, np.array([blue]))
        g = cv2.multiply(g, np.array([green]))
        r = cv2.multiply(r, np.array([red]))

        res = cv2.merge((b, g, r))
        _, data = cv2.imencode('.jpg', res)
        jpeg_base64 = base64.b64encode(data.tostring())
        return jpeg_base64


class BrilloContraste:
    def GET(self):
        brillo = (float(web.input().brillo) + 100) / 100
        contraste = (float(web.input().contraste) + 100) / 100

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        img2hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(img2hsv)

        s = cv2.multiply(s, np.array([contraste]))
        v = cv2.multiply(v, np.array([brillo]))

        res = cv2.merge((h, s, v))

        _, data = cv2.imencode('.jpg', cv2.cvtColor(res, cv2.COLOR_HSV2BGR))
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Rotate:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        angle = float(web.input().angle)
        rows, cols, _ = img.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        dst = cv2.warpAffine(img, M, (cols, rows))

        _, data = cv2.imencode('.jpg', dst)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Mirror:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        mirror = cv2.flip(img, 1)

        _, data = cv2.imencode('.jpg', mirror)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Blur:
    def GET(self):
        blur = int(web.input().blur)

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        output = cv2.blur(img, (blur, blur))

        _, data = cv2.imencode('.jpg', output)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Sharp:
    def GET(self):
        sharp = int(web.input().sharp)

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        # Create the identity filter, but with the 1 shifted to the right!
        kernel = np.zeros((sharp, sharp), np.float32)
        kernel[sharp - 1, sharp - 1] = 2.0  # Identity, times two!

        # Create a box filter:
        boxFilter = np.ones((sharp, sharp), np.float32) / float(pow(sharp, 2))

        # Subtract the two:
        kernel = kernel - boxFilter

        # Note that we are subject to overflow and underflow here...but I believe that
        # filter2D clips top and bottom ranges on the output, plus you'd need a
        # very bright or very dark pixel surrounded by the opposite type.

        custom = cv2.filter2D(img, -1, kernel)

        _, data = cv2.imencode('.jpg', custom)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Convolucion:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        kernel = np.ones((5, 5), np.float32) / 25
        dst = cv2.filter2D(img, -1, kernel)

        _, data = cv2.imencode('.jpg', dst)
        jpeg_base64 = base64.b64encode(data.tostring())

        return jpeg_base64


class Fourier:
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


class DispGaussian:
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
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        edges = cv2.Canny(img, int(web.input().val1), int(web.input().val2))

        _, data = cv2.imencode('.jpg', edges)
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
