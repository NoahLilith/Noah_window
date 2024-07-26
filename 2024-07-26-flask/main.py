from flask import Flask,render_template,request
import data

app = Flask(__name__)
@app.route("/")
def index1():
    return render_template("index1.html.jinja")

@app.route("/index1")
def index():
    #print(list(map(lambda value:value[0],data.get_areas())))
    selected_area = request.args.get('area')
    areas = [tup[0] for tup in data.get_areas()]
    selected_area = '�h�L��' if selected_area is None else selected_area
    detail_snaes = data.get_snaOfArea(area=selected_area)
    
    #areas->�Ҧ���F�� 
    #show_area -> �n��ܪ���F��
    #detail_snaes -> �Ӧ�F�ϩҦ����I��T   
    return render_template('index.html.jinja',areas=areas,show_area=selected_area,detail_snaes=detail_snaes)    
    
    
    
    
    
    