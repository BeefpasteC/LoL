from django.shortcuts import render_to_response

def index(request):
    dicts = {
        "student": [
            {"name": "张三","加载":"97%","p":"../static/image/1.jpg","头像":"../static/image/11.jpg","技能":"../static/image/13.png"},
            {"name": "李四","加载":"98%","p":"../static/image/2.jpg","头像":"../static/image/11.jpg","技能":"../static/image/13.png"},
            {"name": "王五","加载":"97%","p":"../static/image/3.jpg","头像":"../static/image/11.jpg","技能":"../static/image/13.png"},
            {"name": "赵大","加载":"99%","p":"../static/image/4.jpg","头像":"../static/image/11.jpg","技能":"../static/image/13.png"},
            {"name": "钱七","加载":"99%","p":"../static/image/5.jpg","头像":"../static/image/11.jpg","技能":"../static/image/13.png"},
            {"name": "刘大","加载":"99%","p":"../static/image/6.jpg","头像":"../static/image/12.jpg","技能":"../static/image/13.png"},
            {"name": "戴九","加载":"99%","p":"../static/image/7.jpg","头像":"../static/image/12.jpg","技能":"../static/image/13.png"},
            {"name": "黄弎","加载":"99%","p":"../static/image/8.jpg","头像":"../static/image/12.jpg","技能":"../static/image/13.png"},
            {"name": "郑二","加载":"99%","p":"../static/image/9.jpg","头像":"../static/image/12.jpg","技能":"../static/image/13.png"},
            {"name": "乔八","加载":"99%","p":"../static/image/10.jpg","头像":"../static/image/12.jpg","技能":"../static/image/13.png"},
        ]
    }
    return render_to_response("index.html",locals())