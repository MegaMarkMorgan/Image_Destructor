from flask import Flask, request, url_for, redirect, render_template
from PIL import Image, ImageFilter
import random


app = Flask(__name__)

#Start Page
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pic = Image.open("/home/MarkMorgan/mysite/static/digital_memory.png")
        def func1():
            pic.rotate(45).save("/home/MarkMorgan/mysite/static/digital_memory.png")
        def func2():
            pic.quantize(colors=124).save("/home/MarkMorgan/mysite/static/digital_memory.png")
        def func3():
            pic.resize((1002, 1600)).save("/home/MarkMorgan/mysite/static/digital_memory.png")
        def func4():
            pic.convert('RGB').reduce(2).save("/home/MarkMorgan/mysite/static/digital_memory.png")
        def func5():
            pic.convert('RGB').filter(filter=ImageFilter.SHARPEN).save("/home/MarkMorgan/mysite/static/digital_memory.png")
        def func6():
            HSV= pic.convert('HSV')
            H, S, V = HSV.split()
            H = H.point(lambda p: p+40)
            HSVr = Image.merge('HSV', (H,S,V))
            RGBr = HSVr.convert('RGB')
            RGBr.save("/home/MarkMorgan/mysite/static/digital_memory.png")
        my_list = [func1, func2, func3, func4, func5, func6,]
        random.choice(my_list)()

        return redirect(url_for('stage1'))
    return render_template('index.html')

#stage1:
@app.route("/stage1", methods=['GET', 'POST'])
def stage1():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('stage1.html')

if __name__ == '__main__':
    app.run()
