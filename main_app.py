# coding=utf-8
import base64
import json

import web, os, sys, cv2, numpy as np

include_dirs = ['libs']

for dirname in include_dirs:
    sys.path.append(os.path.dirname(__file__) + '/' + dirname)

# from image_bgr import Procesar_bgr

urls = (
    '/', 'SubirImagen',
    '/editar-imagen', 'EditarImagen',
    '/enhanced', 'Enhanced',
    '/negative', 'Negative',
    '/sepia', 'Sepia',
    '/bgr', 'BGR',
    '/brillo-contraste', 'BrilloContraste',
    '/pruebas', 'Test',
    '/pruebas-ajax', 'Test_ajax'

)

app = web.application(urls, locals())

static_dir = os.path.abspath(os.path.dirname(__file__)) + '/static'
template_dir = os.path.abspath(os.path.dirname(__file__)) + '/template'
htmlout = web.template.render(template_dir, base='layout')
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


class Enhanced:
    def GET(self):
        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)

        # Tomar tiempo de aqui
        b, g, r = cv2.split(img)

        equb = cv2.equalizeHist(b)
        equg = cv2.equalizeHist(g)
        equr = cv2.equalizeHist(r)

        res_bgr = cv2.merge((equb, equg, equr))

        _, data = cv2.imencode('.jpg', res_bgr)
        jpeg_base64 = base64.b64encode(data.tostring())

        # Tomar tiempo hasta aquí
        return jpeg_base64
        # return htmlout.editar_imagen(jpeg_base64)


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
        blue = (float(web.input().blue)+100)/100
        green = (float(web.input().green)+100)/100
        red = (float(web.input().red)+100)/100

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
        brillo = (float(web.input().brillo)+100)/100
        contraste = (float(web.input().contraste)+100)/100

        image_path = os.getcwd() + '/images/'
        img_list = os.listdir(image_path)
        img = cv2.imread(image_path + img_list[0], cv2.IMREAD_COLOR)
        img2hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(img2hsv)

        h =cv2.multiply(h, np.array([contraste]))
        v =cv2.multiply(v, np.array([brillo]))

        res = cv2.merge((h, s, v))

        _, data = cv2.imencode('.jpg', cv2.cvtColor(res, cv2.COLOR_HSV2BGR))
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
