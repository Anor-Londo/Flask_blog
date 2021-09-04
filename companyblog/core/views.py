from flask import render_template,request,Blueprint
from puppycompanyblog.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    Home page view.
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page.
    '''
    return render_template('info.html')
